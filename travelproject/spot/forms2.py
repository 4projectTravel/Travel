from django import forms
from .models import GenreCategory, AddressCategory

class AddressSearchForm(forms.Form):
    """検索フォーム"""
    # エリア検索
    #category_address = forms.ModelChoiceField(
    category_address = forms.ModelChoiceField(
        label='エリアでの絞り込み',
        required=False,
        queryset=AddressCategory.objects.order_by('name'),
        widget=forms.Select(attrs={'class': 'form'})
    )


class GenreSearchForm(forms.Form):
    """検索フォーム"""
    # カテゴリー検索
    category_genre = forms.ModelChoiceField(
        label='ジャンルでの絞り込み',
        required=False,
        queryset=GenreCategory.objects.order_by('name'),
        widget=forms.Select(attrs={'class': 'form'})
    )
