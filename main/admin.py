import re

from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import Image, Play, Video, ContactAndInfo, LiveVideo, CharityPageData


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_filter = ('play',)

    def image_tag(self, obj):
        return format_html('<img src="{}" width="224"/>'.format(obj.image_file.url))

    image_tag.short_description = 'Image'
    list_display = ('image_tag', 'description', 'description_bg', 'play', 'carousel', 'poster', 'date_created')


@admin.register(Play)
class PlayAdmin(admin.ModelAdmin):
    pass


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_filter = ('play',)

    def video_tag(self, obj):
        pattern = r'width="\d+" height="\d+"'
        return mark_safe(re.sub(pattern, 'width="224" height="126"', obj.embedded_video))

    video_tag.short_description = 'Video'

    list_display = ('id', 'video_tag', 'description', 'description_bg', 'play', 'play_main_video', 'date_created')


@admin.register(LiveVideo)
class LiveVideoAdmin(admin.ModelAdmin):
    def video_tag(self, obj):
        pattern = r'width="\d+" height="\d+"'
        return mark_safe(re.sub(pattern, 'width="672" height="378"', obj.embedded_video))

    video_tag.short_description = 'Live video'

    list_display = ('description', 'description_bg', 'video_tag')

    def has_add_permission(self, request):
        if LiveVideo.objects.count() > 0:
            return False
        return True


@admin.register(ContactAndInfo)
class ContactAndInfoAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if ContactAndInfo.objects.count() > 0:
            return False
        return True

@admin.register(CharityPageData)
class CharityPageDataAdmin(admin.ModelAdmin):

    def video_tag(self, obj):
        pattern = r'width="\d+" height="\d+"'
        return mark_safe(re.sub(pattern, 'width="672" height="378"', obj.embedded_video))

    video_tag.short_description = 'Charity video'

    def image_tag(self, obj):
        return format_html('<img src="{}" width="224"/>'.format(obj.picture.url))

    image_tag.short_description = 'image'

    list_display = ('image_tag', 'video_tag')

    def has_add_permission(self, request):
        if CharityPageData.objects.count() > 0:
            return False
        return True