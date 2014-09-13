import re

from django.shortcuts import render, get_object_or_404

from birds.models import Species
from creations.models import Creation, Research, ResearchCategory


def birds(request):
    was_search = False
    search_birds = []
    if 'query' in request.GET:
        was_search = True
        terms = request.GET['query'].split()
        birds = Species.objects.filter(is_visible=True)
        for bird in birds:
            for term in terms:
                if (term.lower() not in bird.name.lower() and
                        term.lower() not in bird.common_name.lower()):
                    break
            else:
                search_birds.append(bird)

    context = {
        'was_search': was_search,
        'search_birds': search_birds,
    }

    return render(request, 'birds.html', context)


def birds_taxonomical(request):
    birds = Species.objects.raw(
        'SELECT species.id, species.name, species.common_name, '
        'G.name AS genus_name, '
        'S.name AS subfamily_name, '
        'S.common_name AS subfamily_common, '
        'F.name AS family_name, '
        'F.common_name AS family_common, '
        'O.name AS order_name, '
        'O.common_name AS order_common '
        'FROM birds_species AS species '
        'LEFT JOIN birds_taxonomicgroup AS G '
        'ON species.parent_id=G.id '
        'LEFT JOIN birds_taxonomicgroup AS S '
        'ON (G.parent_id=S.id AND S.level_id=3) '
        'LEFT JOIN birds_taxonomicgroup AS F '
        'ON (S.parent_id=F.id OR G.parent_id=F.id) AND F.level_id=2 '
        'LEFT JOIN birds_taxonomicgroup AS O '
        'ON F.parent_id=O.id '
        'WHERE species.is_visible = 1 '
        'ORDER BY species.absolute_position'
    )

    context = {
        'birds': birds,
    }

    return render(request, 'birds_taxonomical.html', context)


def bird(request, id):
    bird = get_object_or_404(Species, id=id)

    try:
        bird.minnesotaspecies
        bird.is_minnesotan = True
    except AttributeError:
        bird.is_minnesotan = False

    actual_creations = []
    for creation in bird.creation_set.all():
        # Get actual instances to take advantage of polymorphic fields
        actual_creation = creation.get_actual_instance()

        # Format the title to display for this creation
        class_name = actual_creation.__class__.__name__
        words = re.findall('[A-Z][^A-Z]*', class_name)
        actual_creation.category = ' '.join(words)

        # Split up Research instances by research subcategory
        if actual_creation.category.lower() == 'research':
            actual_creation.category = actual_creation.research_category

        actual_creations.append(actual_creation)

    # Sort by creation type in order to use template 'regroup'
    actual_creations = sorted(actual_creations,
                              key=lambda x: x.category)

    context = {
        'bird': bird,
        'actual_creations': actual_creations,
    }

    return render(request, 'bird.html', context)
