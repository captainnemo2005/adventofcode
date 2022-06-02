# adventofcode
In this directory, we will go through the detail process of making a repo  and manage the dependency using poetry. To begin the project,
we can initiate the poetry dependency manager by:

``
poetry new adventofcode
``

Then, we can automate the process of adding new dependency into pyproject.toml (this is the config file for poetry) by:

``
poetry add pendulum
``

Lastly, you can format your code by installing black extension.

``
pip install black
``