from time import sleep
from main.models import Image, Video, ContactAndInfo, Play, LiveVideo
from rest_framework import generics
from main.serializers import ImageSerializer, VideoSerializer, ContactSerializer, PlaySerializer, LiveVideoSerializer

# def some_view(request):
#     images = Image.objects.all()
#     images = [x.image_file.url for x in images]
#     video = [x.embedded_video for x in Video.objects.all()]
#     return render(request, 'index.html', context={'images': images, 'video': video})

from django.views.generic import TemplateView


# TODO - Not usable template view must be removed from urls
class IndexView(TemplateView):
    template_name = 'carousel.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        images = Image.objects.all()
        images = [x.image_file.url for x in images]
        context['carousel_items'] = [
            {'image': '/media/images/test_results_XU7YuY4.jpg', 'caption': 'Caption 1'},
            {'image': '/media/images/viber_image_2022-07-13_19-37-35_ASGYiup.jpg', 'caption': 'Caption 2'},
            {'image': '/media/images/test_results_XU7YuY4.jpg', 'caption': 'Caption 3'},
        ]
        return context


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

    # def get(self, request, *args, **kwargs):
    #     sleep(2)
    #     return super().get(request, *args, **kwargs)


class VideoGalleryAPIView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    # def get(self, request, *args, **kwargs):
    #     sleep(2)
    #     return super().get(request, *args, **kwargs)

class LiveVideoAPIView(generics.ListAPIView):
    queryset = LiveVideo.objects.all()
    serializer_class = LiveVideoSerializer

class PlayAPIView(generics.ListAPIView):
    queryset = Play.objects.all()
    serializer_class = PlaySerializer


class ContactAPIView(generics.ListAPIView):
    queryset = ContactAndInfo.objects.all()
    serializer_class = ContactSerializer
