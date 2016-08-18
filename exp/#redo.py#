#!/usr/bin/env python
# -*- coding: utf-8 -*-
import commands as cmd

# 繰り返し作業するオブジェクトをまとめたもの
catalog = cmd.getstatusoutput('cat ls.tmp')

# catalog の一要素目に 0 が格納されてしまうので、それを飛ばすために必要
def foo():
    foo.count += 1
foo.count = 0

# redo
for x in catalog:
    if foo.count == 0:
        foo()
        continue;
    
    

