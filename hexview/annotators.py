#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

The plan for this module is to create a declarative way of describing fields of
bytes.

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

>>> gzip_annotator = Annotator()
>>> gzip_annotator.annotate(category="magic", start=0x0, end=0x2)
>>> gzip_annotator.annotate(category="compression_method", start=0x2)
>>> gzip_annotator.annotate(category="flags", start=0x3)
>>> gzip_annotator.annotate(category="file_modification_time", start=0x4, end=(0x4+4))
>>> gzip_annotator.annotate(category="extra_flags", start=0x8)
>>> gzip_annotator.annotate(category="OS_type", start=0x8)
>>> gzip_annotator.feedback(0x3,0x9)
[('flags', (3, 4)), ('file_modification_time', (4,8)), ('extra_flags', (8,9))]

'''

class Annotator(object):
    pass
