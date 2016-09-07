
# coding: utf-8

# In[11]:


import sys
import commands as cmd
import MeCab 
import numpy as np
import os

np.set_printoptions(threshold=np.inf)

m = MeCab.Tagger()
o = MeCab.Tagger("-Owakati")


# In[ ]:

def checkhinsi(line, wIDn, wordsn, phrasen):
    print "-**************************************"
    print "line: " + line
    
    ### pline: mecab による解析結果が入った str 型
    pline = (m.parse(line))
    ### pline2: 単語の解析結果を要素にもつ list 型に
    pline2 = pline.split("\n")
    ### wakati: mecab による分かち書き形式に変換したline. str 型
    wakati = o.parse(line)
    ### words: line を単語要素とした list 型
    words = wakati.split(" ")
    
    print "num of words: ",
    print len(words) - 1
    
    ### phrase 自立語と付属語をそれぞれ 1, 0 として line を表現
    phrase = []
    
    ### wID: 読み込んだ corpus での word が何列目に存在するかを格納したもの、 list型
    wID = []
    
    for i in range(0,len(words)-1):
        if "名詞" in pline2[i]:
            phrase.append("1")
            wID.append( searchwordID(words[i], "名詞") )
        elif "動詞" in pline2[i]:
            phrase.append("1")
            wID.append( searchwordID(words[i], "動詞") )
        elif "形容詞" in pline2[i]:
            phrase.append("1")
            wID.append( searchwordID(words[i], "形容詞") )
        elif "副詞" in pline2[i]:
            phrase.append("1")
            wID.append( searchwordID(words[i], "副詞") )
        elif "助詞" in pline2[i]:
            phrase.append("0")
            wID.append( searchwordID(words[i], "助詞") )
        elif "接続詞" in pline2[i]:
            phrase.append("1")
            wID.append( searchwordID(words[i], "接続詞") )
        elif "助動詞" in pline2[i]:
            phrase.append("0")
            wID.append( searchwordID(words[i], "助動詞") )
        elif "連体詞" in pline2[i]:
            phrase.append("1")
            wID.append( searchwordID(words[i], "連体詞") )
        elif "感動詞" in pline2[i]:
            phrase.append("1")
            wID.append( searchwordID(words[i], "感動詞") )
        elif "記号" in pline2[i]:
            phrase.append("1")
            wID.append( searchwordID(words[i], "記号") )
        else:
            print "未知語: " + words[i];
            phrase.append("2")
            wID.append( 0 )
        #elif "" in pline:
        #    print ": " + line
        
    print ;
    print phrase;
    print wID;
    
    split2phrase(words, phrase)
    savedata(wID, wIDn , words, wordsn, phrase, phrasen)
    
    #temp = cmd.getstatusoutput("cat " + pline + "| awk '{print $2}' | sed -e 's/,.*//g'" )


# In[ ]:

def split2phrase(words, phrase):
    frag = 0
    for i in range(0, len(words)-1):
        if (phrase[i] == "1"):
            print "/" + words[i],
        elif (phrase[i] == "0"):
            print words[i],
        elif (phrase[i] == "2"):
            print "/" + words[i],
            frag = 1
    
    print ;
    print ;
    if (frag == 1):
        print "未知語が含まれています"


# In[ ]:

def conv2wakati(line):
    ### wakati: mecab による分かち書き形式に変換したline. str 型
    wakati = o.parse(line)
    return wakati


# In[ ]:

def getcorpus():
    c = []
    f = open("/local/home/hina/gitrepos/EddCorpus/Dazai_Osamu/wakati/mecab/Dazai_Osamu.corpus.uniq.org", "r")
    flen = len( f.readlines() )
    f.close()
    f = open("/local/home/hina/gitrepos/EddCorpus/Dazai_Osamu/wakati/mecab/Dazai_Osamu.corpus.uniq.org", "r")
    for i in range(1, flen):
        a = f.readline()
        b = a.split(" ")
        while b.count('') > 0:
            b.remove('')
        c.append(b)
    f.close()
    return c


