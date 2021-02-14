from django.core.management.base import BaseCommand

from packages.services import FullTextSearchService


class Command(BaseCommand):
    """

    @author: Kamil Żuchowski (kamil@kzuchowskinss.pl).
    """
    help = 'test'

    def handle(self, *args, **options):
        found_results = FullTextSearchService.search_package("pypi")
        for result in found_results:
            print(result.title)
        y = ""

        self.stdout.write(
            self.style.SUCCESS('>>>>>>>>>>>>>>>>>>>>>>>>> test code <<<<<<<<<<<<<<<<<<<<<<<<<<'))
