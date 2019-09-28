#!/bin/bash

src="./Private"
#源文件的父目录

dst="./timeLine3"
#目标目录

function read_dir(){
    for file in `ls $1`;do   #step1 遍历文件
        echo "判断 " $file "文件类型中..."
        if [ -d $1"/"$file ];then
	    echo $file "是目录，处理目录中的文件"
            read_dir $1"/"$file $2
        elif [ -f $1"/"$file ];then #step2 复制文件到目标目录
           echo "复制" $file "到" $2
            [[ `cp -f -v -p $1"/"$file $2` ]]
        else echo ".."
        fi
    done
}

read_dir $src $dst
#递归查找src中的文件，复制到dst中 (暂不能处理重名文件)
echo "复制完毕"
