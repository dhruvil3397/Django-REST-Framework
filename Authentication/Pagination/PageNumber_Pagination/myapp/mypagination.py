from rest_framework.pagination import PageNumberPagination

class MyPageNumberPagination(PageNumberPagination):

    # page_size helps to how many records in per page
    page_size = 4   
    page_query_param = 'ds'

    # If client wants to see how many records appear in per page
    # pattern :--- http://127.0.0.1:8000/studentapi/?ds=1&records=10
    page_size_query_param = 'records'

    # This feature makes limit on maximum records in per page
    # So,client get max only 7 records
    max_page_size = 7
    
    # This feature helps to jump to the last page by writing this:
    # http://127.0.0.1:8000/studentapi/?ds=end
    # This last_page_strings = 'end' override the 'last' keyword 
    last_page_strings = 'end'