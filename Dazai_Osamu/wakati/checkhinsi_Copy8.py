
# coding: utf-8

# In[1]:


import sys
import commands as cmd
import MeCab 

m = MeCab.Tagger()
o = MeCab.Tagger("-Owakati")


# In[2]:

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


# In[3]:

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


# In[4]:

def conv2wakati(line):
    ### wakati: mecab による分かち書き形式に変換したline. str 型
    wakati = o.parse(line)
    return wakati


# In[5]:

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


# In[7]:

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


# In[15]:

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


# In[16]:

def do(fname, wIDn, wordsn, phrasen):
    f = open(fname, "r")
    flen = len( f.readlines() )
    f.close()
    f = open(fname, "r")
    
    for i in range(0,flen):
        line = f.readline()
        if (len(line) >= 2):
            checkhinsi(line, wIDn, wordsn, phrasen)
    f.close()


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


# In[ ]:



