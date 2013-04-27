#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse, sys
import binascii
import math
from binascii import hexlify as hexy
from binascii import unhexlify as unhexy
import string

'''

Beautifile takes in a file and a set of offset ranges with names to produce
beautified HTML.

Let's take gzip as an example format. Looking at the table from
http://www.onicos.com/staff/iz/formats/gzip.html:

    Byte order: Little-endian

    Offset   Length   Contents
      0      2 bytes  magic header  0x1f, 0x8b
      2      1 byte   compression method
                         0: store (copied)
                         1: compress
                         2: pack
                         3: lzh
                         4..7: reserved
                         8: deflate
      3      1 byte   flags
                         bit 0 set: file probably ascii text
                         bit 1 set: continuation of multi-part gzip file, part number present
                         bit 2 set: extra field present
                         bit 3 set: original file name present
                         bit 4 set: file comment present
                         bit 5 set: file is encrypted, encryption header present
                         bit 6,7:   reserved
      4      4 bytes  file modification time in Unix format
      8      1 byte   extra flags (depend on compression method)
      9      1 byte   OS type

We see what the structure is for gzip. Let's see if we can create a way to show
others how this format is laid out.

>>> a = Annotator()
>>> a.annotate(category="magic", start=0x0, end=0x2)
>>> a.annotate(category="compression_method", start=0x2)
>>> a.annotate(category="flags", start=0x3)
>>> a.annotate(category="file_modification_time", start=0x4, end=(0x4+4))
>>> a.annotate(category="extra_flags", start=0x8)
>>> a.annotate(category="OS_type", start=0x8)

'''

class Annotator:
    '''
    This class sets up how bytes are annotated.

    >>> a = Annotator()
    >>> a.annotate(category="magic", start=0x0, end=0x2)
    >>> a.annotate(category="compression_method", start=0x2)
    >>> a.feedback(0x1,0x3)
    [('magic', 1,2), ('compression_method',2,3)]

    '''

    def __init__(self):
        self.LUT = dict()
        pass

    def annotate(self, category, start, end=None):
        '''
        Set the category for a range of indices.

        >>> a = Annotator()
        >>> a.annotate(category="magic", start=0x0, end=0x2)
        >>> a.annotate(category="compression_method", start=0x2)

        '''

        if(end is None):
            end=start+1
        for ii in xrange(start,end):
            self.LUT[ii] = category

    def feedback(self,start,end=None):
        '''
        Get class information about a range of indices.
        If end is not specified, it is assumed to be the single byte at start.

        The list that is returned contains tuples of this format:

        (classType, startClass, endClass)

        >>> a = Annotator()
        >>> a.annotate(category="magic", start=0x0, end=0x2)
        >>> a.annotate(category="compression_method", start=0x2)
        >>> a.feedback(0x1,0x3)
        [('magic',1,2), ('compression_method',2,3)]

        '''
        ll = []
        curr = self.LUT.get(start, "unknown")
        st = start
        if(end==None):
            end = start+1

