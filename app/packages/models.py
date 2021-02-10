from django.db import models


class Package(models.Model):
    title = models.CharField(max_length=70)
    link = models.URLField()
    guid = models.CharField(max_length=70, unique=True)
    description = models.TextField()
    author_name = models.CharField(max_length=320)
    author_email = models.EmailField()

    def __init__(self, *args, **kwargs):
        super(Package, self).__init__(*args, **kwargs)

    def populate_from_rss_raw_package(self, rss_raw_package):
        """
        Fills model fields based on raw dict from rss feed.

        :param rss_raw_package: raw data from rss feed entry
        :return: void
        """
        self.title = rss_raw_package['title']
        self.link = rss_raw_package['link']
        self.guid = rss_raw_package['id']
        self.description = rss_raw_package['summary']
        if hasattr(rss_raw_package, 'author_detail'):
            if hasattr(rss_raw_package['author_detail'], 'email'):
                self.author_email = rss_raw_package['author_detail']['email']
            if hasattr(rss_raw_package['author_detail'], 'name'):
                self.author_name = rss_raw_package['author_detail']['name']
        elif hasattr(rss_raw_package, 'author'):
            self.author_name = rss_raw_package['author']