#!/bin/bash

### パスはフォルダを指定
## ./domecab.sh corpus/

path=$1

#改行を空白へ変換
ls -l $1 | grep ^- | awk '{print $10}' > fnamelist.tmp

filename=(`cat fnamelist.tmp | perl -pe 's;\n; ;g'`)
filenum=`ls -l $path | wc -l`
filenum=`expr $filenum - 1`

echo ;

~/Myshell/seekdir.sh resultmecab || mkdir resultmecab ; { echo created directory resultmecab. ; }
~/Myshell/seekdir.sh $dirname ./resultmecab/ || mkdir ./resultmecab/$dirname ; { echo created directory resultmecab/$dirname. ; }


for((i=0; i<$filenum; i++));do
    echo $path${filename[i]};
    mkdir ./resultmecab/${filename[i]}
    ./remecab.sh $path${filename[i]} || { echo "err."; exit 1 ; }
done

echo ;
echo completed.
echo ;
