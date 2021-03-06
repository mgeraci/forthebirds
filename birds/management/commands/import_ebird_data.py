import argparse

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from birds.models import Species

import csv


class Command(BaseCommand):
    help = 'Migrate bird data from eBird csv'

    def add_arguments(self, parser):
        parser.add_argument('ebird_csv', type=argparse.FileType('r'),
                            help='CSV of species data from eBird')

    def handle(self, **options):
        # Create dictionary of rows that already exist in species database,
        # mapping ebird id to the Species object.

        ebird_to_existing = {}

        for bird in Species.objects.all():
            ebird_to_existing[bird.ebird_id] = bird

        for row in csv.DictReader(options['ebird_csv']):
            if row['CATEGORY'] != 'species':
                continue

            ebird_id = row['SPECIES_CODE']

            try:
                bird = ebird_to_existing[ebird_id]
            except KeyError:
                bird = Species(ebird_id=ebird_id)

            # Replace existing fields
            common_name = row['PRIMARY_COM_NAME'].decode('utf-8')
            if bird.common_name:
                if bird.common_name != common_name:
                    s = (u'Changing common from {} to {}'
                         .format(bird.common_name, common_name))

                    if bird.is_visible:
                        self.stderr.write(s)
                    else:
                        self.stderr.write('\t' + s)

            bird.common_name = common_name

            slug = slugify(common_name)
            if bird.slug and bird.slug != slug:
                s = ('Changing slug from {} to {}'
                     .format(bird.slug, slug))
                if bird.is_visible:
                    self.stderr.write(s)
                else:
                    self.stderr.write('\t' + s)
            bird.slug = slug

            sci_name = row['SCI_NAME']
            if bird.scientific_name and bird.scientific_name != sci_name:
                s = ('Changing scientific from {} to {}'
                     .format(bird.scientific_name, sci_name))
                if bird.is_visible:
                    self.stderr.write(s)
                else:
                    self.stderr.write('\t' + s)
            bird.scientific_name = sci_name

            # new fields
            bird.taxon_order = row['TAXON_ORDER']
            bird.order = row['ORDER1']
            bird.family = row['FAMILY'].split('(')[0].strip()
            bird.family_common = (row['FAMILY'].split('(')[1]
                                  .split(')')[0].strip())
            bird.en_IOC = row['en_IOC']

            bird.save()
