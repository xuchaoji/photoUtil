# -*- coding: utf-8 -*-  

""" 
功能：读取照片的exif信息，按照日期对照片进行整理
使用方法：将脚本和照片放于同一目录，运行脚本 python sort.py
"""  

import shutil  
import os  
import time  
import exifread  


class ReadFailException(Exception):  
    pass  

def getOriginalDate(filename):  
    try:  
        fd = open(filename, 'rb')  
    except:  
        raise ReadFailException, "unopen file[%s]\n" % filename  
    data = exifread.process_file( fd )  
    if data:  
        try:  
            t = data['EXIF DateTimeOriginal']  
            return str(t).replace(":",".")[:7]  
        except:  
            pass  
    state = os.stat(filename)  
    return time.strftime("%Y.%m", time.localtime(state[-2]))  


def classifyPictures(path):  
    for root,dirs,files in os.walk(path,True):  
        dirs[:] = []  
        for filename in files:  
            #filename = os.path.join(root, filename)  
            f,e = os.path.splitext(filename)  
            if e.lower() not in ('.jpg','.png','.mp4','gif','jpeg'):  
                continue  
            info = "文件名: " + filename + " "  
            t=""  
            try:  
                t = getOriginalDate( filename )  
            except Exception,e:  
                print e  
                continue  
            info = info + "拍摄时间：" + t + " "  
            pwd = t 
            #print root, pwd
            dst = pwd + '/' + filename  
            if not os.path.exists(pwd ):  
                os.mkdir(pwd)  
            print info, dst  
            shutil.copy2( filename, dst )  
            os.remove( filename )  

if __name__ == "__main__":  
    path = "."  
    classifyPictures(path) 
