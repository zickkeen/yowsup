from yowsup.common.tools import ImageTools
import os


class ImageAttributes(object):
    def __init__(self, width, height, caption=None, jpeg_thumbnail=None):
        self.width = width
        self.height = height
        self.caption = caption
        self.jpeg_thumbnail = jpeg_thumbnail

    @staticmethod
    def from_filepath(filepath, dimensions=None, caption=None, jpeg_thumbnail=None):
        assert os.path.exists(filepath)
        if not jpeg_thumbnail:
            jpeg_thumbnail = ImageTools.generatePreviewFromImage(filepath)
        dimensions = dimensions or ImageTools.getImageDimensions(filepath)
        width, height = dimensions if dimensions else (None, None)
        assert width and height, "Could not determine image dimensions, install pillow or pass dimensions"

        return ImageAttributes(width, height, caption, jpeg_thumbnail)