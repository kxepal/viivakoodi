# -*- coding: utf-8 -*-
"""
viivakoodi
==========

This package provides a simple way to create standard barcodes.
It needs no external packages to be installed, the barcodes are
created as SVG objects. If PIL (Python Imaging Library) is
installed, the barcodes can also be rendered as images (all
formats supported by PIL).
"""

__project__ = 'viivakoodi'
__author__ = 'Thorsten Weimann, Alexander Shorin'
__copyright__ = '2010-2013, Thorsten Weimann; 2014, Alexander Shorin'
__author_email__ = 'kxepal@gmail.com'
__description__ = ('Create standard barcodes with Python. No external '
                   'modules needed (optional PIL support included).')
__version__ = '0.8.0'
__release__ = '{version}'.format(version=__version__)
__license__ = 'MIT'
__url__ = 'https://github.com/kxepal/viivakoodi'
__classifiers__ = [
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Multimedia :: Graphics',
]


from barcode.errors import BarcodeNotFoundError
from barcode.codex import Code39, PZN, Code128
from barcode.ean import EAN8, EAN13, JAN
from barcode.isxn import ISBN10, ISBN13, ISSN
from barcode.upc import UPCA

try:
    _strbase = basestring  # lint:ok
except NameError:
    _strbase = str


__BARCODE_MAP = dict(
    ean8=EAN8,
    ean13=EAN13,
    ean=EAN13,
    gtin=EAN13,
    jan=JAN,
    upc=UPCA,
    upca=UPCA,
    isbn=ISBN13,
    isbn13=ISBN13,
    gs1=ISBN13,
    isbn10=ISBN10,
    issn=ISSN,
    code39=Code39,
    pzn=PZN,
    code128=Code128,
)

PROVIDED_BARCODES = list(__BARCODE_MAP.keys())
PROVIDED_BARCODES.sort()


def get(name, code=None, writer=None):
    try:
        barcode = __BARCODE_MAP[name.lower()]
    except KeyError:
        raise BarcodeNotFoundError('The barcode {0!r} you requested is not '
                                   'known.'.format(name))
    if code is not None:
        return barcode(code, writer)
    else:
        return barcode


def get_class(name):
    return get_barcode(name)


def generate(name, code, writer=None, output=None, writer_options=None):
    options = writer_options or {}
    barcode = get_barcode(name, code, writer)
    if isinstance(output, _strbase):
        fullname = barcode.save(output, options)
        return fullname
    else:
        barcode.write(output, options)


get_barcode = get
get_barcode_class = get_class
