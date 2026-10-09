# CS 1110 labs

This repository collects Python lab exercises and small practice programs from CS 1110. The folders are organized by lab number; the code is coursework and practice material, not a packaged application.

## Contents

- `lab1/`, `lab3/`, `lab4/`, `lab5/`: introductory programs and string or dice exercises.
- `lab6/`: string functions and debugging practice; some functions are intentionally faulty exercise material.
- `lab7/`, `lab9/`, `lab11/`, `lab12/`, `lab13/`: functions involving strings, time objects, debugging, lists, and iteration.
- `BackendOA/`: a small pretest script.

Some folders include course-provided test or exercise files. The assignment handouts and course instructions define the expected behavior; this repository does not include all assignment specifications.

The Python exercise index below is regenerated from the source files when a lab file changes on `main`. Descriptions come from module docstrings; files without docstrings are labeled as exercises or supporting scripts. The workflow preserves this README's manually written sections.

<!-- BEGIN AUTO-GENERATED LAB INDEX -->
### Python exercise index

#### `BackendOA/`

- [`pretest.py`](BackendOA/pretest.py) — Python exercise or supporting script.

#### `lab1/`

- [`hello1.py`](lab1/hello1.py) — Python exercise or supporting script.
- [`hello2.py`](lab1/hello2.py) — A window displaying Hello World.

#### `lab11/`

- [`lab11.py`](lab11/lab11.py) — A module to demonstrate errors and error debugging.

#### `lab12/`

- [`lab12.py`](lab12/lab12.py) — Python exercise or supporting script.

#### `lab13/`

- [`clamp.py`](lab13/clamp.py) — Python exercise or supporting script.
- [`devowel.py`](lab13/devowel.py) — Python exercise or supporting script.
- [`lesser_than.py`](lab13/lesser_than.py) — Python exercise or supporting script.
- [`removeall.py`](lab13/removeall.py) — Python exercise or supporting script.
- [`uniques.py`](lab13/uniques.py) — Python exercise or supporting script.

#### `lab3/`

- [`dice.py`](lab3/dice.py) — A simple die roller

#### `lab4/`

- [`dice.py`](lab4/dice.py) — A simple die roller
- [`dicefun.py`](lab4/dicefun.py) — Python exercise or supporting script.

#### `lab5/`

- [`quotes.py`](lab5/quotes.py) — The module for first_inside_quotes

#### `lab6/`

- [`europeanize.py`](lab6/europeanize.py) — Python exercise or supporting script.
- [`funcs.py`](lab6/funcs.py) — Functions for handling Strings
- [`quotes.py`](lab6/quotes.py) — The module for first_inside_quotes
- [`test.py`](lab6/test.py) — Course-provided test or exercise checks.
- [`tests.py`](lab6/tests.py) — Course-provided test or exercise checks.

#### `lab7/`

- [`extra.py`](lab7/extra.py) — Additional problem for more practice
- [`lab07.py`](lab7/lab07.py) — Module for implementing Lab 07 functions.
- [`testex.py`](lab7/testex.py) — Course-provided test or exercise checks.

#### `lab9/`

- [`clock.py`](lab9/clock.py) — Module that provides a simple Time class
- [`extras.py`](lab9/extras.py) — Additional problems for more practice
- [`lab09.py`](lab9/lab09.py) — Module for implementing Lab 09 functions.
- [`test09.py`](lab9/test09.py) — Course-provided test or exercise checks.
- [`testex.py`](lab9/testex.py) — Course-provided test or exercise checks.

<!-- END AUTO-GENERATED LAB INDEX -->
## Running a file

Use Python 3 from the repository root. For example:

```sh
python3 lab3/dice.py
python3 lab7/lab07.py
```

Some files only define functions and print nothing when run. Import or call those functions from a Python shell or the relevant course test file. The Kivy example in `lab1/hello2.py` needs Kivy installed; most other exercises use only the Python standard library. There is no shared dependency file or single test command for this collection.

## Notes

Exercises may be incomplete, retain assignment scaffolding, or contain bugs that are part of a debugging task. Review a file and its lab instructions before using it as a reference implementation. Keep course-provided test files with the exercise they belong to.
