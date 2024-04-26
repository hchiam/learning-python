# Learning Python

Miscellaneous practice code in Python and things I've used.

Just one of the things I'm learning. https://github.com/hchiam/learning

You can create share-able online live demos with [trinket.io](https://trinket.io) (similar to [CodePen](https://codepen.io/pen/) for JS/HTML/CSS).

## Notes on Python built-ins worth knowing

https://github.com/hchiam/learning-python/blob/master/python-built-ins-worth-learning.md

## Run code linter

To run python linter `pylint` on a file (for example [`pylint_example.py`](https://github.com/hchiam/learning-python/blob/master/pylint_example.py)), run this in the CLI:

```bash
pylint pylint_example.py
```

Or even better, you can auto-run that command every time you save a file in the folder. To do that, do `pip3 install rerun` and then run this in the CLI:

```bash
rerun "pylint pylint_example.py; python3 pylint_example.py"
```

This works just like [`nodemon` for JS/Node.js](https://github.com/hchiam/learning-js#bonus).

## Type checking

I use `pyright` to do static type checking in VSCode.

You can see an example of (gradual) type annotations [here](https://github.com/hchiam/learning-python/blob/master/leetcode/climbing-stairs-problem.py).

## Maintainability Index (MI score)

The MI combines lines of code, cyclomatic complexity, and the Halstead volume metric (i.e. number of variables, operations, decision paths, and lines of code). After you `pip install radon`, you can get the MI score of your code:

```bash
radon mi your_code.py -s
```

Similar to how I use [`plato`](https://github.com/hchiam/learning-js/blob/master/README.md#get-code-maintainability-index-mi-score) for JavaScript code.

More tools for things like refactoring code (`rope`) and tracking project code complexity (`wily`): <https://realpython.com/python-refactoring/>

## [`Segmentation fault: 11` when running `matplotlib`](https://stackoverflow.com/a/64841196)

```sh
pip uninstall matplotlib
pip install matplotlib
```

## More random notes

pretty print `pprint`: https://www.geeksforgeeks.org/pprint-data-pretty-printer-python/

`all([True, False])`: https://www.w3schools.com/python/ref_func_all.asp

`any([True, False])`: https://www.w3schools.com/python/ref_func_any.asp

`from __future__ import newkeywordthing`: https://stackoverflow.com/questions/7075082/what-is-future-in-python-used-for-and-how-when-to-use-it-and-how-it-works

`import inspect`: https://stackoverflow.com/questions/3711184/how-to-use-inspect-to-get-the-callers-info-from-callee-in-python

`print(wikipedia.summary('web query'))`: https://pypi.org/project/wikipedia/ (see example for other params & methods)

`brew install python` to upgrade python to the latest version https://stackoverflow.com/questions/74214615/how-to-update-python-version-in-terminal
- `brew link --overwrite python@3.12`
- `alias py='python3.12'` in .bash_profile (`alias bas='source ~/.bash_profile'`) so `py --version` outputs something like `Python 3.12.2`

`python3 -m http.server 8000` to quickly set up a basic local server that serves index.html at http://localhost:8000/
- or `python -m SimpleHTTPServer 8000` for older python versions
- consider bash script: `alias srv='python3 -m http.server 8000'`

## Other Repos

- https://github.com/hchiam/hchiam-example-pypi-project
- https://github.com/hchiam/webScraper
- Maching Learning: https://github.com/hchiam/machineLearning
- NLP with spaCy and textacy: https://github.com/hchiam/nlp_spacy_textacy
- One of my experimental programming languages: https://github.com/hchiam/please (for coding by voice)
- Flask: https://github.com/hchiam/learning-flask
- A genetic algorithm: https://github.com/hchiam/cogLang-geneticAlgo
- https://github.com/hchiam/cognateLanguage
- Code and notes based on Udacity course AI for Robotics: https://github.com/hchiam/ai_for_robotics
- Cirq for quantum computer circuits: https://github.com/hchiam/learning-cirq
- https://github.com/hchiam/autotest
- https://github.com/hchiam/audioMonitorQt
- LZW compression algorithm https://github.com/hchiam/learning-lzw
