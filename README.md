# CS 1110 labs

This repository collects Python lab exercises and small practice programs from CS 1110. The folders are organized by lab number; the code is coursework and practice material, not a packaged application.

## Contents

- `lab1/`, `lab3/`, `lab4/`, `lab5/`: introductory programs and string or dice exercises.
- `lab6/`: string functions and debugging practice; some functions are intentionally faulty exercise material.
- `lab7/`, `lab9/`, `lab11/`, `lab12/`, `lab13/`: functions involving strings, time objects, debugging, lists, and iteration.
- `BackendOA/`: a small pretest script.

Some folders include course-provided test or exercise files. The assignment handouts and course instructions define the expected behavior; this repository does not include all assignment specifications.

## Running a file

Use Python 3 from the repository root. For example:

```sh
python3 lab3/dice.py
python3 lab7/lab07.py
```

Some files only define functions and print nothing when run. Import or call those functions from a Python shell or the relevant course test file. The Kivy example in `lab1/hello2.py` needs Kivy installed; most other exercises use only the Python standard library. There is no shared dependency file or single test command for this collection.

## Notes

Exercises may be incomplete, retain assignment scaffolding, or contain bugs that are part of a debugging task. Review a file and its lab instructions before using it as a reference implementation. Keep course-provided test files with the exercise they belong to.
