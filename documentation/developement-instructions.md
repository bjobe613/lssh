# Development Instructions

Author(s): Isak Almquist

Creation date: ?/8-2020

Last change: 31/10-2020

This document will contain instructions for developing the lssh webapp. It will contain instructions on how to set up the development environment.

## Programs and languages
The back-end of the webapp is developed with [Python 3.8](https://www.python.org/) using the [Flask](https://flask.palletsprojects.com/en/1.1.x/) framework.

The front-end is developed with HTML, CSS and JavaScript using a few frameworks.

Version control is done with [git](https://git-scm.com/) in this [git repo](https://gitlab.liu.se/lssh/webapp).

## Frameworks and libraries
Under this heading the different frameworks and libraries that are used throughout the webapp.

### Python frameworks and libraries
#### [Flask](https://flask.palletsprojects.com/en/1.1.x/)
#### [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/)
#### [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
#### [quill-delta](https://github.com/forgeworks/quill-delta-python)

### Front end
The front end is written using a combination of jquery and bootstrap

### Back end

### First time instructions
Make sure that python >3.8 is installed and that it can be run from some command line. Test this using `python --version` or `python3 --version`. The output should be 
```
PS C:\Users\isaka\webapp> python --version
Python 3.8.2
```
The version number can differ, but it should be greater than 3.8. If you get no output or an error message, make sure that python is properly installed.

Create a virtual environment, a venv, by following these [instructions](https://docs.python.org/3/library/venv.html). Then run it using the same instructions. You know that you have succeeeded when there is a `(venv)` before your command line prompt.
```
(venv) PS C:\Users\isaka\webapp> 
```

To install requirements navigate to the root folder, probably 'webapp'. Then run `pip install -r requirements.txt`. This will install all needed frameworks.

### Running instructions
To run the server, make sure that you are inside of the venv. This is done differently depending on your platform, follow these [instructions](https://docs.python.org/3/library/venv.html).

To run the server: `python run.py`

To reset the development database: `python resetDB.py`