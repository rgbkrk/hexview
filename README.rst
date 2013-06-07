hexview
=======

Hexdump++ for python, integration with IPython.

**This is currently a work in progress and is still being designed.**

.. image:: https://travis-ci.org/rgbkrk/hexview.png?branch=master
        :target: https://travis-ci.org/rgbkrk/hexview

Hexview provides ways to visualize binary data within IPython or Python and even export HTML or LaTeX.

Hexview keeps context of fields via annotators.

Example/planned usage:

.. code-block:: python

   >>> from hexview import HexView
   >>> data = open("data/requests-1.2.0.tar.gz","rb").read()
   >>> hv = HexView(data)
   0000000: 1f8b 0808 8cc9 5751 02ff 6469 7374 2f72  ......WQ..dist/r
   0000010: 6571 7565 7374 732d 312e 322e 302e 7461  equests-1.2.0.ta
   0000020: 7200 ec7d 6977 e258 9268 7fd6 af50 67cd  r..}iw.X.h...Pg.
   0000030: 3cdb 65cc bed8 eec9 9e11 2016 9b7d b371  <.e....... ..}.q
   0000040: 771f a700 0132 8bb0 0466 9933 efb7 bf88  w....2...f.3....
   0000050: bb68 4360 c8cc aa99 7e53 9cac 3248 778d  .hC`....~S..2Hw.
   0000060: 1b11 3722 6edc 0843 7d5f a9e6 d2bc 8904  ..7"n..C}_......
   ...
   00535f0: 3feb 67fd ac9f f5b3 7ed6 cfbf e5f3 77ce  ?.g.....~.....w.
   0053600: 1de6 0a00 780f 00                        ....x..

   >>> hv.dump(width=12)
   0000000: 1f8b 0808 8cc9 5751 02ff 6469  ......WQ..di
   000000c: 7374 2f72 6571 7565 7374 732d  st/requests-
   0000018: 312e 322e 302e 7461 7200 ec7d  1.2.0.tar..}
   0000024: 6977 e258 9268 7fd6 af50 67cd  iw.X.h...Pg.
   0000030: 3cdb 65cc bed8 eec9 9e11 2016  <.e....... .
   000003c: 9b7d b371 771f a700 0132 8bb0  .}.qw....2..
   0000048: 0466 9933 efb7 bf88 bb68 4360  .f.3.....hC`
   ...
   00535f8: 7ed6 cfbf e5f3 77ce 1de6 0a00  ~.....w.....
   0053604: 780f 00                        x..

   >>> hv[13:19]
   000000d: 742f 7265 7175                           t/requ

   >>> hv.set_width(2)
   >>> hv[13:19]
   000000d: 742f  t/
   000000f: 7265  re
   0000011: 7175  qu

   >>> hv.annotate("gzip-magic", xrange(0,3))
   >>> hv.html(total_bytes=5,show_offsets=False,show_printables=False)
   '<pre><span class="gzip-magic">1f8b</span> 0808 8c</pre>'
   >>> hv.css(total_bytes=5,show_offsets=False,show_printables=False)
   'span.gzip-magic {
      color: #442200;
   }'


Installation
------------

To install hexview, for now use

.. code-block:: bash

   $ python setup.py install

(adding this to PyPI is planned after I write up more tests)





.. image:: https://d2weczhvl823v0.cloudfront.net/rgbkrk/hexview/trend.png
   :alt: Bitdeli badge
   :target: https://bitdeli.com/free

