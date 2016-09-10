#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

import tempfile

from PIL import Image

from .mylibs import theqrmodule
from .combine import combine



def run(WORDs, version=None, level='H', picture=None, colorized=False, contrast=1.0, brightness=1.0):
    tempdir = os.path.join(os.path.expanduser('~'), '.myqr')

    # the default version depends on WORDs and level
    # init as 0
    ver = version if version else 0
    # the default level is Q
    ecl = level if level else 'H'

    with tempfile.TemporaryDirectory() as tempdir:
        try:
            ver, qr_name = theqrmodule.get_qrcode(ver, ecl, WORDs, tempdir)
        except TypeError:
            qr_name = picture = None

        if picture and picture[-4:]=='.gif':
            print('it takes a while, please wait for minutes...')

            import imageio

            im = Image.open(picture)
            im.save(os.path.join(tempdir, '0.png'))
            while True:
                try:
                    seq = im.tell()
                    im.seek(seq + 1)
                    im.save(os.path.join(tempdir, '%s.png' %(seq+1)))
                except EOFError:
                    break

            imsname = []
            for s in range(seq+1):
                bg_name = os.path.join(tempdir, '%s.png' % s)
                imsname.append(combine(ver, qr_name, bg_name, colorized, contrast, brightness, tempdir))

            ims = [imageio.imread(pic) for pic in imsname]
            qr_name = os.path.splitext(os.path.basename(picture))[0] + '_qrcode.gif'
            imageio.mimsave(qr_name, ims)
        elif picture:
            qr_name = combine(ver, qr_name, picture, colorized, contrast, brightness, os.getcwd())
        elif qr_name:
            qr = Image.open(qr_name)
            qr_name = os.path.basename(qr_name)
            qr.resize((qr.size[0]*3, qr.size[1]*3)).save(qr_name)

        return qr_name
