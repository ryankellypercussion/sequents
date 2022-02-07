# Template
I wrote this template in order to illustrate what I think are the most minimal and well-known ways to collaborate on Python code. Here, `src/module1` and `src/module2` are examples of modules we would write, and `notebooks/demo.ipynb` is an example of an interactive Python notebook that runs the code in the modules alongside prose.

Consult the [development guide](development.md) for more information about installing, running, and developing the package itself.

## TODO
- [ ] Decide whether we should be able to either use the `nltk.sem.logic` representation of FOL, or convert between this representation and whatever representation we choose to use. Consider that in the end we are attempting to replicate the `nltk.sem.logic` module while replacing the `nltk.sem.evalute` module, using some other code like Adrian's prover.
- [ ] Using NLTK sometimes requires downloading things from various places, and we might need to make sure the user has done this before running some code.
- [ ] I put the NLP-related packages in an 'extra' feature, but if we write code using them we will want to specify our code's dependencies appropriately.

## Resources
- [The NLTK Book](https://www.nltk.org/book/), updated for Python 3 and NLTK 3.
- [Python 3 Documentation](https://docs.python.org/3/index.html)
    - [The `venv` module](https://docs.python.org/3/library/venv.html)
    - [The `unittest` module](https://docs.python.org/3/library/unittest.html)
- [NumPy Website](https://numpy.org/)
- [Matplotlib Website](https://matplotlib.org/)
- [NLTK Website](https://www.nltk.org/)
    - [NLTK API Reference](https://www.nltk.org/api/nltk.html)

### Sub-Resource Constellations

#### Analyzing the logical structure of sentences
- [Chapter 9](https://www.nltk.org/book/ch09.html) concerns building feature-based grammars, which underlies the tools in chapter 10.
- [Chapter 10](https://www.nltk.org/book/ch10.html) concerns NLTK's tools to model first-order propositional logic; to build semantic representations using compositional semantics in feature-based grammars; to build discourse representation structures; and more.
- [NLTK API Reference](https://www.nltk.org/api/nltk.html)
    - [The `nltk.sem` package](https://www.nltk.org/api/nltk.sem.html) is introduced primarily in Chapter 10
        - [The `sem.logic` module](https://www.nltk.org/api/nltk.sem.logic.html) contains NLTK's FOL library
