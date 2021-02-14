from django.core.management.base import BaseCommand
from elasticsearch import Elasticsearch

from packages.documents import PackageDocument


class Command(BaseCommand):
    """
    Removes elasticsearch index.

    @author: Kamil Żuchowski (kamil@kzuchowskinss.pl).
    """
    help = 'Command to remove elasticsearch index data.'

    def handle(self, *args, **options):
        es = Elasticsearch()
        es.indices.delete(index=PackageDocument.Index.name, ignore=[400, 404])

        self.stdout.write(
            self.style.SUCCESS('>>>>>>>>>>>>>>>>>>>> Successfully removed index <<<<<<<<<<<<<<<<<<<<'))
