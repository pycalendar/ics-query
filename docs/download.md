# Download

Pre-built binaries are available on the [Releases] page.
No Python installation required.

## Windows

Download `ics-query.exe` from the [Releases] page and run it directly:

```shell
ics-query.exe --version
```

## Linux (x86_64)

Download `ics-query-linux-x86_64` from the [Releases] page.
Make it executable and run it:

```shell
chmod +x ics-query-linux-x86_64
./ics-query-linux-x86_64 --version
```

To use it without the path prefix, move it somewhere on your PATH:

```shell
mv ics-query-linux-x86_64 ~/.local/bin/ics-query
ics-query --version
```

## macOS

macOS binaries are not provided.
Use [Homebrew or pip](install.md) instead.

## Verifying the download

After downloading, check that the version matches the release you downloaded:

```shell
ics-query --version
```

[Releases]: https://github.com/pycalendar/ics-query/releases
