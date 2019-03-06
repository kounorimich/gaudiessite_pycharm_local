# from django.shortcuts import render #get_object_or_404
# from datetime import datetime

from posts.models import Post
from top.models import TopIndexPattern
from django.views.generic import TemplateView

PK_OF_TOP_INDEX_PATTEN = 1


class TopView(TemplateView):
    template_name = 'top/index.html'

    def get_context_data(self, **kwargs):
        pattern = TopIndexPattern.objects.get(pk=PK_OF_TOP_INDEX_PATTEN)
        # TopIndexPatternはひとつだけ作成するのでいつもpk=1を指定する
        fixed_post = Post.objects.get(pk=int(pattern.fixed_post))
        context = super(TopView, self).get_context_data(**kwargs)
        context['fixed_post'] = fixed_post  # topに固定して表示するpost
        last_3_post_index_list = [0, 1, 2, 3]
        last_3_posts = []
        for v in last_3_post_index_list:
            if Post.objects.order_by("-pk")[v] == fixed_post:
                continue
            last_3_posts.append(Post.objects.order_by("-pk")[v])
            if len(last_3_posts) > 3:
                last_3_posts.pop(3)

        context['last_3_posts'] = last_3_posts

        return context


top = TopView.as_view()
