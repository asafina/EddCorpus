#!/bin/bash
# -*- coding: utf-8 -*-

## ./hogehoge/judrjudr.txt
path=$1

linenum=`cat $path | wc -l`
line=(`cat $path | perl -pe 's;\n; ;g'`)
filename=`basename $path`

echo ${line[@]};

mecab&
remecab(){
mecab<<EOF
`echo ${line[i]}`
EOF
}


linenumber=`printf %04d $linenum`
for((i=0; i<$linenum; i++));do
    ind=`expr $i + 1`
    HOSTNAME[$i]="`printf %04d $ind`"
    echo ${HOSTNAME[$i]} / $linenumber;
    remecab > ./resultmecab/$filename/${HOSTNAME[$i]}.dat ;
done
