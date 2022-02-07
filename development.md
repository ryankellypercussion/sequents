# Development Guide

## Installing for general, non-development use
Clone the repository and install with `pip`, optionally with the features `interactive` and `nlp`:
- Install just the package and dependencies: `pip install .`
- Install the package along with the dependencies to run a Jupyter notebook: `pip install ".[interactive]"`
- Install the package along with the packages from the NLTK book: `pip install ".[nlp]"`
- Install all of the above: `pip install ".[interactive,nlp]"`

## Installing for Development
For more information about installing packages, including virtual environments, consult the [Installing Packages Tutorial](https://packaging.python.org/en/latest/tutorials/installing-packages/) from the [Python Packaging User Guide](https://packaging.python.org/en/latest/). Here is a summary.

First, find or install a Python 3 interpreter on your computer, and open a command prompt in the root folder of this repository. Or, open the repository folder in an IDE like Visual Studio Code.

Create a virtual environment called 'venv' in the project root. My Python interpreter is linked to the name `python3`, but you should replace it with whatever command you use.
```sh
python3 -m venv venv
```

Start the virtual environment.
```sh
source venv/bin/activate
```

The virtual environment exists in this `venv` folder, and when active, it modifies your command-line such that the `python` command ends up being a (linked copy of) the `python3` interpreter on the computer, and the `pip` command similarly for `pip3`. Now, all the packages you install with the `pip` command will be installed to this `venv` folder, and the libraries available to the `python` command will be only the ones installed to this folder (and the ones included in Python). This is useful for developing and testing packages without cluttering your system!

Install the Python project package as *editable*, along with the features *interactive* and *nlp*.
```
pip install -e ".[interactive,nlp]"
```

You should now be ready to use and modify the package while in the virtual environment. Further, you should be able to use this virtual environment to run a Jupyter notebook, and have access to most of the libraries from the book, like NLTK, MatPlotLib, Numpy, and NetworkX.

You can deactivate the virtual environment whenever you want by running
```sh
deactivate
```

And to start the virtual environment again, just run
```sh
source venv/bin/activate
```

## Running Code

The package is comprised of a set of Python modules in the `./src` directory. Each of these modules (`module1` and `module2`) are just folders with empty `__init__.py` files. These modules encourage we keep code organized, as they allow multiple projects to exist side-by-side with plenty of separation of concerns.

Observe that `module2` also contains an `__main__.py` file. This file can be run by the command
```sh
python -m module2
```
Thus, `module2` serves as an executable module, just like `venv` above (`venv` is included in Python).

In contrast, the file `example.py` in `module1` is a module which can be imported into different environments, and examples of this are peppered around the code. An example would look something like this
```python
from module1 import example

example.test() # test is a function defined in src/module1/example.py.
```

It also has a block at the end, which determines if the file is the main context being run. So, the block at the end of `example.py` will not be run when the code is imported. The block will only be run if we run this command:
```sh
python -m module1.example
```

This is generally all you need to be able to write and run code. Typically, all program content is going to go into some module in the `src/` directory, but there will be some exceptions we don't need to worry about now.

## Running Tests

Another important module included with Python is the `unittest` module, which provides a way to write code which runs tests against the code in the modules. All of these tests are in the directory `./tests`. The module has a standard way to 'discover' the tests for the package by running the following command:
```sh
python -m unittest discover
```

Lots of IDEs can discover and show a list of all the tests available, as well as if they pass or fail, making them indispensable tools when computations and changes begin getting complicated.

---

## Extra files

As you're working on your code, Python introduces several artifacts that should be excluded from the Git repository. I've put several of them into the `.gitignore` file already, but what are these files for?

Briefly, the `__pycache__` folders and their files are the results of an intermediate compilation step that the interpreter does, in order to be able to load and run modules faster. They depend on your environment and are automatically regenerated when Python runs, so shouldn't be recorded in the repository.

`*.egg-info` folders store information used by your virtual environment about the package. You will probably find it in the `src` folder. It is a result of installing a local package as *editable* in our environment, and also should not be put into the repository.

As well, your own `venv` folder should not be pushed to the repository, and I've put that folder in the `.gitignore` file as well. You could name your environment plenty of other things and put it in other places if you want, just don't upload it. The main benefit of putting it in the root of the project folder is that many IDEs like Visual Studio Code will automatically detect and ask if you wish to use the virtual environment for all Python-related tasks (including Jupyter notebook kernels, tests, debugging, etc.).

A folder alongside the Jupyter notebooks called `.ipynb_checkpoints` can also be ignored. It is just auxiliary data from opening and editing notebooks.