#!/usr/bin/env python
# -*- coding: utf-8 -*-
import commands as cmd

# 繰り返し作業するオブジェクトをまとめたもの
cataloga = cmd.getstatusoutput('cat ls.tmp')
catalog = cataloga[1].split("\n");

out = open("/local/home/hina/gitrepos/EddCorpus/Dazai_Osamu/wakati/mecab/Dazai_Osamu.corpus", "a")

# redo
for x in catalog:
    a = open(x, "r")
    out.write(a.read()) 
   
