#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, math
import MeCab
import os

m = MeCab.Tagger()
o = MeCab.Tagger("-Owakati")

pwd = os.getcwd()

def conv2wakati(line):
    ### wakati: mecab による分かち書き形式に変換したline. str 型
    wakati = o.parse(line)
    return wakati

def makewakati(fnamer, fnamew):
    print fnamer
    print fnamew
    f = open(fnamer, "r")
    out = open(fnamew, "w")

    for i in range(0,680):
        line = f.readline()
        if (len(line) >= 2):
            temp = conv2wakati(line)
            print i,
            print temp;
            out.write(temp)

    ### close() をしないと書き込みが正常に終了しない！        
    out.close()

def domecab(fnamer, fnamew):
    print fnamer
    print fnamew
    f = open(fnamer, "r")
    out = open(fnamew, "w")

    for i in range(0,680):
        line = f.readline()
        if (len(line) >= 2):
            temp = m.parse(line)
            print i,
            print temp;
            out.write(temp)

    ### close() をしないと書き込みが正常に終了しない！        
    out.close()


def temp():

    if os.path.exists("/local/home/hina/gitrepos/EddCorpus/corpus/wakati"):
        os.mkdir("wakati")
        print "made wakati directory";    
    else :
        print "exist";

        makewakati("/local/home/hina/gitrepos/EddCorpus/corpus/test.txt", "/local/home/hina/gitrepos/EddCorpus/exp/wakati/text.txt.wakati")
        
