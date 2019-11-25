# exceptional_dates
Dates which can be used to check date handling code.

The JSON file `dates.json` contains several lists of dates:
 - examples: examples of dates with particular properties
 - valid: valid dates from the Gregorian calendar, years 1 through 9999
 - extra: valid dates which are not from years 1-9999 (can't be represented by some date code)
 - invalid: things which aren't valid dates, and should be recognized as invalid

The format of a date object is a follows:
 - year: an integer
 - month: an integer 1-12
 - day: an integer 1-31
 - calendar: a string, always "Gregorian" except for "invalid" dates. "Gregorian" means the proleptic Gregorian calendar, ie the Gregorian calendar as extended backwards beyond the date of its actual invention
 - description: a short, unique string which describes the date
 - comment: a longer string which explains the date
