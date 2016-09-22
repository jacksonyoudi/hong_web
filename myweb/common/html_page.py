#!/usr/bin/env python
# coding: utf8

from django.utils.safestring import mark_safe


class PageInfo():
    def __init__(self, current_page, all_count, per_item=5):
        self.CurrentPage = current_page
        self.AllCount = all_count
        self.PerItem = per_item

    @property
    def start(self):
        return (self.CurrentPage - 1) * self.PerItem

    @property
    def end(self):
        return self.CurrentPage * self.PerItem

    @property
    def all_page_count(self):
        temp = divmod(self.AllCount, self.PerItem)
        if temp[1] == 0:
            all_page_count = temp[0]
        else:
            all_page_count = temp[0] + 1
        return all_page_count


def Pager(page, all_page_count):
    '''
    :param page:  当前页
    :param all_page_count: 所有页
    :return: 生成的分页html代码
    '''
    first_page = '<a href="/web/index/%d/">首页</a>' % 1
    if page <= 1:
        prev_page = '<a href="#">上一页</a>'
    else:
        prev_page = '<a href="/web/index/%d/">上一页</a>' % (page - 1,)
    page_html = []
    page_html.append(first_page)
    page_html.append(prev_page)

    begin = page - 5
    end = page + 5
    if all_page_count < 11:
        begin = 0
        end = all_page_count
    else:
        if page < 5:
            begin = 0
            end = 11
        else:
            if page + 6 > all_page_count:
                begin = page - 6
                end = all_page_count
            else:
                begin = page - 6
                end = page + 5

    for i in xrange(begin, end):
        if page == i + 1:
            a_html = '<a class="selected" href="/web/index/%d/">%d</a>' % (i + 1, i + 1)
        else:
            a_html = '<a  href="/web/index/%d/">%d</a>' % (i + 1, i + 1)
        page_html.append(a_html)
    if page >= all_page_count:
        next_page = '<a href="#">下一页</a>'
    else:
        next_page = '<a href="/web/index/%d/">下一页</a>' % (page + 1,)
    end_page = '<a href="/web/index/%d/">尾页</a>' % all_page_count
    page_html.append(next_page)
    page_html.append(end_page)
    page_html = mark_safe(' '.join(page_html))
    return page_html
