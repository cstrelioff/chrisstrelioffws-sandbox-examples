bayes_ex01.py
=============

A script that replicates all examples in my blog post on inferring
probabilities-- see `bayes post`_ for more information.

Run all the examples
--------------------

.. code:: bash

    $ python bayes_ex01.py

Or, 

.. code:: bash

    $ chmod u+x bayes_ex01.py
    $ ./bayes_ex01.py

Use the classes defined in the file
---------------------------------

Start Python (or ipython if you like) in the directory containing the
:code:`bayes_ex01.py` file.

.. code:: bash

    $ python

Then import the file and try out a new example by

* creating new data
* specifying a prior
* creating a posterior
* plotting the results of inference

.. code:: python

    Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
    [GCC 4.8.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import numpy as np
    >>> from bayes_ex01 import prior, posterior
    >>> data = np.random.choice([0,1], 500, p=[0.01, 0.99])
    >>> pri = prior(np.arange(0.0, 1.01, 0.01))
    >>> post = posterior(data, pri)
    >>> post.plot()

That's it!

.. _bayes post: http://chrisstrelioff.ws/sandbox/2014/10/24/inferring_probabilities_a_second_example_of_bayesian_calculations.html

