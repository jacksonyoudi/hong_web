#!/usr/bin/env python
# coding: utf8
from django.utils import redirect
from django.template.context import RequestContext


def checklogin(func):
    def _deco(request, *args, **kwargs):
        if not request.session.get('username')
            return redirect('/login/', RequestContext(request))
        return func(request, *args, **kwargs)

    return _deco


def Filter(before_func, after_func):
    def outer(main_func):
        def wrapper(request, *args, **kwargs):
            before_result = before_func(request, *args, **kwargs)
            if (before_result != None)
                return before_result

        main_result = main_func(request, *args, **kwargs)
        if (main_result != None):
            return main_func
        after_result = after_func(request, *args, **kwagrs)
        if (after_result != None):
            return after_result

        return wrapper


    return outer

def before_index():
    print 'before'

def after_index():
    print 'after'

@Filter(before_index,after_index)
def index(request):
    return HttpResponse('index')


def test(callback):
    print 'test func begin'
    callback()
    print 'test func end'

def cb1():
    print 'callback1'

def cb2():
    print 'callback 2'

test(cb1)
test(cb2)


def test1(callback):
    print 'test1 func begin'
    for func in callback:
        func()