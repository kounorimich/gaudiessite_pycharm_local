from django.db import models
from posts.models import Post


class TopIndexPattern(models.Model):
    posts = Post.objects.order_by("-pk")
    choice_tuples_list = []
    for post in posts:
        choice_tuples_list.append((str(post.pk), post.title))
        # strがないと、管理サイトでプルダウンで選ぶ際に「候補がありません」というエラーが出る、、、

    fixed_post = models.TextField(verbose_name="トップ画面に固定するポスト", choices=choice_tuples_list)



