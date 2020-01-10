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
        'email=amltLnByaW9yQGFjY2VudHVyZS5jb20=',
    ))

    expected = (
        "lat:\t'here' " r"(b'\x85\xea\xde'), "
            "'there'\n",
        "link:\t'https://baz.com/#/hear/?r=joe' "
            r"(b'\x86\xdbi\xb3\xff\xdbk7(\x9b\xff\xe1y\xaa\xff\xae:\x1e')"
            "\n",
        "email:\t'amltLnByaW9yQGFjY2VudHVyZS5jb20=' "
            "(b'jim.prior@accenture.com')\n",
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
        "url:\t"
            "'https://foo.com/bar/digest"
            "?lat=here&link=https%3A%2F%2Fbaz.com%2F%23%2Fhear%2F%3Fr%3Djoe'"
            "\n"
        "scheme:\t'https'\n"
        "netloc:\t'foo.com'\n"
        "path:\t'/bar/digest'\n"
        "params:\t''\n"
        "query:\t'lat=here&"
            "link=https%3A%2F%2Fbaz.com%2F%23%2Fhear%2F%3Fr%3Djoe'\n"
        "fragment:\t''\n"
        "lat:\t'here' "
            r"(b'\x85\xea\xde')"
            "\n"
        "link:\t'https://baz.com/#/hear/?r=joe' "
            r"(b'\x86\xdbi\xb3\xff\xdbk7(\x9b\xff\xe1y\xaa\xff\xae:\x1e')"
            "\n"
    )
    main(input_lines)
    captured = capsys.readouterr()
    actual = captured.out
    assert expected == actual


def test_main_two_urls(capsys):
    input_lines = (
        'https://foo.com/\n',
        'https://bar.com/\n',
    )
    expected = (
        "url:\t'https://foo.com/'\n"
        "scheme:\t'https'\n"
        "netloc:\t'foo.com'\n"
        "path:\t'/'\n"
        "params:\t''\n"
        "query:\t''\n"
        "fragment:\t''\n"
        "\n"
        "url:\t'https://bar.com/'\n"
        "scheme:\t'https'\n"
        "netloc:\t'bar.com'\n"
        "path:\t'/'\n"
        "params:\t''\n"
        "query:\t''\n"
        "fragment:\t''\n"
    )
    main(input_lines)
    captured = capsys.readouterr()
    actual = captured.out
    assert expected == actual
