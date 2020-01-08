from urllib.parse import urlparse, parse_qs

import pytest

from parse_url import format_parsed_url, format_query, main

def test_format_parsed_url():
    url = (
        'https://foo.com/bar/digest'
        '?lat=here&link=https%3A%2F%2Fbaz.com%2F%23%2Fhear%2F%3Fr%3Djoe'
    )
    parsed_url = urlparse(url)
    expected = (
        "scheme:\t'https'\n",
        "netloc:\t'foo.com'\n",
        "path:\t'/bar/digest'\n",
        "params:\t''\n",
        "query:\t'lat=here&link=https%3A%2F%2Fbaz.com%2F"
            "%23%2Fhear%2F%3Fr%3Djoe'\n",
        "fragment:\t''\n",
    )
    actual = tuple(format_parsed_url(parsed_url))
    assert expected == actual


def test_format_query():
    query = '&'.join((
        'lat=here',
        'lat=there',
        'link=https%3A%2F%2Fbaz.com%2F%23%2Fhear%2F%3Fr%3Djoe',
    ))

    expected = (
        "lat:\t'here', 'there'\n",
        "link:\t'https://baz.com/#/hear/?r=joe'\n",
    )
    actual = tuple(format_query(query))
    assert expected == actual
    

def test_main(capsys):
    input_lines = (
        (
            'https://foo.com/bar/digest'
            '?lat=here&link=https%3A%2F%2Fbaz.com%2F%23%2Fhear%2F%3Fr%3Djoe\n'
        ),
    )
    expected = (
        'url:\t' 
        "'https://foo.com/bar/digest"
        "?lat=here&link=https%3A%2F%2Fbaz.com%2F%23%2Fhear%2F%3Fr%3Djoe'"
        '\n'

        "scheme:\t'https'\n"
        "netloc:\t'foo.com'\n"
        "path:\t'/bar/digest'\n"
        "params:\t''\n"
        "query:\t'lat=here&link=https%3A%2F%2Fbaz.com%2F"
            "%23%2Fhear%2F%3Fr%3Djoe'\n"
        "fragment:\t''\n"

        "lat:\t'here'\n"
        "link:\t'https://baz.com/#/hear/?r=joe'\n"
    )
    main(input_lines)
    captured = capsys.readouterr()
    actual = captured.out
    assert expected == actual
