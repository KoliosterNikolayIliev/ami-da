from rest_framework import serializers

from main.mixins import SwapIdForOrderId
from main.models import (Image,
                         Video,
                         ContactAndInfo,
                         Play,
                         LiveVideo,
                         CharityPageData)


class ImageSerializer(SwapIdForOrderId, serializers.ModelSerializer):
    image_field_url = serializers.SerializerMethodField()
    play_name = serializers.SerializerMethodField()
    play_name_bg = serializers.SerializerMethodField()
    id = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ('id', 'image_field_url', 'description', 'description_bg', 'play_name', 'play_name_bg')

    def get_image_field_url(self, obj):
        return obj.image_file.url

    def get_play_name(self, obj):
        return obj.play.play_name

    def get_play_name_bg(self, obj):
        return obj.play.play_name_bg


class VideoSerializer(SwapIdForOrderId, serializers.ModelSerializer):
    play_name = serializers.SerializerMethodField()
    play_name_bg = serializers.SerializerMethodField()
    id = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = ('id', 'embedded_video', 'description', 'description_bg', 'play_name', 'play_name_bg')

    def get_play_name(self, obj):
        return obj.play.play_name

    def get_play_name_bg(self, obj):
        return obj.play.play_name_bg


class PlaySerializer(SwapIdForOrderId, serializers.ModelSerializer):
    poster_url = serializers.SerializerMethodField()
    id = serializers.SerializerMethodField()

    class Meta:
        model = Play
        fields = (
            'id', 'play_name', 'play_name_bg', 'description', 'description_bg', 'next_play', 'poster_url')  # poster_url

    def get_poster_url(self, obj):
        image = obj.image_set.filter(poster=True)
        if len(image) > 0:
            return image[0].image_file.url
        return 'no_image'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactAndInfo
        fields = ('id', 'phone', 'address', 'address_bg', 'info', 'info_bg', 'about', 'about_bg',)


class LiveVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveVideo
        fields = ('embedded_video', 'description', 'description_bg')


class CharityPageDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharityPageData
        fields = "__all__"
