import uuid

from django.db import models


class DangerType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name


class Danger(models.Model):
    danger_type = models.ForeignKey(DangerType, on_delete=models.CASCADE)

    NONE = 'N'
    LOW = 'L'
    MEDIUM = 'M'
    HIGHT = 'H'

    DANGER_LEVEL_CHOICES = (
    (NONE, 'None'),
    (LOW, 'Low'),
    (MEDIUM, 'Medium'),
    (HIGHT, 'Hight'),
    )

    danger_level = models.CharField(
        max_length=1,
        choices=DANGER_LEVEL_CHOICES,
        default=NONE
    )

    def __str__(self):
        return '{0}: {1}'.format(self.danger_type, self.danger_level)


def get_image_path(instance, filename): # instance is None before create!
    from os import path
    file_ext = path.splitext(filename)[1]
    return path.join(str(instance.id), 
                        'avatar' + file_ext )

class Content(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    dangers = models.ManyToManyField(Danger, blank=True)


    SITE = 'S'
    INSTAGRAM_ACCOUNT = 'I_A'
    YOUTUBE_CHANNEl = 'Y_C'
    FACEBOOK_GROUP = 'F_G'
    FACEBOOK_ACCOUNT = 'F_A'
    TWITTER_ACCOUNT = 'T_A'
    REDDIT_THREAD = 'R_T'

    CONTENT_TYPE_CHOICES = (
        (SITE, 'Site'),
        (INSTAGRAM_ACCOUNT, 'Instagram Account'),
        (YOUTUBE_CHANNEl, 'Youtube Channel'),
        (FACEBOOK_GROUP, 'Facebook Group'),
        (FACEBOOK_ACCOUNT, 'Facebook Account'),
        (TWITTER_ACCOUNT, 'Twitter Account'),
        (REDDIT_THREAD, 'Reddit Thread'),
    )

    content_type = models.CharField(
        max_length=3,
        choices=CONTENT_TYPE_CHOICES,
    )

    image = models.ImageField(
        default='photos/default',
        upload_to=get_image_path, 
        blank=True, null=True
        )

    def __str__(self):
        return '{0} [{1}]'.format(self.name, self.content_type)
