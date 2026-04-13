# Timezones

## Default behavior

By default, `ics-query` uses each component's own timezone when comparing against your query.

Two events at 6am — one in Berlin, one in Los Angeles — both match a query for a given date, even though they are hours apart in absolute time. Each event is compared against your query in its own local time.

## Querying in a specific timezone

Use `--tz` to convert all components to the same timezone before comparing:

```shell
ics-query at --tz=Europe/Berlin 2024-08-20 calendar.ics -
```

With `--tz` set, the same two 6am events behave differently. The Los Angeles event at 6am is 3pm in Berlin. If you query for August 20th in Berlin time, only the Berlin event matches — unless the LA event also overlaps that date in Berlin time.

Use `--tz=localtime` to query in your system timezone:

```shell
ics-query at --tz=localtime 2024-08-20 calendar.ics -
```

Use `--tz=UTC` for UTC:

```shell
ics-query at --tz=UTC 2024-08-20 calendar.ics -
```

Set the timezone via environment variable instead of passing the flag each time:

```shell
export ICS_QUERY_TZ=Europe/Berlin
ics-query at 2024-08-20 calendar.ics -
```

## Available timezones

`ics-query` uses Python's `zoneinfo` module for timezone data. To list all available names:

```shell
ics-query --available-timezones
```

The output includes `localtime` (your system timezone), `UTC`, and all IANA timezone names such as `Europe/Berlin`, `America/New_York`, `Asia/Tokyo`.

## Floating times

Some calendar events have no timezone at all — they use floating times. A floating time of 9am means 9am wherever you are, with no timezone attached.

When you query without `--tz`, floating times are matched against your query as-is. When you use `--tz`, floating times are treated as if they are in the specified timezone.

## X-WR-TIMEZONE

Some calendar applications export calendars with an `X-WR-TIMEZONE` property instead of individual `TZID` attributes on each component. `ics-query` handles this automatically via the [x-wr-timezone] library.

[x-wr-timezone]: https://pypi.org/project/x-wr-timezone/
