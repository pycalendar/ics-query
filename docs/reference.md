# Command reference

## Global options

These options apply to all commands.

| Option | Env var | Description |
| ------ | ------- | ----------- |
| `--tz TEXT` | `ICS_QUERY_TZ` | Query in a specific timezone. Use `localtime` for your system timezone, `UTC` for UTC, or any IANA timezone name. |
| `-c, --component TEXT` | `ICS_QUERY_COMPONENT` | Filter by component type. Can be passed multiple times. Default: `VEVENT`, `VTODO`, `VJOURNAL`. |
| `--as-calendar` | `ICS_QUERY_AS_CALENDAR` | Wrap output in a `VCALENDAR` block with `VTIMEZONE` components. Produces a valid `.ics` file. |

## Top-level flags

| Flag | Description |
| ---- | ----------- |
| `--version` | Show the version and exit. |
| `--available-timezones` | List all available timezone names and exit. |
| `--license` | Show the license and exit. |

## jCal conversion

`ics-query` accepts RFC 5545 iCalendar input. To use RFC 7265 jCal JSON,
convert the file with [`ical2jcal`](https://pypi.org/project/ical2jcal/)
before or after running `ics-query`.

```shell
ical2jcal calendar.ics calendar.jcal
jcal2ical calendar.jcal calendar.ics
```

See the [ical2jcal documentation](https://pycalendar.github.io/ical2jcal/)
for the full command reference.

## ics-query at

```
ics-query at [OPTIONS] DATE CALENDAR [OUTPUT]
```

Returns all occurrences that overlap with the time span represented by DATE.

DATE sets both the start and end of the span. A year covers the whole year, a day covers 24 hours, a minute covers 60 seconds, and so on. Start is inclusive, end is exclusive.

Pass `-` as CALENDAR to read from stdin. Pass `-` as OUTPUT to write to stdout. OUTPUT defaults to `-`.

### DATE formats

| Format | Example | Span |
| ------ | ------- | ---- |
| `YYYY` | `2024` | whole year |
| `YYYY-MM` | `2024-08` | whole month |
| `YYYYMM` | `202408` | whole month |
| `YYYY-MM-DD` | `2024-08-12` | whole day |
| `YYYYMMDD` | `20240812` | whole day |
| `YYYY-MM-DDTHH` | `2024-08-12T17` | one hour |
| `YYYYMMDDTHH` | `20240812T17` | one hour |
| `YYYY-MM-DDTHH:MM` | `2024-08-12T17:20` | one minute |
| `YYYYMMDDTHHMM` | `202408121720` | one minute |
| `YYYY-MM-DDTHH:MM:SS` | `2024-08-12T17:20:00` | one second |
| `YYYYMMDDTHHMMSS` | `20240812172000` | one second |

Single-digit months, days, hours, minutes, and seconds are accepted (`2024-8-2T7:5`).
A space may be used instead of `T` as the date-time separator.

## ics-query between

```
ics-query between [OPTIONS] START END CALENDAR [OUTPUT]
```

Returns all occurrences that overlap with the span from START to END.
START is inclusive, END is exclusive.

START accepts the same formats as DATE in `at`. Each format resolves to the earliest moment it represents — `2024-08` resolves to `2024-08-01T00:00:00`.

END can be an absolute time (same formats as START) or a relative duration added to START.

### Duration formats

| Format | Description |
| ------ | ----------- |
| `+1d` | one day |
| `+1h` | one hour |
| `+1m` | one minute |
| `+1s` | one second |
| `+5d10h` | five days and ten hours |
| `+3h15m` | three hours and fifteen minutes |

The `+` prefix is optional. Units are lowercase only.

## ics-query first

```
ics-query first [OPTIONS] CALENDAR [OUTPUT]
```

Returns the first occurrence in each calendar file.

When multiple calendar files are passed, returns the first occurrence from each one independently — not the first overall.

## ics-query all

```
ics-query all [OPTIONS] CALENDAR [OUTPUT]
```

Returns all occurrences in a calendar.

Calendars with recurring events can produce a very large number of results. Some recurring events repeat indefinitely. Use `head` to limit output:

```shell
ics-query all calendar.ics - | head -100
```
