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

## Other Repos

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
