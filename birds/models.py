from django.db import models


class TaxonomicLevel(models.Model):
    name = models.CharField(max_length=20)
    depth = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return self.name


class TaxonomicGroup(models.Model):
    name = models.CharField(max_length=30, unique=True)
    common_name = models.CharField(max_length=50)
    level = models.ForeignKey(TaxonomicLevel)
    parent = models.ForeignKey('self', null=True, blank=True)
    position_within_siblings = models.PositiveSmallIntegerField(null=True)

    def __unicode__(self):
        return self.common_name if self.common_name else self.name


class Species(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    absolute_position = models.PositiveSmallIntegerField(null=True)
    name = models.CharField(max_length=50, unique=True)
    parent = models.ForeignKey(TaxonomicGroup)
    common_name = models.CharField(max_length=50)
    french_name = models.CharField(max_length=50)
    nacc_annotation = models.TextField()
    nacc_is_accidental = models.NullBooleanField()
    nacc_is_hawaiian = models.NullBooleanField()
    nacc_is_introduced = models.NullBooleanField()
    nacc_is_nonbreeding = models.NullBooleanField()
    nacc_is_extinct = models.NullBooleanField()
    nacc_is_misplaced = models.NullBooleanField()

    def __unicode__(self):
        return self.name

    def important_field_differs(self, other):
        return (
            self.name != other.name or
            self.parent != other.parent or
            self.common_name != other.common_name or
            self.nacc_is_accidental != other.nacc_is_accidental or
            self.nacc_is_hawaiian != other.nacc_is_hawaiian or
            self.nacc_is_introduced != other.nacc_is_introduced or
            self.nacc_is_nonbreeding != other.nacc_is_nonbreeding or
            self.nacc_is_extinct != other.nacc_is_extinct or
            self.nacc_is_misplaced != other.nacc_is_misplaced
        )

    def update_aou_fields(self, other):
        self.name = other.name
        self.parent = other.parent
        self.common_name = other.common_name
        self.french_name = other.french_name
        self.nacc_annotation = other.nacc_annotation
        self.nacc_is_accidental = other.nacc_is_accidental
        self.nacc_is_hawaiian = other.nacc_is_hawaiian
        self.nacc_is_introduced = other.nacc_is_introduced
        self.nacc_is_nonbreeding = other.nacc_is_nonbreeding
        self.nacc_is_extinct = other.nacc_is_extinct
        self.nacc_is_misplaced = other.nacc_is_misplaced
