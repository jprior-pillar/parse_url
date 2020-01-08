#!/usr/bin/env python3

import sys
from urllib.parse import urlparse, parse_qs


def format_parsed_url(parsed_url):
    # q = urlparse(parsed_url)

    field_names = ('scheme', 'netloc', 'path', 'params', 'query', 'fragment')
    for key, value in zip(field_names, parsed_url):
        yield f'{key}:\t{value!r}\n'


def format_query(query):
    output = []
    for key, value in parse_qs(query).items():
        output.append(f'{key}:\t{value!r}\n')
    return ''.join(output)
    

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
        print(format_query(query), end='')
    pass


if __name__ == '__main__':
    main(sys.stdin)
