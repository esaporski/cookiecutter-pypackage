.. highlight:: shell

============
Installation
============


Stable release
--------------

To install {{ cookiecutter.project_name }}, run this command in your terminal:

.. code-block:: console

    $ pip install {{ cookiecutter.project_slug }}

This is the preferred method to install {{ cookiecutter.project_name }}, as it will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


From sources
------------

The sources for {{ cookiecutter.project_name }} can be downloaded from the `Git repo`_.

You can either clone the repository:

.. code-block:: console

    $ git clone git://{{ cookiecutter.vcs.lower() }}.{{ 'org' if cookiecutter.vcs == 'BitBucket' or cookiecutter.vcs == 'Codeberg' else 'com' }}/{{ cookiecutter.vcs_username }}/{{ cookiecutter.project_slug }}

Or download the `tarball`_:

.. code-block:: console

    $ curl -OJL https://{{ cookiecutter.vcs.lower() }}.{{ 'org' if cookiecutter.vcs == 'BitBucket' or cookiecutter.vcs == 'Codeberg' else 'com' }}/{{ cookiecutter.vcs_username }}/{{ cookiecutter.project_slug }}/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install


.. _Git repo: https://{{ cookiecutter.vcs.lower() }}.{{ 'org' if cookiecutter.vcs == 'BitBucket' or cookiecutter.vcs == 'Codeberg' else 'com' }}/{{ cookiecutter.vcs_username }}/{{ cookiecutter.project_slug }}
.. _tarball: https://{{ cookiecutter.vcs.lower() }}.{{ 'org' if cookiecutter.vcs == 'BitBucket' or cookiecutter.vcs == 'Codeberg' else 'com' }}/{{ cookiecutter.vcs_username }}/{{ cookiecutter.project_slug }}/tarball/master
