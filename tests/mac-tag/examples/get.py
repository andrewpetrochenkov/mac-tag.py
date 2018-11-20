#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mac_tag

tags = ["red", "blue"]
path = [__file__]

mac_tag.set(tags, path)
tags = mac_tag.get(path)
print(tags)
