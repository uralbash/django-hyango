# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.conf.urls.i18n import i18n_patterns

from views import GalleryList, GalleryDetail, GalleryImagesJSON

urlpatterns = patterns('',
                            url(r'^gallery/$', GalleryList.as_view(),
                                name="gallery_list"),
                            url(r'^gallery/(?P<slug>[-_\w]+)/$',
                                GalleryDetail.as_view(),
                                name="gallery_detail"),
                            url(r'^gallery/(?P<slug>\d+)/images/$',
                                GalleryImagesJSON.as_view(),
                                name='gallery_images_json'),
                            )