# In[ ]:

def searchwordID(word, hinnsi):
    corpus = getcorpus()
    lines = len(corpus)
    wtmp = word.decode("utf-8")
    htmp = hinnsi.decode("utf-8")
    count = 1
    flag = False
    for line in corpus:
        for a in line:
            atmp = a.decode("utf-8")
            if atmp.startswith(wtmp):
                if atmp.find(htmp):
                    return count
                    flag = True
                    break
        if flag:
            break
        count += 1


# In[ ]:

def savedata(wID, wIDn , words, wordsn, phrase, phrasen):
    f1 = open(wIDn, "a")
    f2 = open(wordsn, "a")
    f3 = open(phrasen, "a")
    
    f1.write( str(wID) )
    f1.write("\n")
    f2.write( str(words) )
    f2.write("\n")
    f3.write( str(phrase) )
    f3.write("\n")
    
    f1.close()
    f2.close()
    f3.close()


# In[ ]:

def makewakati(fnamer, fnamew):
    f = open("fnamer", "r")
    out = open("./wakati/fnamew", "w")

    for i in range(0,680):
        line = f.readline()
        if (len(line) >= 2):
            temp = conv2wakati(line)
            print i,
            print temp;
            out.write(temp)

    ### close() をしないと書き込みが正常に終了しない！        
    out.close()


# In[2]:

def rmnewline(lst):
    a = []
    for x in lst:
        tmp = x.strip()
        tmp = tmp.strip("[")
        a.append( tmp.strip("]") )
    return a


# In[3]:

def wIDproc(lst):
    a = []
    for x in lst:
        b = x.split(", ")
        a.append(b)
    return a


# In[4]:

def phraseproc(lst):
    c = []
    ite = 0
    for k in lst:
        a = list(k)
        b = []
        for x in a:
                if x == "1":
                    b.append("1")
                elif x == "0":
                    b.append("0")
        c.insert(ite, b)
        ite += 1
    return c


# In[5]:

def readfile(fname, opt, typ):
    flag = 0
    if opt == "lines":
        if typ == "phrase":
            f = open(fname, "r")
            a = createonehotvec(f.readlines(), 35854, typ)
            f.close()
            return a
    
        f = open(fname, "r")
        a = createonehotvec(f.readlines(), 35854, typ)
        f.close()
        return a
    
    elif opt == "line":
        f = open(fname, "r")
        flen = len(f.readlines())
        f.close()
        f = open(fname, "r")
        for i in range(1, flen):
            if flag ==0:
                a = f.readline()
                b = createonehotvec(a, 35854, typ)
                flag += 1
            a = f.readline()
            b.append( createonehotvec(a, 35854, typ) )
        f.close()
        return b


# In[6]:

def splitwID2phrase(wID, phrase):
    # c: 何文節目か
    c = []
    # d: 何行目か
    d = []
    i = 0
    index = 0
    while i < len(phrase):
        b = []
        c = []
        flag = 0
        ii = 0
        index = 0
        for x in phrase[i]:
            if x == "1":
                if flag == 0:
                    b.append(wID[i][ii])
                    ii += 1
                    flag += 1
                    continue
                c.insert(index, b)
                index += 1
                b = []
                b.append(wID[i][ii])
                ii += 1
            if x == "0":
                b.append(wID[i][ii])
                ii += 1
            if x == "2":
                b.append("0")
                ii += 1
        
        c.insert(index, b)
        d.insert(i, c)
        i += 1
    return  d


# In[7]:

def createonehotvec(lst, voc, typ):
    #a = np.zeros( (1, voc) )
    if typ == "phrase":
        a = phraseproc(lst)
        #a = rmnewline(a)
        a = np.array(a)
        return a
    if typ == "wID":
        a = rmnewline(lst)
        a = wIDproc(a)
        a = np.array(a)
        return a


# In[9]:

def onehotvec_bak(phrase, V):
    a = np.zeros( (1, V) )
    print a
    for x in phrase:
        print x
        a[0][x] = '1.'
    return a
