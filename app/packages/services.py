import elasticsearch
import feedparser
from django.conf import settings
from django.contrib.postgres.search import SearchVector

from packages.documents import PackageDocument
from packages.models import Package


class PackageParserService:
    """
    Service class responsive for parsing python packages rss feed.

    @author: Kamil Żuchowski (kamil@kzuchowskinss.pl).
    """

    def __init__(self):
        self.feed_link = getattr(settings, "PACKAGES_RSS_SOURCE_LINK", "https://pypi.org/rss/packages.xml")

    def parse_packages_from_rss_source(self):
        """
        Parses python packages rss feed returning raw entries.

        :return: raw feed entries
        """
        feed = feedparser.parse(self.feed_link)
        return feed['entries']


class FullTextSearchService:
    """
    Service class responsive for searching for packages data in elasticsearch/database.

    @author: Kamil Żuchowski (kamil@kzuchowskinss.pl).
    """

    @staticmethod
    def search_package(phrase):
        """
        Searches for package first in elasticsearch if will meet any problem data will be searched in database.

        :param phrase: search phrase
        :return: found packages in Elasticsearch by searched phrase
        """
        try:
            return FullTextSearchService._search_package_in_elastic(phrase)
        except elasticsearch.exceptions.ElasticsearchException as ex:
            # faced errors due to Elasticsearch, search in database.
            return FullTextSearchService._search_package_in_db(phrase)

    @staticmethod
    def _search_package_in_elastic(phrase):
        """
        Searching for given phrase in Elasticsearch.

        :param phrase: search phrase
        :return: found packages in database by searched phrase
        """
        return PackageDocument.search().query("query_string", query=phrase).execute()

    @staticmethod
    def _search_package_in_db(phrase):
        """
        Searching for given phrase in database.

        :param phrase: search phrase
        :return: found packages in database by searched phrase
        """
        return Package.objects.annotate(
            search=SearchVector('author_name', 'link', 'author_email', 'description', 'title'),
        ).filter(search=phrase).values('author_name', 'link', 'author_email', 'description', 'title')
