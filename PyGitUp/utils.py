# coding=utf-8
"""
Some simple, generic usefull methods.
"""

import subprocess
import sys


def find(seq, test):
    """ Return first item in sequence where test(item) == True """
    for item in seq:
        if test(item):
            return item


def uniq(seq):
    """ Return a copy of seq without duplicates. """
    seen = set()
    return [x for x in seq if str(x) not in seen and not seen.add(str(x))]


def execute(cmd):
    """ Execute a command and return it's output. """
    try:
        lines = subprocess.check_output(cmd).splitlines()
    except subprocess.CalledProcessError:
        return None
    else:
        if lines:
            return lines[0].strip()
        else:
            return None


def decode(s):
    """
    Decode a string using the system encoding if needed (ie byte strings)
    """
    if isinstance(s, bytes):
        return s.decode(sys.getdefaultencoding())
    else:
        return s
