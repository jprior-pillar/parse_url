#!/usr/bin/env python3

import sys
from urllib.parse import urlparse, parse_qs
from base64 import b64decode
import binascii


def format_parsed_url(parsed_url):
    field_names = ('scheme', 'netloc', 'path', 'params', 'query', 'fragment')
    for field_name, value in zip(field_names, parsed_url):
        yield f'{field_name}:\t{value!r}\n'


def format_query_value(value):
    s = repr(value)
    try:
        d = b64decode(value)
    except binascii.Error:
        pass
    else:
        s += f' ({d!r})'
    return s


def format_query(query):
    for field_name, values in parse_qs(query).items():
        formatted_values = ', '.join(
            map(format_query_value, values)
        )
        yield f'{field_name}:\t{formatted_values}\n'
    

def print_lines(lines):
    for line in lines:
        print(line, end='')


def main(padded_urls):
    for padded_url in padded_urls:
        url = padded_url.strip()
        print(f'url:\t{url!r}')
        parsed_url = urlparse(url)
        print_lines(format_parsed_url(parsed_url))
        query = parsed_url.query
        print_lines(format_query(query))


if __name__ == '__main__':
    main(sys.stdin)
