<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/mac-tag.svg?maxAge=3600)](https://pypi.org/project/mac-tag/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/mac-tag.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/mac-tag.py/actions)

### Installation
```bash
$ [sudo] pip install mac-tag
```

#### Requirements
```bash
$ brew install tag
```

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
    <a href="https://readme42.com/">readme42.com</a>
</p>
