#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import public
import runcmd
import values

"""
https://github.com/jdberry/tag
"""

bin = "/usr/local/bin/tag"


def _string(value):
    try:
        return isinstance(value, basestring)
    except NameError:
        return isinstance(value, str)


def run(args):
    """run `/usr/local/bin/tag` with arguments and return output"""
    if not os.path.exists(bin):
        raise OSError("%s NOT EXISTS\nrun `brew install tag`" % bin)
    return runcmd.run([bin] + values.get(args))._raise().out


def _tags(value):
    if not value:
        return []
    if _string(value):
        return [value]
    return [",".join(value)]


@public.add
def add(tags, path):
    """add tags to path(s)"""
    if path:
        run(["-a"] + _tags(tags) + values.get(path))


@public.add
def remove(tags, path):
    """remove tags from path(s)"""
    tags = "*" if not tags else _tags(tags)
    if path:
        run(["-r"] + tags + values.get(path))


@public.add
def update(tags, path):
    """set path(s) tags. equivalent of `tag -s | --set`"""
    if path:
        run(["-s"] + _tags(tags) + values.get(path))


@public.add
def match(tags, path):
    """return a list of paths with with matching tags"""
    args = ["-m"] + _tags(tags) + values.get(path)
    out = run(args)
    return out.splitlines()


@public.add
def parse_list_output(out):
    """parse `tag -l` output and return dict"""
    result = dict()
    for l in out.splitlines():
        if "\t" in l:
            path, tags = l.split("\t")
            result[path] = tags.split(",")
        else:
            result[l] = []
    return result


@public.add
def get(path):
    """return dict where keys are paths, values are lists of tags. equivalent of `tag -l`"""
    args = ["-l"] + values.get(path)
    out = run(args)
    return parse_list_output(out)


@public.add
def find(tags, path=None):
    """return a list of all paths with tags, limited to path(s) if present"""
    args = ["-f"] + _tags(tags) + values.get(path)
    out = run(args)
    return out.splitlines()
