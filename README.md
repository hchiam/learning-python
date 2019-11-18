# Learning Python

Miscellaneous practice code in Python and things I've used. 

Just one of the things I'm learning. https://github.com/hchiam/learning

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

More tools for things like refactoring code (`rope`) and tracking project code complexity (`wily`): <https://realpython.com/python-refactoring/>

## Older Repos

https://github.com/hchiam/webScraper

https://github.com/hchiam/autotest

https://github.com/hchiam/audioMonitorQt
