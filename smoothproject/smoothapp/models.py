from django.db import models
from django.utils import timezone


def user_directory_path(instance, filename):
    return 'submissions/{0}'.format(filename)


class ReviewSubmission(models.Model):
    description = models.CharField(max_length=250, null=True, blank=True)
    image = models.ImageField(upload_to=user_directory_path, null=True, blank=False)
    date_sent = models.DateTimeField(default=timezone.now, null=False, blank=True)

    def __str__(self):
        return str(self.pk) + " image"
