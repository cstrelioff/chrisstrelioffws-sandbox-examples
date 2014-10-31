bayes_ex01.py
=============

A script that replicates all examples in my blog post on inferring
probabilities:

You can

Run all the examples
--------------------

.. code:: bash

    $ python baye_ex01.py

Or, 

.. code:: bash

    $ chmod u+x bayes_ex01.py
    $ ./bayes_ex01.py

Use the class defined in the file
---------------------------------

Start Python (or ipython if you like) in the directory containing the
:code:`baeys_ex01.py` file:

.. node:: bash

    $ python

Try out a new example:

.. code:: python

    Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
    [GCC 4.8.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from bayes_ex01 import *
    >>> dir()
    ['__builtins__', '__doc__', '__name__', '__package__', 'division',
    'likelihood', 'np', 'plt', 'posterior', 'print_function', 'prior']
    >>> data = np.random.choice([0,1], 500, p=[0.01, 0.99])
    >>> prior = prior(np.arange(0.0, 1.01, 0.01))
    >>> post = posterior(data, prior)
    >>> post.plot()
    >>> exit()

That's it!

