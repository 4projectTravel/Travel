from django.views import generic
from .models import AddressCategory, GenreCategory, AddressGenre
from django.shortcuts import render
from .forms import GenreSearchForm, AddressSearchForm


class AddressGenreList(generic.ListView):
    template_name = 'spot/AddressGenre_list.html'
    model = AddressGenre
    #ordering = '-like'

    # 追加
    def get_queryset(self):
        queryset = super().get_queryset()
        self.form = form_1 = GenreSearchForm(self.request.GET or None)
        self.form = form_2 = AddressSearchForm(self.request.GET or None)

        if (form_1.is_valid()) and (form_2.is_valid()):
            genre = form_1.cleaned_data.get('genre')
            address = form_2.cleaned_data.get('address')
            addressgenre = genre + address
            if addressgenre:
                queryset = queryset.filter(genre=genre).filter(address=address)
                #queryset = queryset.filter(category_genre=category_genre)
                #queryset = queryset.filter(category_genre=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # search formを渡す
        context['search_form_addressgenre'] = self.form

        return context
"""
    def get_queryset(self):
        queryset = super().get_queryset()
        self.form = form = AddressSearchForm(self.request.GET or None)

        if form.is_valid():
            address = form.cleaned_data.get('address')
            if address:
                queryset = queryset.filter(address=address)
                #queryset = queryset.filter(category_genre=category_genre)
                #queryset = queryset.filter(category_genre=category)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # search formを渡す
        context['search_form_address'] = self.form

        return context
"""
