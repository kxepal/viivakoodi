# -*- coding: utf-8 -*-
"""Module: barcode.upc

:Provided barcodes: UPC-A
"""

from __future__ import unicode_literals

from barcode.ean import EuropeanArticleNumber13

__docformat__ = 'restructuredtext en'


class UniversalProductCodeA(EuropeanArticleNumber13):
    """Initializes new UPC-A barcode. Can be rendered as EAN-13 by passing
    `True` to the `make_ean` argument.

    :parameters:
        upc : String
            The upc number as string.
        writer : barcode.writer Instance
            The writer to render the barcode (default: SVGWriter).
        make_ean : Boolean
            Render barcode as EAN-13 with leading 0 (default: False).
    """

    name = 'UPC-A'

    digits = 11

    def __init__(self, upc, writer=None, make_ean=False):
        if make_ean:
            UniversalProductCodeA.digits = 12
            upc = '0' + upc
        self.upc = upc
        super(UniversalProductCodeA, self).__init__(upc, writer)

    def __unicode__(self):
        return self.upc

    __str__ = __unicode__


UPCA = UniversalProductCodeA
