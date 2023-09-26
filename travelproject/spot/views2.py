from django.shortcuts import render
from django.views import generic
from .models import Genre, Address, GenreCategory, AddressCategory
from .forms import GenreSearchForm, AddressSearchForm


class GenreList(generic.ListView):
    template_name = 'spot/genre_list.html'
    model = Genre
    #ordering = '-like'

    # 追加
    def get_queryset(self):
        queryset = super().get_queryset()
        self.form = form = GenreSearchForm(self.request.GET or None)

        if form.is_valid():

            # カテゴリでの絞り込み
            category_genre = form.cleaned_data.get('category_genre')
            if category_genre:
                queryset = queryset.filter(category_genre=category_genre).filter()
                #queryset = queryset.filter(category_genre=category_genre)
                #queryset = queryset.filter(category_genre=category)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # search formを渡す
        context['search_form_genre'] = self.form

        return context

class AddressList(generic.ListView):
    #template_name = 'spot/address_list.html'
    template_name = 'spot/genre_list.html'
    model = Address

    # 追加
    def get_queryset(self):
        queryset = super().get_queryset()
        self.form = form = AddressSearchForm(self.request.GET or None)

        if form.is_valid():

            # カテゴリでの絞り込み
            #category_address = form.cleaned_data.get('category_address')
            category_address = form.cleaned_data.get('category_address')
            #if category_address:
                #queryset = queryset.filter(category_address=category_address)
            if category_address:
                queryset = queryset.filter(category_address=category_address)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # search formを渡す
        #context['search_form_address'] = self.form
        context['search_form_address'] = self.form

        return context
