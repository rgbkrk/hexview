# hexview

Hexdump++

Hexview provides ways to visualize binary data within IPython or Python and even export HTML or LaTeX.

Hexview keeps context of fields via annotators.


```python

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

>>> hv.annotate("gzip-magic", xrange(0,3))



```