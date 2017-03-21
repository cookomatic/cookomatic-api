"""Image utilities."""

from google.appengine.api import images
from google.appengine.ext import blobstore

GS_BUCKET = '/gs/project-cookomatic.appspot.com'
THUMB_SIZE = 256


def generate_image_url(filename):
    """
    Generates secure serving URL for images

    :param filename: filename of image in GCS bucket
    :return: two URLs as tuple. First is full-size image, second is thumbnail.
    """
    blob_key = blobstore.create_gs_key("%s/%s" % (GS_BUCKET, filename))
    return images.get_serving_url(blob_key, secure_url=True), \
           images.get_serving_url(blob_key, secure_url=True, size=THUMB_SIZE)
