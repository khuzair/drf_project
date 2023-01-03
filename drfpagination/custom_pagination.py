from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class MyCustomePageNumberPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'record'
    max_page_size = 6


class MyCustomLimitOffesetPagination(LimitOffsetPagination):
    default_limit = 4 # as equal to page_size
    limit_query_param = 'mylimit' # default will be 'limit' query parameter
    offset_query_param = 'myoffset' # where to start and show the records, default name will be offset query parameter
    max_limit = 5


class MyCustomCursonPagination(CursorPagination):
    page_size = 4
    ordering = 'name'
    cursor_query_param = 'cu'