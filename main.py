# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
from eth.eth import start
from common import init
from common import property

if __name__ == '__main__':
    init
    start(property.get_value("eth.url"))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
