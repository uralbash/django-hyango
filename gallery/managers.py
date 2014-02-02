# -*- coding: utf-8 -*-
from django.core.exceptions import SuspiciousOperation
from django.db import models

from filebrowser.base import FileListing, FileObject


class GalleryImageFBManager(models.Manager):

    fl_sorting_by = 'date'
    fl_sorting_order = 'desc'
    fl_filetypes = ['Image']

    def _filter_filelisting(self, item):
        return item.filetype in self.fl_filetypes

    def get_filelisting(self, path):
        fb_path = FileObject(path)
        try:
            is_folder = fb_path.is_folder
        except SuspiciousOperation:
            is_folder = False
        if not is_folder:
            return []
        fl = FileListing(
            path, filter_func=self._filter_filelisting,
            sorting_by=self.fl_sorting_by,
            sorting_order=self.fl_sorting_order
        ).files_listing_filtered()
        return fl
