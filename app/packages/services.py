import feedparser
from django.conf import settings


class PackageParserService:
    """
    Service class responsive for parsing python packages rss feed.
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
