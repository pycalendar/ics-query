# Overview

`ics-query` is a command line tool for querying RFC 5545 `.ics` calendar files.
You give it a time and a calendar file, and it gives you back the matching components as ICS output.

It handles recurring events, timezones, and the three standard component types: events (`VEVENT`), to-dos (`VTODO`), and journal entries (`VJOURNAL`). You can also query alarms (`VALARM`) separately.

## How it works

`ics-query` reads one or more `.ics` files, expands all recurring components into their
individual occurrences, filters them by the time you specify, and writes the result to
a file or stdout.

Three libraries do the heavy lifting:

- [recurring-ical-events] expands recurring events and handles RFC 5545 recurrence rules.
- [icalendar] parses and serialises `.ics` files.
- [x-wr-timezone] handles the non-standard `X-WR-TIMEZONE` property used by some calendar apps.

## Occurrence calculation

An event can span multiple days. If you query a time window smaller than the event,
the event still appears in the result as long as it overlaps with your query.

```
event.DTSTART <= span.DTEND  and  span.DTSTART < event.DTEND
```

Start is inclusive. End is exclusive.

## When to use it

- You have `.ics` files and want to extract what is happening in a given period.
- You want to pipe calendar data into shell scripts or other tools.
- You need to filter a large calendar down to a specific component type.
- You want to check what a recurring event produces for a specific date without opening a calendar app.

## Related work

- [icalendar-events-cli](https://github.com/waldbaer/icalendar-events-cli#readme) — another command line implementation of `recurring-ical-events`
- [icalBuddy](https://hasseg.org/icalBuddy/)
- [ical2jcal](https://pypi.org/project/ical2jcal/) — convert between iCalendar `.ics` files and RFC 7265 jCal JSON
- [Blog Post](https://opencollective.com/open-web-calendar/updates/calendar-calculation-on-the-command-line-ics-query)
- [#icsquery on mastodon](https://toot.wales/tags/icsquery)
- [Homebrew tap for ics-query](https://github.com/niccokunzmann/homebrew-tap)

## Planned features

These features are planned but not yet implemented.

**`--select-index`** — Use an index or range to select which occurrence to return.
Examples: `0,2,4` or `0-10`.

**`--select-uid`** — Filter occurrences by UID.

**Edit events** — Edit occurrences to produce new ICS files.

**Notifications** — Use `ics-query` together with `cron` to get notified about upcoming events. For example: how many to-dos are in the next hour, how many events today, or a reminder to write a journal entry.

[recurring-ical-events]: https://pypi.org/project/recurring-ical-events/
[icalendar]: https://pypi.org/project/icalendar/
[x-wr-timezone]: https://pypi.org/project/x-wr-timezone/
