import os

from django.core.management.base import BaseCommand
from django.db import connection

from django.conf import settings

from packagesloader.tasks import parse_and_load_feed


class Command(BaseCommand):
    """
    """
    help = 'test'

    def handle(self, *args, **options):
        parse_and_load_feed()

        self.stdout.write(
            self.style.SUCCESS('>>>>>>>>>>>>>>>>>>>>>>>>> test code <<<<<<<<<<<<<<<<<<<<<<<<<<'))
