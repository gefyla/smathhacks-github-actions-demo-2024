<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Development Guide](#development-guide)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


# Development Guide

1. Create an issue
2. Checkout a new branch off main
3. Make your changes
4. Run pre-commit and pytest locally

```bash
# assuming you've installed python3
# create virtual environment
python3 -m venv ./venv
source ./venv/bin/activate
# install pre-commit
pip install pre-commit
# run precommit
pre-commit run --all-files

Check Yaml...............................................................Passed
Fix End of Files.........................................................Passed
Trim Trailing Whitespace.................................................Passed

# install pytest and coverage
pip install pytest coverage
# run pytest
coverage run -m pytest -v -s
================================================= test session starts =================================================
platform darwin -- Python 3.10.4, pytest-7.1.2, pluggy-1.0.0 -- /Library/Frameworks/Python.framework/Versions/3.10/bin/python3.10
cachedir: .pytest_cache
rootdir: /Users/geoffreyfylak/Desktop/smathhacks/smathhacks-github-actions-demo-2024
plugins: dash-2.8.1, cov-4.0.0
collected 3 items

tests/test_utils.py::test_addition PASSED
tests/test_utils.py::test_subtraction PASSED
tests/test_utils.py::test_equivalence PASSED
```
5. Open a PR
