from django.db import models


# TODO - cards with play with the ingo and small thumbnail to watch the video the same like videos and images but more text
# TODO Live should be only one video and the button should be visible only whe there is live (maybe using web socket)
class Play(models.Model):
    name = models.CharField(max_length=150, blank=False)
    name_bg = models.CharField(max_length=150, blank=False)
    description = models.TextField(null=True, blank=True)
    description_bg = models.TextField(null=True, blank=True)
    next_play = models.DateTimeField(verbose_name="next_play", blank=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    description = models.CharField(max_length=200, blank=True)
    description_bg = models.CharField(max_length=200, blank=True)
    play = models.ForeignKey(to=Play, on_delete=models.SET_NULL, blank=False, null=True)
    carousel = models.BooleanField(blank=False, default=False)
    image_file = models.ImageField(upload_to='images/')
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    poster = models.BooleanField(blank=False, default=False)

    def save(self, *args, **kwargs):
        if self.poster:
            Image.objects.filter(play=self.play).exclude(pk=self.pk).update(poster=False)
        super(Image, self).save(*args, **kwargs)


class Video(models.Model):
    description = models.TextField(null=True, blank=True)
    description_bg = models.TextField(null=True, blank=True)
    play = models.ForeignKey(to=Play, on_delete=models.CASCADE, blank=False, null=False)
    embedded_video = models.TextField(blank=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    play_main_video = models.BooleanField(blank=False, default=False)

    def save(self, *args, **kwargs):
        if self.play_main_video:
            Video.objects.exclude(pk=self.pk).update(play_main_video=False)
        super(Video, self).save(*args, **kwargs)


class LiveVideo(models.Model):
    description = models.TextField(null=True, blank=True)
    description_bg = models.TextField(null=True, blank=True)
    play = models.ForeignKey(to=Play, on_delete=models.SET_NULL, blank=True, null=True)
    active = models.BooleanField(default=False)
    embedded_video = models.TextField(blank=False)

    def get_live_stream_link(self):
        # Implement your logic here to get the live stream link based on the model data
        return self.embedded_video


class ContactAndInfo(models.Model):
    phone = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    address_bg = models.TextField(blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    info_bg = models.TextField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    about_bg = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Contacts and information'
        verbose_name_plural = 'Contacts and information'

    def __str__(self):
        return 'Contact information'

# class SocialNetwork(models.Model):
#     name = models.CharField(max_length=150, default='Unknown')
#     contact = models.ForeignKey(to=ContactAndInfo, on_delete=models.CASCADE)
#     url = models.URLField()
#     icon_class = models.CharField(max_length=150, blank=True, default=None, null=True)
#
#     def __str__(self):
#         return self.name
