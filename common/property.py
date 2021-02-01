# -*- coding: utf-8 -*-

def _init(file_name):  # 初始化
    global _global_porperties
    _global_porperties = {}
    fopen = open(file_name, 'r')
    for line in fopen:
        line = line.strip()
        if line.find('=') > 0 and not line.startswith('#'):
            strs = line.split('=')
            _global_porperties[strs[0].strip()] = strs[1].strip()


def set_value(key, value):
    """ 定义一个全局变量 """
    _global_porperties[key] = value


def get_value(key):
    return _global_porperties[key]


def getInt(key):
    return int(_global_porperties[key])
