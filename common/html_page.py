#!/usr/bin/env python
# coding: utf8

from django.utils.safestring import mark_safe


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

    for i in range(begin, end):
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
