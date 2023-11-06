from django.shortcuts import render, redirect, get_object_or_404 # 追加
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Avg
from django.core.paginator import Paginator
from django.http import JsonResponse # 追加


from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)
from .models import Post, Review, PostLike
from .consts import ITEM_PER_PAGE
'''
def logout_view(request):
    logout(request)
    return redirect('accounts/login')

def index_view(request):
    #object_list = Post.objects.order_by('category')
    object_list = Post.objects.order_by('-id')
    ranking_list = Post.objects.annotate(avg_rating=Avg('review__rate')).order_by('-avg_rating')

    paginator = Paginator(ranking_list, ITEM_PER_PAGE)
    page_number = request.GET.get('page',1)
    page_obj = paginator.page(page_number)

    return render(
        request,
        'post/index.html',
        {'post_list': object_list, 'ranking_list': ranking_list, 'page_obj':page_obj },
    )
'''


class ListPostView(LoginRequiredMixin, ListView):
    template_name = 'post/post_list.html'
    model = Post
    paginate_by = ITEM_PER_PAGE

    # 検索フォーム
    def get_queryset(self): # 検索機能のために追加
        query = self.request.GET.get('query')
        #query="鎌倉"

        if query:
            post_list = Post.objects.filter(title__icontains=query)
        else:
            post_list = Post.objects.all()
        return post_list

    #いいね機能
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        for item in self.object_list:
            if item.postlike_set.filter(user_id=self.request.user).exists():
                context['is_user_liked'] = True
            else:
                context['is_user_liked'] = False

        return context


def postlike(request):
    post_pk = request.POST.get('post_pk')
    context = {
        'user_id': f'{ request.user }',
    }
    post = get_object_or_404(Post, pk=post_pk)
    like = PostLike.objects.filter(target=post, user_id=request.user)

    if like.exists():
        like.delete()
        context['method'] = 'delete'
    else:
        like.create(target=post, user_id=request.user)
        context['method'] = 'create'

    return JsonResponse(context)


class DetailPostView(LoginRequiredMixin, DetailView):
    template_name = 'post/post_detail.html'
    model = Post

    #いいね機能
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.object.postlike_set.filter(user_id=self.request.user).exists():
            context['is_user_liked'] = True
        else:
            context['is_user_liked'] = False

        return context

class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = 'post/post_create.html'
    model = Post
    fields = ('name', 'address', 'category')
    success_url = reverse_lazy('list-post')

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)


class DeletePostView(LoginRequiredMixin, DeleteView):
    template_name = 'post/post_confirm_delete.html'
    model = Post
    success_url = reverse_lazy('list-post')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied

        return obj

class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ('name', 'address', 'category')
    template_name = 'post/post_update.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied

        return obj

    def get_success_url(self):
        return reverse('detail-post', kwargs={'pk': self.object.id})

class CreateReviewView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ('post', 'title', 'text', 'rate')
    template_name = 'post/review_form1.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk=self.kwargs['post_id'])
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detail-post', kwargs={'pk': self.object.post.id})

def like(request):
        return render(request, 'post/postlike.html')

def move_to_mypage(request):
        return render(request, 'mypage.html')

def move_to_itinerary(request):
        return render(request, 'itinerary.html')

def topA(request):
    return render(request, 'topA.html')

def topB(request):
    return render(request, 'topB.html')

def selection(request):
        return render(request, 'selection.html')

def move_to_record(request):
        return render(request, 'record.html')

def move_to_traveling(request):
        return render(request, 'traveling.html')

def map_restaurant(request):
        return render(request, 'map_restaurant.html')
