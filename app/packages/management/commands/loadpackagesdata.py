from django.core.management.base import BaseCommand

from packages.tasks import parse_and_load_feed


class Command(BaseCommand):
    """
    Loads packages data to database.

    @author: Kamil Żuchowski (kamil@kzuchowskinss.pl).
    """
    help = 'Command loads python packages information to database.'

    def handle(self, *args, **options):
        parse_and_load_feed()

        self.stdout.write(
            self.style.SUCCESS('>>>>>>>>>>>>>>>>>>>> Successfully loaded python packages data <<<<<<<<<<<<<<<<<<<<'))
