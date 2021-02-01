# -*- coding: utf-8 -*-
import property
import dal
import sys
import os

property._init(sys.path[0] + os.sep + "config.properties")
dal._init(sys.path[0] + os.sep + "dal.properties")
