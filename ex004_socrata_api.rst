ex004_socrata_api.py
====================

A script that replicates all examples in my blog post using Python to get data
from the Socrata API: `Socrata post`_ .

Run all the examples
--------------------

.. code:: bash

    $ python ex004_socrata_api.py

Or, 

.. code:: bash

    $ chmod u+x ex004_socrata_api.py
    $ ./ex004_socrata_api.py

Use the classes defined in the file
-----------------------------------

Start Python (or ipython if you like) in the directory containing the
:code:`ex004_socrata_api.py` file.

.. code:: bash

    $ python

Then import the file and try out a new example by getting trees 6 - 10 from an
API query


.. code:: python

    >>> import ex004_socrata_api as socapi
    >>> args = {"$order": ":id", "$limit": 5, "$offset": 5}
    >>> next_five_trees = socapi.get_trees(args)
    >>> for n, tree in enumerate(next_five_trees):
    ...     print "--Tree {}:\n {}\n".format(n+1, tree)
    ...
    >>> exit()

That's it, give it a try!

.. _Socrata post: http://chrisstrelioff.ws/sandbox/2015/02/17/using_python_to_query_data_from_socrata.html