#lst = ['1', '3']
#onehotvec(lst, 5)


# In[20]:

def onehotvec_bak2(phrase, V):
    for x in phrase:
        a = np.zeros( (1, V) )
        print x
        if len(x)>1:
            for y in x:
                xx = int(y)
                a[0][xx] = '1'
            print "a: ",
            print type(a),
            print a
            continue
        a[0][x] = '1'
        print "a: ",
        print type(a),
        print a
    return a
#lst = [[0], [1, 3], [2, 4]]
#a = onehotvec(lst, 5)
#print a
#print type(a)


# def onehotvec_bak3(phrase, V):
#     i = 0
#     plen = len(phrase)
#     a = np.zeros( (plen, V) )
#     for x in phrase:
#         print x
#         if len(x)>1:
#             for y in x:
#                 xx = int(y)
#                 a[i][xx] = '1'
#             print "a: ",
#             print type(a),
#             print a
#             i += 1
#             continue
#         a[i][x] = '1'
#         print "a: ",
#         print type(a),
#         print a
#         i += 1
#     return a
# lst = [[0], [1, 3], [2, 4]]
# a = onehotvec(lst, 5)
# print "main: "
# print a
# #print type(a)

# In[28]:

def onehotvec(phrase, V):
    i = 0
    plen = len(phrase)
    a = np.zeros( (plen, V) )
    for x in phrase:
        if len(x)>1:
            for y in x:
                xx = int(y)
                a[i][xx] = '1'
            i += 1
            continue
        a[i][x] = '1'
        i += 1
    return a
#lst = [[0], [1, 3], [2, 4]]
#a = onehotvec(lst, 5)
#print type(a)


# In[1]:

# type(my_wID[1]): <type 'list'>
#my_wID = readfile("/local/home/hina/gitrepos/EddCorpus/Dazai_Osamu/wakati/preproc/human_lost.txt.utf8.ped.wakati.wID", "lines", "wID")
# type(my_phrase[1]): <type 'list'>
#my_phrase = readfile("/local/home/hina/gitrepos/EddCorpus/Dazai_Osamu/wakati/preproc/human_lost.txt.utf8.ped.wakati.phrase", "lines", "phrase")
#my_phrase = np.loadtxt(\"/local/home/hina/gitrepos/EddCorpus/Dazai_Osamu/wakati/preproc/human_lost.txt.utf8.ped.wakati.phrase\")

#print "main: "
#a = splitwID2phrase(my_wID, my_phrase)
#print "wID: "
#print my_wID
#print type(my_wID)
#print "a: "
#print a
#print type(a)

# a[何行目か][何文節目か][何単語目か]
##print a[4][2][1]
##print "len: ",
##print len(a[4][1][0:])
    
def temp(phr):
    print type(phr)
    i = 0
    for a in phr:
        print ;
        print i,
        print ": ",
        print a
        b = onehotvec(a, 35855)
        i += 1
    
    #print "b: ",
    #print type(b),
    #print b
    #f = open("/local/home/hina/gitrepos/EddCorpus/test0001.dat", "w")
    #f.write( str(b) )
    #f.close()
    
#temp(a)


# In[22]:

def do(fname):
    root, ext = os.path.splitext(fname)
    a = root + ".phrase"
    my_wID = readfile(fname, "lines", "wID")
    my_phrase = readfile(a, "lines", "phrase")
    
    temp = splitwID2phrase(my_wID, my_phrase)
    i = 0
    for x in temp:
        print ;
        print i,
        print ": ",
        print x
        b = onehotvec(x, 35855)
        i += 1
    print "b: ",
    print type(b),
    print b

    #fw = root + ".splitphrase"
    #f = open(fw, "w")
    #f.write( str(b) )
    #f.close()
    
    #np.savetxt('test.csv', ndarr1, delimiter=',')


# In[29]:

#do("/local/home/hina/gitrepos/EddCorpus/Dazai_Osamu/wakati/preproc/human_lost.txt.utf8.ped.wakati.wI")


# In[ ]:



