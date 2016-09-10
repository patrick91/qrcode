# -*- coding: utf-8 -*-

# To be used just when PyInstaller is not installed

from MyQR.__main__ import run

def cli():
    import argparse
    argparser = argparse.ArgumentParser()
    argparser.add_argument('WORDs', help = 'The words to produce you QR-code picture, like a URL or a sentence. Please read the README file for the supported characters.')
    argparser.add_argument('-v', '--version', type = int, choices = range(1,41), help = 'The version means the length of a side of the QR-Code picture. From little size to large is 1 to 40.')
    argparser.add_argument('-l', '--level', choices = list('LMQH'), help = 'Use this argument to choose an Error-Correction-Level: L(Low), M(Medium) or Q(Quartile), H(High). Otherwise, just use the default one: H')
    argparser.add_argument('-p', '--picture', help = 'the picture  e.g. example_pic.jpg')
    argparser.add_argument('-c', '--colorized', action = 'store_true', help = "Produce a colorized QR-Code with your picture. Just works when there is a correct '-p' or '--picture'.")
    argparser.add_argument('-con', '--contrast', type = float, help = 'A floating point value controlling the enhancement of contrast. Factor 1.0 always returns a copy of the original image, lower factors mean less color (brightness, contrast, etc), and higher values more. There are no restrictions on this value. Default: 1.0')
    argparser.add_argument('-bri', '--brightness', type = float, help = 'A floating point value controlling the enhancement of brightness. Factor 1.0 always returns a copy of the original image, lower factors mean less color (brightness, contrast, etc), and higher values more. There are no restrictions on this value. Default: 1.0')
    args = argparser.parse_args()

    run(
        args.version,
        args.level,
        args.WORDs,
        args.picture,
        args.colorized,
        args.contrast,
        args.brightness
    )

if __name__ == '__main__':
    cli()