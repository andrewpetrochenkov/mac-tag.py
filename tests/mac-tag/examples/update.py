#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mac_tag

tags = ["red", "blue"]
path = [__file__]

mac_tag.update(tags, path)
print(mac_tag.get(path))
