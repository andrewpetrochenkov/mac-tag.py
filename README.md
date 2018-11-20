[![](https://img.shields.io/badge/OS-MacOS-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/pyversions/mac-tag.svg?longCache=True)](https://pypi.org/pypi/mac-tag/)
[![](https://img.shields.io/pypi/v/mac-tag.svg?maxAge=3600)](https://pypi.org/pypi/mac-tag/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/mac-tag.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/mac-tag.py/)

#### Install
```bash
$ [sudo] pip install mac-tag
```

#### Requirements
```bash
$ brew install tag
```

#### Functions
function|description
-|-
`mac_tag.add(tags, path)`|add tags to path(s)
`mac_tag.find(tags, path=None)`|return list of all paths with tags, limited to path(s) if present
`mac_tag.get(path)`|return dict where keys are paths, values are lists of tags. equivalent of `tag -l`
`mac_tag.match(tags, path)`|return list of paths with with matching tags
`mac_tag.parse_list_output(out)`|parse `tag -l` output and return dict
`mac_tag.remove(tags, path)`|remove tags from path(s)
`mac_tag.update(tags, path)`|set path(s) tags. equivalent of `tag -s | --set`

#### Examples
```python
>>> mac_tag.update(["red","blue"],["path1","path2"])
>>> mac_tag.add(["green"],["path1","path2"])
```

```python
>>> mac_tag.get(["path1"])
{'path1': ['blue', 'red', 'green']}
```

```python
>>> mac_tag.remove(["red"],["path1","path2"])
>>> mac_tag.remove(["*"],["path1","path2"])
```

#### Links
+   [github.com/jdberry/tag](https://github.com/jdberry/tag)

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>