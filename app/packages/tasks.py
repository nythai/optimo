from celery import Celery

from packages.models import Package
from packages.services import PackageParserService

app = Celery('optimo')


@app.task
def load_python_packages_data():
    """
    Parses python packages rss feed and loads them to database.
    Searches for existing package first based on guid, when found it updates existing one if not, creates new.


    :return: void
    @author: Kamil Żuchowski (kamil@kzuchowskinss.pl).
    """
    parsing_service = PackageParserService()
    parsed_packages = parsing_service.parse_packages_from_rss_source()
    for parsed_package in parsed_packages:
        try:
            # when package exists then update
            package = Package.objects.get(guid=parsed_package['guid'])
        except Package.DoesNotExist:
            package = Package()
        package.populate_from_rss_raw_package(parsed_package)
        package.save()

    print("Added/Updated %s packages." % len(parsed_packages))