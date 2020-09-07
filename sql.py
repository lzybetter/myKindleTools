#coding:utf-8
import pymysql

def saveToMysql(clips):

    CREATE_DB = 'create database if not exists kindle;'

    db = pymysql.connect(host='localhost', user='root',passwd='Lzy19911104-',port=3306)

    cursor = db.cursor()

    cursor.execute(CREATE_DB)
    cursor.execute('use kindle')
    for clip in clips:
        print (clip)
        name = clip.split('（')[0]
        name = name.split('：')[0].split(':')[0]
        name = name.split('(')[0].replace('[','').replace(']','').replace(' ','')
        create_table = """create table if not exists %s (location INT, note TEXT);"""%name
        print(create_table)
        cursor.execute(create_table)
        for location, note in clips[clip].items():

            print(location, note)
            insert_note = """INSERT INTO %s (location, note) VALUES (%d, '%s');"""%(name, int(location), note)
            cursor.execute(insert_note)

    db.commit()
    cursor.close()
    db.close()