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
        4  62  53  64


  * Add labels to columns:

        :::python
        >>> df.columns = ['a', 'b', 'c']
        >>> df
            a   b   c
        0  35  66  14
        1  30   3  13
        2  17  69  97
        3  99  27   0
        4  62  53  64


  * Drop all but `a` and `c` columns:

        :::python
        >>> df[['a', 'c']]
            a   c
        0  35  14
        1  30  13
        2  17  97
        3  99   0
        4  62  64


  * Get a NumPy array of index values:

        :::python
        >>> df.index.values
        array([0, 1, 2, 3, 4])


Other resources:

  * [Pandas official documentation
  ](http://pandas.pydata.org/pandas-docs/stable/)
  * [Stack Overflow's pandas questions
  ](https://stackoverflow.com/questions/tagged/pandas)
  * [Becky Sweger's snippets
  ](https://gist.github.com/bsweger/e5817488d161f37dcbd2)
