# Installation

## pip

```shell
pip install ics-query
```

To verify:

```shell
ics-query --version
```

To upgrade:

```shell
pip install --upgrade ics-query
```

## pipx

If you want `ics-query` as a standalone command without touching your system Python, use [pipx].
It installs the tool in an isolated environment and puts `ics-query` on your PATH automatically.

```shell
pipx install ics-query
```

If you do not have pipx yet:

```shell
pip install pipx
pipx ensurepath
```

To upgrade:

```shell
pipx upgrade ics-query
```

## Homebrew (macOS)

```shell
brew install niccokunzmann/tap/ics-query
```

## Version pinning

Version numbers follow `a.b.c`:

- `c` increments for each bug fix.
- `b` increments when new features are added.
- `a` increments when the interface or major assumptions change.

If you use `ics-query` in scripts, pin to the same `a` and let `b` and `c` float.

[PyPI]: https://pypi.org/project/ics-query/
[pipx]: https://pipx.pypa.io
