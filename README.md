#  Automated API testing for https://jsonplaceholder.typicode.com/
This project automates testing for common REST operations.  Python 3.5+ is required.

## Howto install python dependencies for this test suite
### With conda:

```
# conda env create -f python_3_13_environment.yml
# conda activate py313
```

### With pip:
`# pip install -f requirements.txt`

## Howto run the tests
`# pytest`

## Howto create the docker container based on Ubuntu, Python 3.13, and MiniConda.
Warning: the built image is 1.7GB
```
# docker build -t api-tester .
# docker run --rm api-tester
```

## Howto generate documentation
```
# cd docs
# make html
```

## Howto view the documentation
Auto generated code documentation can be view in [docs/_build/index.html](docs/_build/html/index.html)

## Howto look at the test report
A test report from the last pytest run can be found at [reports/report.html](reports/report.html)

## Project layout
Business logic for the common REST actions are in [actions/user_actions.py](actions/user_actions.py)
The actual tests for Create, Update, and Delete type operations on the /users routes are in [tests/test_users.py](tests/test_users.py)
The logger utility configuration is in [utils/logger.py](utils/logger.py)
The dataclass representation of a Users's properties is in [models/models.py](models/models.py)

## TODO
1. Create instances of data classes using dicts to deserialize for known tests.
2. Incorporate redis for a large DB cache to test performance.