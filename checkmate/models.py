from django.db import models


class DangerType(models.Model):
    name = moders.CharField(max_length=50)
    description = models.TextField(max_length=200)



NONE = 'N'
LOW = 'L'
MEDIUM = 'M'
HIGHT = 'H'
DANGER_LEVEL = (
    (NONE, 'None'),
    (LOW, 'Low'),
    (MEDIUM, 'Medium'),
    (HIGHT, 'Hight'),
)

class Danger(models.Model):
    danger_type = models.ForeignKey(DangerType, on_delete=models.CASCADE)

    danger_level = models.CharField(
        max_length=1,
        choices=DANGER_LEVEL,
        default=NONE
    )


SITE = 'S'
INSTAGRAM_ACCOUNT = 'I_A'
YOUTUBE_CHANNEl = 'Y_C'
FACEBOOK_GROUP = 'F_G'
FACEBOOK_ACCOUNT = 'F_A'
TWITTER_ACCOUNT = 'T_A'
REDDIT_THREAD = 'R_T'

CONTENT_TYPE = (
    (SITE, 'Site'),
    (INSTAGRAM_ACCOUNT, 'Instagram Account'),
    (YOUTUBE_CHANNEl, 'Youtube Channel'),
    (FACEBOOK_GROUP, 'Facebook Group'),
    (FACEBOOK_ACCOUNT, 'Facebook Account'),
    (TWITTER_ACCOUNT, 'Twitter Account')
    (REDDIT_THREAD, 'Reddit Thread'),
)

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class Content(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    dangers = models.ManyToManyField(Danger, blank=True)

    content_type = models.CharField(
        max_length=3,
        choices=CONTENT_TYPE,
    )

    image = ImageField(upload_to=get_image_path, blank=True, null=True)

