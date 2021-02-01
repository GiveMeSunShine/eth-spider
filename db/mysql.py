# coding=utf-8
import MySQLdb
import sys
import os

from _mysql_exceptions import OperationalError

from common import property


def createDB():
    print "创建数据库"
    try:
        conn = MySQLdb.connect(host=property.get_value("db.host"), port=property.getInt("db.port"), user=property.get_value("db.user"), passwd=property.get_value("db.passwd"), db='mysql')
        cur = conn.cursor()
        sql = "CREATE DATABASE if not exists `" + property.get_value("db.name") + "` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci"
        cur.execute(sql)
        cur.close()
        conn.close()
    except OperationalError:
        print OperationalError.message


def initDB():
    print "初始化数据库"
    createDB()
    try:
        conn = MySQLdb.connect(host=property.get_value("db.host"), port=property.getInt("db.port"), user=property.get_value("db.user"), passwd=property.get_value("db.passwd"), db=property.get_value("db.name"))
        cur = conn.cursor()
        sql = open(sys.path[0] + os.sep +"initsql.sql", "r")
        sqltxt = sql.readlines()
        sql.close()
        sql = "".join(sqltxt)
        cur.execute(sql)
        cur.close()
        conn.close()
    except OperationalError:
        print OperationalError.message


def save(sql, parms):
    conn = MySQLdb.connect(host=property.get_value("db.host"), port=property.getInt("db.port"), user=property.get_value("db.user"), passwd=property.get_value("db.passwd"), db=property.get_value("db.name"))
    cur = conn.cursor()
    result = cur.execute(sql, parms)
    conn.commit()
    cur.close()
    conn.close()
    return result



