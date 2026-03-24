from django.db import models

class BannedIp(models.Model):
    ip_address = models.CharField(max_length=15)

    def __str__(self):
        return self.ip_address
