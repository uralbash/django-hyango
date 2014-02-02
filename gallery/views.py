# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.list import ListView

from common.pagination import SlicePaginatorMixin
from common.mixins import JSONResponseMixin, SEOMixin

from models import Gallery, GalleryImage


class GalleryList(SlicePaginatorMixin, ListView):

    context_object_name = 'galleries'
    model = Gallery
    queryset = model.objects.all()
    template_name = 'gallery/gallery_list.html'


class GalleryMixin(object):
    context_object_name = 'images'
    model = GalleryImage
    pk_url_kwarg = 'slug'
    template_name = 'gallery/gallery_detail.html'

    def dispatch(self, request, *args, **kwargs):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        self.object = get_object_or_404(Gallery, pk=pk)
        return super(GalleryMixin, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        if self.object.directory:
            return self.model.fb_objects.get_filelisting(self.object.directory)
        return self.object.images.all()


class GalleryDetail(SEOMixin, SlicePaginatorMixin, GalleryMixin, ListView):

    """
    Подробная информации о галереи.
    """
    paginate_by = 20

    def get_context_data(self, **kwargs):
        kwargs['gallery'] = self.object
        context = super(GalleryDetail, self).get_context_data(**kwargs)
        return context


class GalleryImagesJSON(JSONResponseMixin, GalleryMixin, ListView):

    def dispatch(self, request, *args, **kwargs):
        if not request.is_ajax():
            return redirect('gallery_detail', *args, **kwargs)
        return super(GalleryImagesJSON, self).dispatch(request, *args, **kwargs)

    def render_to_response(self, context, **response_kwargs):
        images_ctx = []
        images = context.get(self.context_object_name, [])
        for image in images:
            images_ctx__itm = {
                'id': 'img-%s' % self.object.pk,
            }
            image_fo = image
            if not self.object.directory:
                image_fo = image_fo.image
                images_ctx__itm['description'] = image.description
                images_ctx__itm['id'] += '-%s' % image.pk
            else:
                images_ctx__itm['id'] += '-%s' % image_fo.filename
            try:
                img = image_fo.version_generate('gallery_image').url
            except:
                img = image_fo.url
            images_ctx__itm['img'] = img
            try:
                thumb = image_fo.version_generate('b_gallery_slider_thumb').url
            except:
                thumb = image_fo.url
            images_ctx__itm['thumb'] = thumb
            images_ctx.append(images_ctx__itm)
        context_json = {
            'images': images_ctx,
        }
        return self.json_to_response(context_json, **response_kwargs)
