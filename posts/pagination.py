from rest_framework import pagination


class ListPagination(pagination.LimitOffsetPagination):
    default_limit = 2
    max_limit = 1000
