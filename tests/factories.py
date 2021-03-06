from __future__ import absolute_import, unicode_literals

import factory
from wagtail.wagtailimages.tests.utils import get_test_image_file
from wagtail.wagtailimages.models import Image


class ImageFactory(factory.DjangoModelFactory):
    title = factory.sequence(lambda x: 'image-{0}'.format([x]))
    file = factory.LazyAttribute(lambda x: get_test_image_file())

    class Meta:
        model = Image


class MockedUrlImageFile(object):
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        self.image_url = kwargs.pop('image_url')

    @property
    def url(self):
        return self.image_url
