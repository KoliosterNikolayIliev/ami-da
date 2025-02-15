from django.db import models
from twisted.plugins.twisted_reactors import default


class Play(models.Model):
    play_name = models.CharField(max_length=150, blank=False)
    play_name_bg = models.CharField(max_length=150, blank=False)
    description = models.TextField(null=True, blank=True)
    description_bg = models.TextField(null=True, blank=True)
    next_play = models.DateTimeField(verbose_name="next_play", blank=True)

    def __str__(self):
        return self.play_name


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
    embedded_video = models.TextField(blank=False)

    def get_live_stream_link(self):
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


# TODO - this date is needed in order frontend to know when to fetch when live video exists! (for future development)
class NextLiveVideo(models.Model):
    date = models.DateTimeField(blank=False)
    live_video_is_playing = models.BooleanField(default=False, blank=False)


class CharityPageData(models.Model):
    charity_tab_active = models.BooleanField(default=False)
    charity_link_name_bg = models.CharField(max_length=255, blank=False, null=False, default='Благотворителност')
    charity_link_name_en = models.CharField(max_length=255, blank=False, null=False, default='Charity')
    heading_bg = models.CharField(max_length=255, blank=True, null=True)
    heading_en = models.CharField(max_length=255, blank=True, null=True)
    main_text_bg = models.TextField(blank=True, null=True)
    main_text_en = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='images/', blank=True, null=True)
    embedded_video = models.TextField(blank=True, null=True)
    payment_heading_bg = models.CharField(max_length=255, blank=True, null=True)
    payment_heading_en = models.CharField(max_length=255, blank=True, null=True)
    payment_info_bg = models.TextField(blank=True, null=True)
    payment_info_en = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Charity page data'

