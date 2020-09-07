import sql
# import getUSB
import kindle
import pymysql
import getInfo
import getHeaders
from PIL import Image
import requests
from io import BytesIO
import json
import os

# path = getUSB.getUDiskPath()
# path = '/home/lzybetter/Nutstore Files/myKindleTools/My Clippings.txt'
# if path != None:
#     sql.saveToMysql(kindle.return_clip(path))
# else:
#     print('Not Found Kindle')

path_base = '/home/lzybetter/test/'


    
books = getInfo.getBooks()
pics = getInfo.getPic(books)
getInfo.savePic(pics, books, path_base)