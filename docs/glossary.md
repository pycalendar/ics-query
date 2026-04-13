# Glossary

```{glossary}
ICS file
  A text file in the iCalendar format with a `.ics` extension. Defined by RFC 5545.

RFC 5545
  The Internet standard that defines the iCalendar format. Specifies the structure of `.ics` files, component types, properties, and recurrence rules.

VCALENDAR
  The top-level wrapper component in an `.ics` file. Contains all other components.

VEVENT
  A calendar event. Has a start time (`DTSTART`), optional end time (`DTEND`), and optional recurrence rules.

VTODO
  A to-do item. Like a `VEVENT` but represents a task rather than a scheduled event. May have a due date instead of an end time.

VJOURNAL
  A journal entry. Represents a note or record associated with a date.

VALARM
  An alarm attached to a `VEVENT` or `VTODO`. Has a trigger time (absolute or relative to the parent component). Not included in default output — use `-c VALARM` to query alarms.

VTIMEZONE
  A timezone definition embedded in a calendar file. Defines the UTC offset and daylight saving rules for a named timezone.

DTSTART
  The start date or date-time of a component. For recurring components, this is the start of the first occurrence.

DTEND
  The end date or date-time of a component. Exclusive — an event ending at 10:00 does not overlap a query starting at 10:00.

RRULE
  A recurrence rule. Defines how a component repeats — daily, weekly, monthly, and so on. `ics-query` expands these into individual occurrences automatically.

EXDATE
  A list of dates excluded from a recurrence series. Occurrences on these dates are skipped.

occurrence
  A single instance of a component. A weekly recurring event has one occurrence per week. `ics-query` filters and returns occurrences, not the raw recurring rule.

recurrence
  A component that repeats over time, defined by an `RRULE`. `ics-query` uses [recurring-ical-events] to expand recurrences into individual occurrences.

floating time
  A date-time with no timezone. Interpreted as local time wherever it is read. Contrast with a timezone-aware date-time which has a fixed `TZID`.

X-WR-TIMEZONE
  A non-standard calendar property used by some applications (e.g., Google Calendar exports) to specify a calendar-wide timezone. `ics-query` handles this automatically.
```

[recurring-ical-events]: https://pypi.org/project/recurring-ical-events/
