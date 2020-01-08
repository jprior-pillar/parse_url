parse_url.py
============

parse_url.py shows information parsed from URLs.
It is a command line filter.
URLs are input, one per line on standard input.
The information is output on standard output.
base64 decoded query values are shown if query values can be base64 decoded.

For example:

    you@here:~$ echo 'https://www.foo.com/bar?site=1&link=https%3a%2f%2fhello.com%2fworld%23%2f92387499-2034-9827-8972-043257012987' | ./parse_url.py
    url:    'https://www.foo.com/bar?site=1&link=https%3a%2f%2fhello.com%2fworld%23%2f92387499-2034-9827-8972-043257012987'
    scheme: 'https'
    netloc: 'www.foo.com'
    path:   '/bar'
    params: ''
    query:  'site=1&link=https%3a%2f%2fhello.com%2fworld%23%2f92387499-2034-9827-8972-043257012987'
    fragment:       ''
    site:   '1'
    link:   'https://hello.com/world#/92387499-2034-9827-8972-043257012987'
    you@here:~$
