Prompts
=======

When you create a package, you are prompted to enter these values.

Templated Values
----------------

The following appear in various parts of your generated project.

full_name
    Your full name.

email
    Your email address.

vcs_username
    Your VCS username.

project_name
    The name of your new Python package project. This is used in documentation, so spaces and any characters are fine here.

project_slug
    The namespace of your Python package. This should be Python import-friendly. Typically, it is the slugified version of project_name. Note: your PyPi project will use project_slug, so change those in the README afterwards.

project_short_description
    A 1-sentence description of what your Python package does.

pypi_username
    Your Python Package Index account username.

version
    The starting version number of the package.

Options
-------

The following package configuration options set up different features for your project.

use_poetry
    Whether to manage packages with `poetry <https://python-poetry.org/docs/>`_

use_pytest
    Whether to use `pytest <https://docs.pytest.org/en/latest/>`_

command_line_interface
    Whether to create a console script using Click. Console script entry point will match the project_slug. Options: ['Click', 'Argparse', 'No command-line interface']

create_author_file
    Whether to create an authors file

project_license
    Choose a `license <https://choosealicense.com/>`_. Options: [1. MIT, 2. BSD-3-Clause, 3. ISC, 4. Apache-2.0, 5. GPL-3.0-or-later, 6. Proprietary]
