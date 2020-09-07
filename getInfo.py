import requests
import json
import getHeaders
import pymysql
from PIL import Image
from io import BytesIO
import os


def getBooks():
    db = pymysql.connect(host='localhost', user='root',passwd='Lzy19911104-',port=3306)
    cursor = db.cursor()

    books = []
    try:
        use_kindle = 'use kindle'
        cursor.execute(use_kindle)
        show_tables = 'show tables;'
        cursor.execute(show_tables)
        result = cursor.fetchall()
        for i in range(len(result)):
            books.append(result[i][0])
        
    finally:
        cursor.close()
        db.close()
    return books

def getPic(books):
    baseUrl = 'https://book.douban.com/j/subject_suggest?q='
    headers = getHeaders.getHeader()
    headers['accept-encoding'] = 'gzip'
    pics = []
    for book in books:
        res = requests.get(baseUrl + book, headers=headers)
        if len(res.text) > 2:
            res_json = json.loads(res.text)
            pic_url = res_json[0]['pic']
            pics.append(pic_url)
        else:
            pics.append('')

    return pics

def savePic(pics, books, path_base):
    for pic,book in zip(pics,books):
        print('获取《{0}》封面中'.format(book))
        if not os.path.exists(path_base + book):
            os.mkdir(path_base + book)
        if pic != '':
            response = requests.get(pic)
            image = Image.open(BytesIO(response.content))
            image.save(path_base + book+'/'+book+'.jpg',quality=100)
        else:
            os.popen('cp ' + path_base + '/default.jpg ' + path_base + book + '/' + book + '.jpg') 