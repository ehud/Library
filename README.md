# Library
Scripts for automating relationship with university library.

## Purchase order

Reads a list of ISBNs from file, fetches book information from
WorldCat and prepares a monthly purchase form ready to be sent to the
library.

Books that are not found on WolrdCat (yet) remain in the
file. Otherwise the books are removed, and their ISBNs are appended to
the watched for ISBN file.

## Watcher

Reads a list of ISBNs and searches the university library (powered by Ex Libris Aleph) to
see if they have the book. If found, a notification is emailed.

Note that this script searches the library catalog of Tel Aviv University. The search url should be customized to that of your local institution.
