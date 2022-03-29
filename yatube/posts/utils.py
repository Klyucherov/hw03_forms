from django.core.paginator import Paginator

from yatube.settings import COUNT_POST


def get_page_context(post_list, request):
    paginator = Paginator(post_list, COUNT_POST)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj
