PEXNET (an abbreviation for "Participatory EconomiCS NETwork") is a website that 
provides the framework for a participatory economy.

The website so far tracks goods (and their indicative prices), tasks (and their 
desirability and empowerment ratings), an individual's own goods and tasks,
and the ability to add in new goods and tasks.

Before running for the first time, run:

python ./load.py

Do NOT run load.py again unless you want to destroy the database.

To activate the website, run: 

python ./pexnet.py

Technical Requirements:
Python >=2.7.4
Bottle >=0.12.4
sqlite3 for Python

TODO: Make sql injection safe throughout.
TODO: Make PEXNET logo
TODO: Make templates DRY
TODO: Add Twitter Bootstrap
TODO: Align search bar to the right
TODO: Make credits page
TODO: Align "Add my Tasks/Add my Goods" button to the right
TODO: Strip entries in my_tasks dictionary that have value of zero.
TODO: Present goods and tasks (rather than IDs) in my goods/tasks pages.
TODO: Allow ability to update/contribute to indicative prices. 
