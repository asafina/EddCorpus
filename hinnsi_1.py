
# coding: utf-8

# In[52]:



import sys
import commands as cmd
import codecs

reload(sys)
sys.setdefaultencoding("utf-8")
print "defaultencoding:", sys.getdefaultencoding()


# In[53]:

def hinsi(obj):
    temp1 = cmd.getstatusoutput("cat " + obj + "| awk '{print $2}' | sed -e 's/,.*//g'" )
    for a in temp1:
        print a
    
    temp2 = cmd.getstatusoutput("cat " + obj + "| awk '{print $1}'")
    for a in temp2:
        print a
    
    f1 = open("./test1.dat", "w")
    f1.write(str(temp1))


# In[54]:

open_file = open("./resultmecab/test.txt/0001.dat", "r")

for a in open_file:
    print a


# In[55]:

hinsi("./resultmecab/test.txt/0001.dat")


# In[56]:

f = open("./test1.dat", "r")
for a in f:
    print a


# In[ ]:



