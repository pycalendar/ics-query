# Changelog

We automatically release versions that only update dependencies.
If the version you installed does not show up here, only the dependencies have been updated.

- v0.5.13

  - Move documentation from `README.md` into the documentation website. See [Issue 87](https://github.com/pycalendar/ics-query/issues/87).

- v0.5.12

  - Expand documentation with command reference, glossary, changelog, and timezone pages. Extract changelog into `CHANGELOG.md`. See [Issue 36](https://github.com/pycalendar/ics-query/issues/36).

- v0.5.11

  - Add documentation website at [ics-query.readthedocs.io](https://ics-query.readthedocs.io). See [Issue 36](https://github.com/pycalendar/ics-query/issues/36).

- v0.5.8

  - Name Linux binary by platform and architecture (e.g. `ics-query-linux-x86_64`). See [Issue 70](https://github.com/pycalendar/ics-query/issues/70).

- v0.5.0

  - Remove Python 3.9 support.

- v0.4.54

  - Test and support Python 3.13 and 3.14. See [Issue 9](https://github.com/niccokunzmann/ics-query/issues/9).

- v0.4.36

  - Test and document `VALARM`. See [Issue 16](https://github.com/niccokunzmann/ics-query/issues/16).

- v0.4.33

  - Add `--as-calendar` parameter.

- v0.4.32

  - Update dependencies.
  - Include recurrence ID in events to identify the occurrence in a series.
  - Update help message in command line.

- v0.4.1

  - Automatic release with patch level version number increased.
  - Increase patch version instead of minor version for automatic releases.

- v0.3.4

  - Update dependencies.
  - Start automatic release of dependencies increasing the version number.

- v0.3.3b

  - Update dependencies.

- v0.3.2b

  - Fix `--tz localtime` using `localtime` as timezone name instead of the local timezone name.
  - Fix tests on Windows.
  - Add Windows .exe build artifact.

- v0.3.1b

  - Add `--license` option.

- v0.3.0b

  - Add `--tz` timezone parameter.
  - Add `ics-query all` to get all occurrences.

- v0.2.1a

  - Add `--component` to filter component types VEVENT, VJOURNAL and VTODO.

- v0.2.0a

  - Add `ics-query first <calendar> <output>` for earliest occurrences.
  - Add `ics-query between <span_start> <span_stop> <calendar> <output>` to query time ranges.

- v0.1.1a

  - Add `--version`.
  - Add `ics-query at <date> <calendar> <output>`.
  - Add support for multiple calendars in one input.

- v0.1.0a

  - Update Python version compatibility.
  - Add development documentation.

- v0.0.1a

  - First version.
