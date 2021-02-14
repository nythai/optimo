from django.core.management.base import BaseCommand

from packages.tasks import load_python_packages_data


class Command(BaseCommand):
    """
    Loads packages data to database.

    @author: Kamil Żuchowski (kamil@kzuchowskinss.pl).
    """
    help = 'Command to load python packages information to database.'

    def handle(self, *args, **options):
        load_python_packages_data()

        self.stdout.write(
            self.style.SUCCESS('>>>>>>>>>>>>>>>>>>>> Successfully loaded python packages data <<<<<<<<<<<<<<<<<<<<'))
