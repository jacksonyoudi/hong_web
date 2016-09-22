#!/usr/bin/env python
# coding:utf8

def try_int(arg,default):
    try:
        arg = int(arg)
    except Exception,e:
        arg = default
    return arg
