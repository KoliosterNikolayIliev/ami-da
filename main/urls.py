from django.urls import path

from main.views import (
                        CarouselAPIView,
                        ImageGalleryAPIView,
                        VideoGalleryAPIView,
                        ContactAPIView,
                        PlayAPIView,
                        LiveVideoAPIView,
                        CharityAPIView,
                        )

app_name = 'main'
urlpatterns = [
    path('api/carousel', CarouselAPIView.as_view()),
    path('api/image_gallery', ImageGalleryAPIView.as_view()),
    path('api/video_gallery', VideoGalleryAPIView.as_view()),
    path('api/plays', PlayAPIView.as_view()),
    path('api/live-video', LiveVideoAPIView.as_view()),
    path('api/contact', ContactAPIView.as_view()),
    path('api/charity', CharityAPIView.as_view()),
]
