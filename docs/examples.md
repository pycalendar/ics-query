# Examples

`ics-query` takes a command, a time argument, one or more calendar files, and an output.
Pass `-` as the calendar to read from stdin. Pass `-` as the output to write to stdout.

```shell
ics-query at 2019-03-04 calendar.ics -
```

## Events at a specific time

Use `at` to get all occurrences at a date, month, year, or precise time.

Get everything happening on a specific day:

```shell
ics-query at 2019-03-04 calendar.ics -
```

Get everything happening this month:

```shell
ics-query at `date +%Y-%m` calendar.ics -
```

Get everything happening right now (to the second):

```shell
ics-query at `date +%Y%m%d%H%M%S` calendar.ics -
```

Accepted time formats for `at` and for the `START` argument of `between`:

| Format | Description |
| ------ | ----------- |
| `2019` | all of 2019 |
| `2019-08` | August 2019 |
| `2019-08-12` | 12 August 2019 |
| `2019-08-12T17` | 17:00 to 18:00 on 12 August 2019 |
| `2019-08-12T17:20` | 17:20 to 17:21 on 12 August 2019 |
| `2019-08-12T17:20:00` | exactly 17:20:00 on 12 August 2019 |

Compact formats without separators are also accepted: `20190812`, `20190812T1720`, `201908121720`.

## Events within a time span

Use `between` to get occurrences between a start and an end.
Start is inclusive, end is exclusive.

Get events in the next 7 days:

```shell
ics-query between `date +%Y%m%d` +7d calendar.ics -
```

Get events between two specific dates:

```shell
ics-query between 2024-05-01 2024-06-10 calendar.ics events.ics
```

Get events around New Year's Eve midnight:

```shell
ics-query between 2025-12-31T21:00 +6h calendar.ics -
```

The `END` argument can be a relative duration after `START`:

| Duration | Description |
| -------- | ----------- |
| `+1d` | one day |
| `+1h` | one hour |
| `+1m` | one minute |
| `+1s` | one second |
| `+3600s` | one hour as seconds |
| `+5d10h` | five days and 10 hours |

The `+` prefix is optional.

## First occurrence

Use `first` to get only the first occurrence in each calendar file.

```shell
ics-query first calendar.ics -
```

## All occurrences

Use `all` to get every occurrence in a calendar.

```shell
ics-query all calendar.ics -
```

Calendars with recurring events can produce a very large number of occurrences.
Use `head` to limit the output:

```shell
ics-query all calendar.ics - | head -100
```

## Filtering by component type

By default, `ics-query` returns `VEVENT`, `VTODO`, and `VJOURNAL` components.
Use `-c` or `--component` to filter.

Only events:

```shell
ics-query at 2024-08 -c VEVENT calendar.ics -
```

Only to-dos:

```shell
ics-query at 2024-08 -c VTODO calendar.ics -
```

Only journal entries:

```shell
ics-query at 2024-08 -c VJOURNAL calendar.ics -
```

Pass `-c` multiple times to include more than one type:

```shell
ics-query at 2024-08 -c VEVENT -c VTODO calendar.ics -
```

You can also set the component via environment variable:

```shell
export ICS_QUERY_COMPONENT=VEVENT
ics-query at 2024-08 calendar.ics -
```

## Querying alarms

Use `-c VALARM` to query components by their alarm times.
`VALARM` is not included in the default output.

Alarms behave differently from other components:

- The parent component (`VEVENT`, `VTODO`) may fall outside the queried time span
  while the alarm falls within it, and it will still be included.
- Absolute alarms may appear only once, not for every recurrence.
- Each result contains only one alarm.
- Do not mix `-c VALARM` with other types. You will not be able to tell whether
  the alarm or the parent component matched the time span.

Get all alarms and show their trigger time and event summary:

```shell
ics-query all -c VALARM calendar.ics - | grep -E 'TRIGGER|SUMMARY'
```

## Timezones

By default, `ics-query` uses each component's own timezone.
Two events at 6am in different timezones both appear when you query by date,
even though they are hours apart in absolute time.

Use `--tz` to query in a specific timezone:

```shell
ics-query at --tz=Europe/Berlin 2024-08-20 calendar.ics -
```

Use `--tz=localtime` to query in your local system timezone:

```shell
ics-query at --tz=localtime 2024-08-20 calendar.ics -
```

Use `--tz=UTC` for UTC:

```shell
ics-query at --tz=UTC 2024-08-20 calendar.ics -
```

Set the timezone via environment variable:

```shell
export ICS_QUERY_TZ=Europe/Berlin
ics-query at 2024-08-20 calendar.ics -
```

List all available timezone names:

```shell
ics-query --available-timezones
```

## Valid ICS output

By default, the output contains only the matched components with no `VCALENDAR` wrapper
and no `VTIMEZONE`. This is intentional for piping into other tools.

To produce a valid `.ics` file that calendar applications can open, use `--as-calendar`:

```shell
ics-query at --as-calendar 2014-05-03 calendar.ics output.ics
```

The output is wrapped in a `VCALENDAR` block and includes any `VTIMEZONE` components
from the source calendar.

You can also set this via environment variable:

```shell
export ICS_QUERY_AS_CALENDAR=1
ics-query at 2014-05-03 calendar.ics output.ics
```

## Multiple calendars

Pass multiple files directly:

```shell
ics-query at 2024-08 calendar1.ics calendar2.ics -
```

Or concatenate them through stdin:

```shell
cat calendar1.ics calendar2.ics | ics-query at 2024-08 - -
```

## Fetching a calendar from the web

```shell
wget -qO- 'https://example.com/calendar.ics' | ics-query at 2024-08 - -
```
