# akiyokoさんの言う通り、クラスベースでビューを作ってみよう！！
from django.shortcuts import render
from django.views.generic.base import TemplateView, View
from datetime import datetime
from .models import Post


# class IndexView(TemplateView):
'''TemplateViewを使った書き方'''
#
#     template_name = 'posts/index.html'
#     def get_context_data(self, **kwargs):
#         context = super(IndexView, self).get_context_data(**kwargs)
#         context['now'] = datetime.now()
#         return context
#
# index = IndexView.as_view()


class PostsIndexView(View):
    '''Viewを使った書き方'''
    def get(self, request, *args, **kwargs):
        context = {
            'posts': Post.objects.order_by('-pk')
        }
        return render(request, 'posts/index.html', context)


index = PostsIndexView.as_view()

