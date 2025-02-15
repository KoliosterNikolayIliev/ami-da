from time import sleep
from main.models import (Image,
                         Video,
                         ContactAndInfo,
                         Play,
                         LiveVideo,
                         CharityPageData)

from rest_framework import generics
from main.serializers import (ImageSerializer,
                              VideoSerializer,
                              ContactSerializer,
                              PlaySerializer,
                              LiveVideoSerializer,
                              CharityPageDataSerializer)


class CarouselAPIView(generics.ListAPIView):
    queryset = Image.objects.filter(carousel=True)
    serializer_class = ImageSerializer

    # just for testing:
    def get(self, request, *args, **kwargs):
        sleep(1)
        return super().get(request, *args, **kwargs)


class ImageGalleryAPIView(generics.ListAPIView):
    queryset = Image.objects.filter(poster=False)
    serializer_class = ImageSerializer


class VideoGalleryAPIView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class LiveVideoAPIView(generics.ListAPIView):
    queryset = LiveVideo.objects.all()
    serializer_class = LiveVideoSerializer


class PlayAPIView(generics.ListAPIView):
    queryset = Play.objects.all()
    serializer_class = PlaySerializer


class ContactAPIView(generics.ListAPIView):
    queryset = ContactAndInfo.objects.all()
    serializer_class = ContactSerializer

class CharityAPIView(generics.ListAPIView):
    queryset = CharityPageData.objects.all()
    serializer_class = CharityPageDataSerializer