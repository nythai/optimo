import os

from django.core.management.base import BaseCommand
from django.db import connection

from django.conf import settings


class Command(BaseCommand):
    """
    Clears database.
    Check settings before running.
    Example: $> python manage.py cleardatabase
    """
    help = 'Clears database'

    def handle(self, *args, **options):

        # When database is sqlite so we need to remove a file (db)
        if settings.DATABASES['default']['ENGINE'] == 'django.db.backends.sqlite3':
            if os.path.exists(settings.DATABASES['default']['NAME']):
                os.remove(settings.DATABASES['default']['NAME'])
        else:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_type != 'VIEW' AND table_name NOT LIKE 'pg_ts_%%'")
            rows = cursor.fetchall()
            for row in rows:
                try:
                    cursor.execute('drop table %s cascade ' % row[0])
                except:
                    self.stdout.write(self.style.SUCCESS('couldn\'t drop %s' % row[0]))

        self.stdout.write(
            self.style.SUCCESS('>>>>>>>>>>>>>>>>>>>>>>>>> Successful database dropped <<<<<<<<<<<<<<<<<<<<<<<<<<'))
