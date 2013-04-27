#!/usr/bin/env python
# -*- coding: utf-8 -*-

from binascii import hexlify

hexable = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ "

def printables(s):
    get_printable = lambda x: x if x in hexable else "."
    return "".join(map(get_printable, s))

class HexView(object):
    '''

    Display hex dumps of raw binary data

    >>> data = open("data/requests-1.2.0.tar.gz","rb").read()
    >>> hv = HexView(data)
    >>> print(hv)
    00000000: 1f8b 0808 8cc9 5751 02ff 6469 7374 2f72  ......WQ..dist/r
    00000010: 6571 7565 7374 732d 312e 322e 302e 7461  equests-1.2.0.ta
    00000020: 7200 ec7d 6977 e258 9268 7fd6 af50 67cd  r..}iw.X.h...Pg.
    00000030: 3cdb 65cc bed8 eec9 9e11 2016 9b7d b371  <.e....... ..}.q
    00000040: 771f a700 0132 8bb0 0466 9933 efb7 bf88  w....2...f.3....
    00000050: bb68 4360 c8cc aa99 7e53 9cac 3248 778d  .hC`....~S..2Hw.
    00000060: 1b11 3722 6edc 0843 7d5f a9e6 d2bc 8904  ..7"n..C}_......
    ...
    00053600: 1de6 0a00 780f 00                        ....x..

    >>> print(hv.dump(width=12))
    00000000: 1f8b 0808 8cc9 5751 02ff 6469  ......WQ..di
    0000000c: 7374 2f72 6571 7565 7374 732d  st/requests-
    00000018: 312e 322e 302e 7461 7200 ec7d  1.2.0.tar..}
    00000024: 6977 e258 9268 7fd6 af50 67cd  iw.X.h...Pg.
    00000030: 3cdb 65cc bed8 eec9 9e11 2016  <.e....... .
    0000003c: 9b7d b371 771f a700 0132 8bb0  .}.qw....2..
    00000048: 0466 9933 efb7 bf88 bb68 4360  .f.3.....hC`
    ...
    00053604: 780f 00                        x..

    '''

    def __init__(self, data, width=16, split=2, limit=7, text_dump=True):
        # The original data
        # TODO: Try out other iterables, unicode, mmap
        self.bindata = data
        # Width of the hex dump (in bytes)
        self.width = width
        # When to break bytes up by space
        if(split == 0):
            split = width
        self.split = split
        # How many rows of bytes to print
        self.limit = limit
        # Whether to print ASCII text on the right
        # Figure out other encodings
        self.text_dump = text_dump

    def __str__(self):
        return self.dump(self.width,self.limit)

    def __repr__(self):
        return str(self)

    def _repr_html_(self):
        '''
        HTML Representation for IPython

        TODO: Use templating, add in annotation so we can "syntax highlight"
        the hexdumps.
        '''

        return "<pre>" + self.dump(self.width,self.limit) + "</pre>"


    def build_row(self,row,width):
        '''
        Builds an individual row for hexdumping

        >>> hv = HexView("A"*23)
        >>> print(hv)
        00000000: 4141 4141 4141 4141 4141 4141 4141 4141  AAAAAAAAAAAAAAAA
        00000010: 4141 4141 4141 41                        AAAAAAA

        >>> hv = HexView("A"*32, width=8, split=4)
        >>> print(hv)
        00000000: 41414141 41414141  AAAAAAAA
        00000008: 41414141 41414141  AAAAAAAA
        00000010: 41414141 41414141  AAAAAAAA
        00000018: 41414141 41414141  AAAAAAAA

        >>> hv = HexView("A"*16, width=16, split=0)
        >>> print(hv)
        00000000: 41414141414141414141414141414141  AAAAAAAAAAAAAAAA

        '''
        if(row >= len(self.bindata)):
                raise IndexError("Data slice out of range")

        build_str = "%08x: " % row
        for col in range(width):
            index = row + col
            if(index < len(self.bindata)):
                build_str += hexlify(self.bindata[index])
                # Group bytes on `split`
                build_str += " " if col % self.split == self.split-1 else ""

        if(self.text_dump):
            build_str += " "
            row_length = min(row+width, len(self.bindata))


            if(row_length == len(self.bindata)):
                hex_space =  (len(build_str) - 10) # 10 characters for the
                                                   # offsets
                total_spacing = (
                                 width*2 + # Two nibbles in a byte
                                 width/self.split # Spacing between groups
                                )

                build_str += " "*(total_spacing - hex_space + 1)

            build_str += printables(self.bindata[row:row_length])

        return build_str

    def dump(self, width=16,limit=7):
        '''
        Builds out a pure hexdump (no styling)

        >>> data = open("data/requests-1.2.0.tar.gz","rb").read()
        >>> hv = HexView(data)
        >>> print(hv.dump())
        00000000: 1f8b 0808 8cc9 5751 02ff 6469 7374 2f72  ......WQ..dist/r
        00000010: 6571 7565 7374 732d 312e 322e 302e 7461  equests-1.2.0.ta
        00000020: 7200 ec7d 6977 e258 9268 7fd6 af50 67cd  r..}iw.X.h...Pg.
        00000030: 3cdb 65cc bed8 eec9 9e11 2016 9b7d b371  <.e....... ..}.q
        00000040: 771f a700 0132 8bb0 0466 9933 efb7 bf88  w....2...f.3....
        00000050: bb68 4360 c8cc aa99 7e53 9cac 3248 778d  .hC`....~S..2Hw.
        00000060: 1b11 3722 6edc 0843 7d5f a9e6 d2bc 8904  ..7"n..C}_......
        ...
        00053600: 1de6 0a00 780f 00                        ....x..

        >>> print(hv.dump(width=12))
        00000000: 1f8b 0808 8cc9 5751 02ff 6469  ......WQ..di
        0000000c: 7374 2f72 6571 7565 7374 732d  st/requests-
        00000018: 312e 322e 302e 7461 7200 ec7d  1.2.0.tar..}
        00000024: 6977 e258 9268 7fd6 af50 67cd  iw.X.h...Pg.
        00000030: 3cdb 65cc bed8 eec9 9e11 2016  <.e....... .
        0000003c: 9b7d b371 771f a700 0132 8bb0  .}.qw....2..
        00000048: 0466 9933 efb7 bf88 bb68 4360  .f.3.....hC`
        ...
        00053604: 780f 00                        x..


        >>> hv = HexView("A"*13)
        >>> print(hv.dump(width=1, limit=2))
        00000000: 41  A
        00000001: 41  A

        '''
        max_display_bytes = min(len(self.bindata),limit*width)

        if(max_display_bytes != len(self.bindata)):
            print_excess = True
        else:
            print_excess = False

        rows = []

        for row in range(0,max_display_bytes,width):
            build_str = self.build_row(row,width)
            rows.append(build_str)

        if(print_excess):
            rows.append("...")

            num_rows = len(self.bindata)/width
            row = num_rows*width

            build_str = self.build_row(row,width)
            rows.append(build_str)

        return ("\n".join(rows))






