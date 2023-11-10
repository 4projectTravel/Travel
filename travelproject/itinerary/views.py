from django.shortcuts import render, redirect
from django.db import models
from django.urls import reverse, reverse_lazy
from django.views.generic import (
     ListView,
     DetailView,
     CreateView,
     UpdateView,
     DeleteView,
)
from .models import Itinerary, Review
from .forms import AddItineraryForm
from django.contrib.admin.widgets import AdminDateWidget


class ListItineraryView(ListView):
    template_name = 'itinerary/itinerary_list.html'
    model = Itinerary

    # 検索フォーム
    def get_queryset(self): # 検索機能のために追加
        query = self.request.GET.get('query')

        if query:
            itinerary_list = Itinerary.objects.filter(schedule_1__icontains=query)
            itinerary_list = Itinerary.objects.filter(schedule_2__icontains=query)
            itinerary_list = Itinerary.objects.filter(schedule_3__icontains=query)
            itinerary_list = Itinerary.objects.filter(schedule_4__icontains=query)
            itinerary_list = Itinerary.objects.filter(schedule_5__icontains=query)
            itinerary_list = Itinerary.objects.filter(schedule_6__icontains=query)
            itinerary_list = Itinerary.objects.filter(schedule_7__icontains=query)
            itinerary_list = Itinerary.objects.filter(schedule_8__icontains=query)
            itinerary_list = Itinerary.objects.filter(schedule_9__icontains=query)
            itinerary_list = Itinerary.objects.filter(schedule_10__icontains=query)
            itinerary_list = Itinerary.objects.filter(schedule_11__icontains=query)
            itinerary_list = Itinerary.objects.filter(schedule_12__icontains=query)
        else:
            itinerary_list = Itinerary.objects.all()
        return itinerary_list

    # 投稿ユーザーとログインユーザーが一致した時のみ表示する。
    def mypagefunc(request):
        object_list = Itinerary.objects.all()
        return render(request, 'itinerary_list.html', {'object_list': object_list})

class ListItineraryAllView(ListView):
     template_name = 'itinerary/itinerary_list_all.html'
     model = Itinerary

     # 検索フォーム
     def get_queryset(self): # 検索機能のために追加
         query = self.request.GET.get('query')

         if query:
             itinerary_list = Itinerary.objects.filter(schedule_1__icontains=query)
             itinerary_list = Itinerary.objects.filter(schedule_2__icontains=query)
             itinerary_list = Itinerary.objects.filter(schedule_3__icontains=query)
             itinerary_list = Itinerary.objects.filter(schedule_4__icontains=query)
             itinerary_list = Itinerary.objects.filter(schedule_5__icontains=query)
             itinerary_list = Itinerary.objects.filter(schedule_6__icontains=query)
             itinerary_list = Itinerary.objects.filter(schedule_7__icontains=query)
             itinerary_list = Itinerary.objects.filter(schedule_8__icontains=query)
             itinerary_list = Itinerary.objects.filter(schedule_9__icontains=query)
             itinerary_list = Itinerary.objects.filter(schedule_10__icontains=query)
             itinerary_list = Itinerary.objects.filter(schedule_11__icontains=query)
             itinerary_list = Itinerary.objects.filter(schedule_12__icontains=query)
         else:
             itinerary_list = Itinerary.objects.all()
         return itinerary_list

         # 投稿ユーザーとログインユーザーが一致した時のみ表示する。
         def mypagefunc(request):
             object_list = Itinerary.objects.all()
             return render(request, 'itinerary_list_all.html', {'object_list': object_list})

class ListKamakuraItineraryAllView(ListView):
    template_name = 'itinerary/itinerary_kamakura_list_all.html'
    model = Itinerary

class DetailItineraryView(DetailView):
    template_name = 'itinerary/itinerary_detail.html'
    model = Itinerary

class DetailItineraryAllView(DetailView):
    template_name = 'itinerary/itinerary_detail_all.html'
    model = Itinerary


class CreateItineraryView(CreateView):
    template_name = 'itinerary/itinerary_create.html'
    model = Itinerary
    form_class = AddItineraryForm
    #fields = ('title','date_1','date_2','date_3','time_1','time_2','time_3','time_4','time_5','time_6','time_7','time_8','time_9','time_10','time_11','time_12',
#'schedule_1','schedule_2','schedule_3','schedule_4','schedule_5','schedule_6','schedule_7',
#'schedule_8','schedule_9','schedule_10','schedule_11','schedule_12','category','contributer')

    success_url = reverse_lazy('list-itinerary')
    widgets = {
       'date_field':AdminDateWidget(),
       #attrs={
          #'placeholder': '内容を1,024文字以内で入力してください。',
          #'rows':4, 'cols':15}),
    }

    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        #context["form"] = AddItineraryForm()
        #return context


#def CreateItineraryView(request):
    #template_name = 'itinerary/itinerary_create.html'
    #if request.POST:
        #title = request.POST["title"]
        #date = request.POST["content1"]
        #time = request.POST["content2"]
        #schedule = request.POST["content3"]
        #note = request.POST["content4"]

    #return render(request, template_name)


class UpdateItineraryView(UpdateView):
    template_name = 'itinerary/itinerary_update.html'
    model = Itinerary
    fields = ('title','date_1','date_2','date_3','time_1','time_2','time_3','time_4','time_5','time_6','time_7','time_8','time_9','time_10','time_11','time_12',
'schedule_1','schedule_2','schedule_3','schedule_4','schedule_5','schedule_6','schedule_7','schedule_8','schedule_9','schedule_10','schedule_11','schedule_12','category','contributer')

    def get_success_url(self):
        return reverse('detail-itinerary', kwargs={'pk': self.object.id})

class CreateReviewView(CreateView):
    model = Review
    fields = ('itinerary', 'title', 'text', 'rate_1', 'rate_2')
    template_name = 'itinerary/review_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['itinerary'] = Itinerary.objects.get(pk=self.kwargs['itinerary_id'])
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detail-itinerary', kwargs={'pk': self.object.itinerary.id})

class DeleteItineraryView(DeleteView):
    template_name = 'itinerary/itinerary_confirm_delete.html'
    model = Itinerary
    success_url = reverse_lazy('list-itinerary')
