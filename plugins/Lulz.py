import logging
from cStringIO import StringIO
from plugins.plugin import Plugin
from plugins.Inject import Inject
from PIL import Image, ImageFile

class Lulz(Inject, Plugin):
    name       = "Lulz"
    optname    = "lulz"
    desc       = 'Does some silly stuff'
    alt_implements = {"handleResponse": "imageResponse", "handleHeader": "imageHeader"}
    version    = "0.2"
    has_opts   = True
    req_root   = False

    def initialize(self, options):
        self.options = options
        self.rickroll = options.rickroll
        self.upsidedown = options.upsidedownternet

        globals()['Image'] = Image
        globals()['ImageFile'] = ImageFile

        if options.rickroll:
            self.alt_implements = {}
            Inject.initialize(self, options)
            Inject.html_payload = '<iframe width="100%" height="100%" src="//www.youtube.com/embed/dQw4w9WgXcQ?autoplay=1" frameborder="0" allowfullscreen></iframe>'

    def imageHeader(self, request, key, value):
        '''Kill the image skipping that's in place for speed reasons'''
        if self.upsidedown:
            if request.isImageRequest:
                request.isImageRequest = False
                request.isImage = True
                request.imageType = value.split("/")[1].upper()

    def imageResponse(self, request, data):

        if self.upsidedown:
            data = flip180(request, data)

        return {'request': request, 'data': data}

    def flip180(self, request, data):
        try:
            isImage = getattr(request, 'isImage')
        except AttributeError:
            isImage = False

        if isImage:
            try:
                image_type = request.imageType
                #For some reason more images get parsed using the parser
                #rather than a file...PIL still needs some work I guess
                p = ImageFile.Parser()
                p.feed(data)
                im = p.close()
                im = im.transpose(Image.ROTATE_180)
                output = StringIO()
                im.save(output, format=image_type)
                data = output.getvalue()
                output.close()
                logging.info("%s Flipped image" % request.client.getClientIP())
                return data
            except Exception as e:
                logging.info("%s Error: %s" % (request.client.getClientIP(), e))

    def add_options(self, options):
        group = options.add_mutually_exclusive_group(required=False)
        group.add_argument("--upsidedownternet", action="store_true", default=False, help="Flips images 180 degrees")
        group.add_argument("--rickroll", action="store_true", default=False, help="Overwrites the body of pages with a full screen Rickroll.")