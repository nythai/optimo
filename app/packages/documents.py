from django.conf import settings
from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from packages.models import Package


@registry.register_document
class PackageDocument(Document):
    """
    Elasticsearch document class created to configure Elasticsearch document and map with Django model.

    @author: Kamil Żuchowski (kamil@kzuchowskinss.pl).
    """
    class Index:
        name = "packages"

        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Package

        fields = [
            'title',
            'link',
            'guid',
            'description',
            'author_email',
        ]

        queryset_pagination = settings.PACKAGES_PAGINATION_PAGE_LIMIT
