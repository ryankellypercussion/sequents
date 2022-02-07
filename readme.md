# Template
I wrote this template in order to illustrate what I think are the most minimal and well-known ways to collaborate on Python code.

## Getting Started
For more information about installing packages, including virtual environments, consult the [Installing Packages Tutorial](https://packaging.python.org/en/latest/tutorials/installing-packages/) from the [Python Packaging User Guide](https://packaging.python.org/en/latest/). Here is a summary.

Create a virtual environment called 'venv' in the project root.
```sh
python3 -m venv venv
```

Start the virtual environment.
```sh
source venv/bin/activate
```

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



## Development

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

---

## Resources
 
- [The NLTK Book](https://www.nltk.org/book/), updated for Python 3 and NLTK 3.
- [Python 3 Documentation](https://docs.python.org/3/index.html)
    - [The `venv` module](https://docs.python.org/3/library/venv.html)
    - [The `unittest` module](https://docs.python.org/3/library/unittest.html)
- [NumPy Website](https://numpy.org/)
- [Matplotlib Website](https://matplotlib.org/)