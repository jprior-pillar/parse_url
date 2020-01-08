#!/usr/bin/env python3

import sys
from urllib.parse import urlparse, parse_qs


def format_parsed_url(parsed_url):
    # q = urlparse(parsed_url)

    field_names = ('scheme', 'netloc', 'path', 'params', 'query', 'fragment')
    return ''.join(
        f'{key}:\t{value!r}\n'
        for key, value in zip(field_names, parsed_url)
    )


def format_query(query):
    output = []
    for key, value in parse_qs(query).items():
        output.append(f'{key}:\t{value!r}\n')
    return ''.join(output)
    

def main(lines):
    for line in lines:
        url = line.strip()
        print(f'url:\t{url!r}')
        parsed_url = urlparse(url)
        print(format_parsed_url(parsed_url), end='')
        query = parsed_url.query
        print(format_query(query), end='')
    pass


if __name__ == '__main__':
    main(sys.stdin)
