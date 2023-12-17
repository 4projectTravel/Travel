from django.shortcuts import render, redirect, get_object_or_404 # 追加
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Avg
from django.core.paginator import Paginator
from django.http import JsonResponse # 追加

from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)
from .models import Post2, Review2, PostLike2, Category
from .consts import ITEM_PER_PAGE



class ListPost2View(LoginRequiredMixin, ListView):
    template_name = 'post2/post_list.html'
    model = Post2
    paginate_by = ITEM_PER_PAGE


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 投稿に対するいいねの数
        for item in self.object_list:
            like_count = item.postlike2_set.count()
            context['like_count'] = like_count

        for item in self.object_list:
            if item.postlike2_set.filter(user_id=self.request.user).exists():
                context['is_user_liked'] = True
            else:
                context['is_user_liked'] = False
        return context

    #いいね機能
def postlike2(request):
    post_pk = request.POST.get('post2_pk')
    context = {
        'user_id': f'{ request.user }',
    }
    post = get_object_or_404(Post2, pk=post2_pk)
    like = PostLike2.objects.filter(target=post, user_id=request.user)

    if like.exists():
        like.delete()
        context['method'] = 'delete'
    else:
        like.create(target=post, user_id=request.user)
        context['method'] = 'create'

    context['like_count'] = post.postlike2_set.count()

    return JsonResponse(context)


class ListLikePostView(LoginRequiredMixin, ListView):
    template_name = 'post2/likepost_list.html'
    model = PostLike2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        like_count = self.object_list.count()
        context['like_count'] = like_count
        return context




class DetailPost2View(LoginRequiredMixin, DetailView):
    template_name = 'post2/post_detail.html'
    model = Post2


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post2_list = Post2.objects.filter(post2_id=self.kwargs['pk']) # pkを指定してデータを絞り込む
        context['post2_list'] = post2_list
        return context

    #いいね機能
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 投稿に対するいいねの数
        like_count = self.object.postlike2_set.count()
        context['like_count'] = like_count

        if self.object.postlike2_set.filter(user_id=self.request.user).exists():
            context['is_user_liked'] = True
        else:
            context['is_user_liked'] = False

        return context

class CreatePost2View(LoginRequiredMixin, CreateView):
    template_name = 'post2/post_create.html'
    model = Post2
    fields = ('name', 'address', 'category', 'thumbnail')
    success_url = reverse_lazy('list-post2')

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)


class CreateReview2View(LoginRequiredMixin, CreateView):
    model = Review2
    fields = ('post2', 'title', 'text', 'rate')
    template_name = 'post2/review_form1.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post2'] = Post2.objects.get(pk=self.kwargs['post2_id'])
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detail-post2', kwargs={'pk': self.object.post2.id})

def like(request):
        return render(request, 'post2/postlike.html')

def move_to_itinerary(request):
        return render(request, 'itinerary.html')

def topA(request):
    return render(request, 'topA.html')


def move_to_mypage_top(request):
        return render(request, 'mypage_top.html')

def move_to_traveling(request):
        return render(request, 'traveling.html')
