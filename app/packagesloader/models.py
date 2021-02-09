from django.db import models


class Package(models.Model):
    title = models.CharField(max_length=70)
    link = models.URLField()
    guid = models.CharField(max_length=70)
    description = models.TextField()
    author_name = models.CharField(max_length=320)
    author_email = models.EmailField()
    pub_date = models.DateTimeField()

    def __init__(self, *args, **kwargs):
        super(Package, self).__init__(*args, **kwargs)

        rss_dict = kwargs.pop('rss_dict', None)
        if rss_dict:
            self.title = rss_dict['title']
            self.link = rss_dict['link']
            self.guid = rss_dict['id']
            self.description = rss_dict['summary']
            self.author_name = rss_dict['author']
            self.author_email = rss_dict['author']
            self.pub_date = rss_dict['title']
