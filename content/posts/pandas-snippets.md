date: 2015-11-05 12:00:00
title: Pandas snippets
category: English
tags: Pandas, Computer programming, date, development, Python, Data, Analytics, NumPy

All snippets below are initialized with the following Python code:

    :::python
    >>> import numpy as np
    >>> import pandas as pd


  * Create a 5 rows and 3 columns frame with random integers between 0 and 99:

        :::python
        >>> df = pd.DataFrame(np.random.randint(100, size=(5, 3)))
        >>> df
            0   1   2
        0  35  66  14
        1  30   3  13
        2  17  69  97
        3  99  27   0
        4  30  53  64


  * Add labels to columns:

        :::python
        >>> df.columns = ['a', 'b', 'c']
        >>> df
            a   b   c
        0  35  66  14
        1  30   3  13
        2  17  69  97
        3  99  27   0
        4  30  53  64


  * Drop all but `a` and `c` columns:

        :::python
        >>> df[['a', 'c']]
            a   c
        0  35  14
        1  30  13
        2  17  97
        3  99   0
        4  30  64


  * Get a NumPy array of index values:

        :::python
        >>> df.index.values
        array([0, 1, 2, 3, 4])


  * Make column `a` the index:

        :::python
        >>> df.set_index('a', inplace=True)
        >>> df
            b   c
        a
        35  66  14
        30   3  13
        17  69  97
        99  27   0
        30  53  64


  * Sort along the index:

        :::python
        >>> df.sort(inplace=True)
        >>> df
            b   c
        a
        17  69  97
        30  53  64
        30   3  13
        35  66  14
        99  27   0


  * Deduplicate `c` data points at the same `a` index, with the highest `c` value taking precedence:

        :::python
        >>> df['c'].reset_index().groupby('a').max()
            c
        a
        17  97
        30  64
        35  14
        99   0


  * Transform a timeline of [`arrow`](http://crsmithdev.com/arrow/) objects to Pandas' internal Timestamp index:
  
        :::python
        >>> df = pd.DataFrame({'int_ts': pd.Series(np.random.randint(9999999999, size=5))})
        >>> df
               int_ts
        0  4324228164
        1  9618753903
        2  8393343044
        3  7226161665
        4  2309375336
        >>> import arrow
        >>> df['dt_arrow'] = df.int_ts.map(arrow.get)
        >>> df
               int_ts                   dt_arrow
        0  4324228164  2107-01-11T22:29:24+00:00
        1  9618753903  2274-10-22T04:05:03+00:00
        2  8393343044  2235-12-23T04:10:44+00:00
        3  7226161665  2198-12-27T03:07:45+00:00
        4  2309375336  2043-03-07T21:08:56+00:00
        >>> df['dt_index'] = pd.to_datetime(df['dt_arrow'].apply(attrgetter('datetime')), utc=True)
        >>> df
               int_ts                   dt_arrow                   dt_index
        0  4324228164  2107-01-11T22:29:24+00:00  2107-01-11 22:29:24+00:00
        1  9618753903  2274-10-22T04:05:03+00:00  2274-10-22 04:05:03+00:00
        2  8393343044  2235-12-23T04:10:44+00:00  2235-12-23 04:10:44+00:00
        3  7226161665  2198-12-27T03:07:45+00:00  2198-12-27 03:07:45+00:00
        4  2309375336  2043-03-07T21:08:56+00:00  2043-03-07 21:08:56+00:00
 

Other resources:

  * [Pandas official documentation
  ](http://pandas.pydata.org/pandas-docs/stable/)
  * [Stack Overflow's pandas questions
  ](https://stackoverflow.com/questions/tagged/pandas)
  * [Becky Sweger's snippets
  ](https://gist.github.com/bsweger/e5817488d161f37dcbd2)
