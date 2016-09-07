#!/usr/bin/env python
# -*- coding: utf-8 -*-
import commands as cmd
import checkhinsi3 as ch

# 繰り返し作業するオブジェクトをまとめたもの
cataloga = cmd.getstatusoutput('cat ls.tmp')
catalog = cataloga[1].split("\n");

# redo
for x in catalog:
    ch.do(x) 
   
