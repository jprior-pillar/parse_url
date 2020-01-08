#!/usr/bin/env python3

import sys
from urllib.parse import urlparse, parse_qs


def format_parsed_url(parsed_url):
    field_names = ('scheme', 'netloc', 'path', 'params', 'query', 'fragment')
    for key, value in zip(field_names, parsed_url):
        yield f'{key}:\t{value!r}\n'


def format_query(query):
    for key, values in parse_qs(query).items():
        formatted_values = ', '.join(
            repr(value) for value in values
        )
        yield f'{key}:\t{formatted_values}\n'
    

def print_lines(lines):
    for line in lines:
        print(line, end='')


def main(lines):
    for line in lines:
        url = line.strip()
        print(f'url:\t{url!r}')
        parsed_url = urlparse(url)
        print_lines(format_parsed_url(parsed_url))
        query = parsed_url.query
        print_lines(format_query(query))


if __name__ == '__main__':
    main(sys.stdin)
