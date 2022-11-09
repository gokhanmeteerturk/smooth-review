from django.db import models
from django.utils import timezone


def user_directory_path(instance, filename):
    allowed_extensions = ['jpg', 'JPG', 'png', 'PNG', 'jpeg', 'JPEG']
    image_extension = filename.split(".")[-1]

    if image_extension in allowed_extensions:
        return 'submissions/submission.' + image_extension

    return 'submissions/submission.jpg'


class ReviewSubmission(models.Model):

    description = models.CharField(max_length=250,
                                   null=True,
                                   blank=True)

    screenshot_app = models.ImageField(upload_to=user_directory_path,
                                       null=True,
                                       blank=False)

    screenshot_review = models.ImageField(upload_to=user_directory_path,
                                          null=True,
                                          blank=False)

    date_sent = models.DateTimeField(default=timezone.now,
                                     null=False,
                                     blank=True)

    def __str__(self):
        return "image " + str(self.pk)


class WaitListRecord(models.Model):
    email = models.EmailField(null=False,
                              blank=False,
                              unique=True)
    date_sent = models.DateTimeField(default=timezone.now,
                                     null=False,
                                     blank=True)

    def __str__(self):
        return self.email
