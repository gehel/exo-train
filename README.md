# exo-train
Exercise suited for a code kata

This is heavily inspired (meaning shamelessly stolen) by an exercise from
[Carlo Bottiglieri](https://github.com/inverno).

## Goal
Given a string representation of a train, print an ASCII-art representation of
this train. The tests are provided, you need to write the implementation.

* **H**: locomotive `<HHHH` or `HHHH>` (depending on which side of the train it is)
* **P**: passenger car `|OOOO|`
* **R**: restaurant car `|hThT|`
* **C**: cargo car `|____|` (when empty) `|^^^^|` (when full)

Cars are attached together by `::`.

## Setup

* Ensure that `virtualenv` is available in your system.
* In the root of the checkout run:
```
virtualenv .venv
source .venv/bin/activate
pip install tox
```

## Running the tests

The flake8 code linter and the tests with code coverage are configured to run on both Python 2.7 and Python 3.4.
To run all of them simply run:

```
tox
```

If in your system one of the two version of Python is not available you can run single `tox` environments.
To list of the environments available run
```
$ tox -l
py27-flake8
py3-flake8
py27-tests
py3-tests
```

To run a specific one:
```
$ tox -e py27-flake8
```
