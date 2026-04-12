# Maintenance

## Development setup

Clone the repo and install the dependencies:

```shell
git clone https://github.com/pycalendar/ics-query.git
cd ics-query
pip install -e .[test]
```

To set up the pre-commit hooks:

```shell
pip install pre-commit
pre-commit install
```

## Running the tests

The project uses `tox` to run tests across all supported Python versions.

```shell
pip install tox
```

Run the full test suite:

```shell
tox
```

Run tests on a specific Python version:

```shell
tox -e py311
```

Run only the linter:

```shell
tox -e ruff
```

Build and test the executable:

```shell
tox -e exe
```

Build the documentation:

```shell
tox -e docs
```

## How the tests work

Tests use two patterns.

**Unit tests** are standard pytest files for the date and time parsing functions in
`ics_query/tests/test_parse_date.py` and `ics_query/tests/test_parse_timedelta.py`.

**IO tests** are file-based integration tests in `ics_query/tests/runs/`.
The filename encodes the CLI command to run. The file content is the expected stdout output.
Test calendars live in `ics_query/tests/runs/calendars/`.

To add a new integration test, create a `.run` file with the expected output.
The filename is the command, for example:

```
at 2019-03-04 one-event.ics -.run
```

## Adding a test calendar

If you have a calendar file that produces incorrect output, add it to
`ics_query/tests/runs/calendars/` and write a `.run` file for it.
[Open an issue](https://github.com/pycalendar/ics-query/issues) first if you want
to discuss the expected behaviour.

## Code style

We use `ruff` for formatting and linting.
Run this to format and fix automatically:

```shell
tox -e ruff
```

## Releasing a new version

Renovate updates dependencies automatically on `main`.
Each commit to `main` is automatically published with an increased patch version.

To release a new minor or major version:

1. Edit the changelog section in `README.md`.
2. Create a commit and push it.
3. Wait for [GitHub Actions](https://github.com/pycalendar/ics-query/actions) to finish.
4. Create a tag and push it:

    ```shell
    git tag v0.2.0
    git push origin v0.2.0
    ```

5. Notify the issues about their release.

## Adding a new Python version

When a new Python version is released, update these files:

- `tox.ini` — add the version to `envlist`
- `pyproject.toml` — add a `Programming Language :: Python :: X.Y` classifier
- `.github/workflows/tests.yml` — add the version to both the `run-tests` and `test-version` matrices
- `README.md` — add a changelog entry
