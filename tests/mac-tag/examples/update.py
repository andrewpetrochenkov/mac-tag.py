#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mac_tag

tags = ["Red", "Blue"]
path = [__file__]

mac_tag.update(tags, path)
print(mac_tag.get(path))
