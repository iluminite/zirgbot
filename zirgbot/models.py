from django.db import models

CHANNELS = (("1", "#oms"),)

class Log(models.Model):
    user = models.CharField(max_length=20)
    msg = models.TextField()
    channel = models.CharField(max_length=1, choices=CHANNELS)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"%s %s" % (self.pub_date, self.msg[:20])
