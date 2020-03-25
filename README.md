<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/badge/OS-macOS-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/pyversions/mac-tag.svg?longCache=True)](https://pypi.org/project/mac-tag/)
[![](https://img.shields.io/pypi/v/mac-tag.svg?maxAge=3600)](https://pypi.org/project/mac-tag/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![Travis](https://api.travis-ci.org/andrewp-as-is/mac-tag.py.svg?branch=master)](https://travis-ci.org/andrewp-as-is/mac-tag.py/)

#### Installation
```bash
$ [sudo] pip install mac-tag
```

#### Requirements
```bash
$ brew install tag
```

#### Functions
function|`__doc__`
-|-
`mac_tag.add(tags, path)` |add tags to path(s)
`mac_tag.find(tags, path=None)` |return a list of all paths with tags, limited to path(s) if present
`mac_tag.get(path)` |return dict where keys are paths, values are lists of tags. equivalent of `tag -l`
`mac_tag.match(tags, path)` |return a list of paths with with matching tags
`mac_tag.parse_list_output(out)` |parse `tag -l` output and return dict
`mac_tag.remove(tags, path)` |remove tags from path(s)
`mac_tag.update(tags, path)` |set path(s) tags. equivalent of `tag -s | --set`

#### Examples
```python
>>> mac_tag.update(["Red","Blue"],["path1","path2"])
>>> mac_tag.add(["Green"],["path1","path2"])
```

```python
>>> mac_tag.get(["path1"])
{'path1': ['Blue', 'Red', 'Green']}
```

```python
>>> mac_tag.remove(["Red"],["path1","path2"])
>>> mac_tag.remove(["*"],["path1","path2"])
```

#### Links
+   [github.com/jdberry/tag](https://github.com/jdberry/tag)

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>