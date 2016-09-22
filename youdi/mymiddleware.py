#!/usr/bin/env python
# coding:utf8
'''
    Create on
    @author: youdi
'''

from django.http.response import HttpResponse


class MywebMiddleware(object):
    def process_request(self, request):
        print '1.process_request'
        print request.get_host

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print '1.process_view'

    def process_exception(self, request, exception):
        print '1.process_exception'

    def process_response(self, request, response):
        print '1.process_response'
        return response

class MywebMiddleware2(object):
    def process_request(self, request):
        print '2.process_request'

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print '2.process_view'

    def process_exception(self, request, exception):
        print '2.process_exception'

    def process_response(self, request, response):
        print '2.process_response'
        return response