from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Updates fulltext search engine index with python packages data.

    @author: Kamil Żuchowski (kamil@kzuchowskinss.pl).
    """
    help = 'Command updated fulltext search engine index with python packages data.'

    def handle(self, *args, **options):



        self.stdout.write(
            self.style.SUCCESS('>>>>>>>>>>>>>>>>>>>> Successfully updated index <<<<<<<<<<<<<<<<<<<<'))
