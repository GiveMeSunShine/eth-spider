# -*- coding: utf-8 -*-

def _init(file_name):  # 初始化
    global _global_dal
    _global_dal = {}
    fopen = open(file_name, 'r')
    for line in fopen:
        line = line.strip()
        if line.find('=') > 0 and not line.startswith('#'):
            strs = line.split('=')
            _global_dal[strs[0].strip()] = strs[1].strip()


def get_value(key):
    return _global_dal[key]

