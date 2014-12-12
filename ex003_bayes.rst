ex003_bayes.py
=============

A script that replicates all examples in my blog post on inferring
probabilities using a Beta prior-- see `bayes post`_ for more information.

Run all the examples
--------------------

.. code:: bash

    $ python ex003_bayes.py

Or, 

.. code:: bash

    $ chmod u+x ex003_bayes.py
    $ ./ex003_bayes.py

Use the classes defined in the file
---------------------------------

Start Python (or ipython if you like) in the directory containing the
:code:`ex003_bayes.py` file.

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
    >>> from ex003_bayes import prior, posterior
    >>> data = np.random.choice([0,1], 500, p=[0.01, 0.99])
    >>> pri = prior(1,1)
    >>> post = posterior(data, pri)
    >>> post.plot()

That's it!

.. _bayes post: http://chrisstrelioff.ws/sandbox/2014/12/11/inferring_probabilities_with_a_beta_prior_a_third_example_of_bayesian_calculations.html

