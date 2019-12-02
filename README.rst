===============
learn_nlp_again
===============


.. image:: https://img.shields.io/pypi/v/lna.svg
	:target: https://pypi.python.org/pypi/lna

.. image:: https://img.shields.io/travis/zacbi/lna.svg
	:target: https://travis-ci.org/zacbi/lna

.. image:: https://readthedocs.org/projects/lna/badge/?version=latest
	:target: https://lna.readthedocs.io/en/latest/?badge=latest
	:alt: Documentation Status




Learn NLP from scratch again
----------------------------

..
 After learning some basic concepts and knowledge about NLP, using tools like Pytorch, AllenNLP, Jieba tokenizer, following course like DeepLearning and CS224n, writting networks, reading papers about SOTA/classic theory, applying model on real world tasks, I still can't have an overall insigt in NLP. I have to admit that I didn't get professional training and systematic education about NLP(although I major in SE).    

Here is why I started this project: **learn NLP from scratch again**. I choose `Speech and language process`_ as my entry point, and try to write solutions and implement some algorithms/models of this book. I hope I can stick to this project and update frequently. 

.. _`Speech and language process`: https://web.stanford.edu/~jurafsky/slp3/

* Free software: MIT license
* Documentation: https://lna.readthedocs.io.

Usage
--------

.. codeblock::shell
	:linenos:

    git clone git@github.com:ZacBi/learn_NLP_again.git
	cd ./learn_NLP_again
	pip install -r ./requirements_dev.txt
	pip install -e ./ --no-binary :all:

pytest:

.. codeblock::python
	:linenos:

	pytest ./tests/


Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
