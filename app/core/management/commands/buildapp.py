import os

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand

AVAILABLE_BUILD_PARAMETERS = ['production', 'development']
WARN_BUILD_PROFILES = ['production']


class Command(BaseCommand):
    """
    Parametrized build script:
    Takes as --profile parameter one of AVAILABLE_BUILD_PARAMETERS.
    Use --acceptrisk when about to rebuild production or any of WARN_BUILD_PROFILES.
    Example: $> python manage.py buildapp --profile development
    """
    help = 'Builds an app. CAUTION: It clears profile\'s database'

    def add_arguments(self, parser):
        parser.add_argument(
            '--profile',
            dest='profile',
            required=True,
            help='Select building profile',
        )
        parser.add_argument(
            '--acceptrisk',
            '-R',
            dest='acceptrisk',
            required=False,
            help='Required if about to rebuild profiles under risk group',
            default=False
        )

    def handle(self, *args, **options):
        profile = options['profile']

        if profile in WARN_BUILD_PROFILES and options['acceptrisk'] is False:
            self.stdout.write(self.style.ERROR(
                'You are about to rebuild profile under risk group. Rerun command with --acceptrisk true parameter.'))
            exit(1)

        if profile not in AVAILABLE_BUILD_PARAMETERS:
            self.stdout.write(self.style.ERROR('Invalid profile parameter. These are available parameters:'))
            for available_profile in AVAILABLE_BUILD_PARAMETERS:
                self.stdout.write(available_profile + ',\n')

            exit(1)

        # Check if settings are correct (are equal to building profile ex. stage=stage)
        with open(os.path.join(settings.BASE_DIR, 'optimo/settings/__init__.py'), 'r+') as settings_file:
            settings_file_content = settings_file.read()

        # When profile mismatch change settings rerun script
        if profile + ' ' not in settings_file_content:
            with open(os.path.join(settings.BASE_DIR, 'optimo/settings/__init__.py'), 'w') as settings_file:
                settings_file.write('from .%s import *' % profile)
                settings_file.truncate()

                self.stdout.write(self.style.ERROR('Replaced database configuration, rerun script.'))
                # rerun command
                return self.handle(**options)

        call_command('cleardatabase')
        call_command('removemigrations')
        call_command('makemigrations', interactive=False)
        call_command('migrate', interactive=False)
        self.stdout.write(self.style.SUCCESS('Migrated.'))

        self.stdout.write(self.style.SUCCESS('>>>>>>>>>>>>>>>>>>>>>>>>> Successful build <<<<<<<<<<<<<<<<<<<<<<<<<<'))
