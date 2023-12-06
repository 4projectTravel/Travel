from django import forms
from django.contrib.admin.widgets import AdminDateWidget    #インポート
from .models import Itinerary, Review
from django.forms import ModelForm





class DateInput(forms.DateInput):
    input_type = 'date'

class AddItineraryForm(forms.ModelForm):
    class Meta:
        model = Itinerary
        fields = ('title','date_1','date_2','date_3','time_1','time_2','time_3','time_4','time_5','time_6','time_7','time_8','time_9','time_10','time_11','time_12',
    'schedule_1','schedule_2','schedule_3','schedule_4','schedule_5','schedule_6','schedule_7','schedule_8','schedule_9','schedule_10','schedule_11','schedule_12','category','contributer','companion')
        widgets = {
            'title':forms.Textarea(attrs={'cols': '50', 'rows': '1'}),
            'date_1':DateInput(),
            'date_2':DateInput(),
            'date_3':DateInput(),

            'time_1':forms.TimeInput(format='%H:%M'),
            'time_2':forms.TimeInput(format='%H:%M'),
            'time_3':forms.TimeInput(format='%H:%M'),
            'time_4':forms.TimeInput(format='%H:%M'),
            'time_5':forms.TimeInput(format='%H:%M'),
            'time_6':forms.TimeInput(format='%H:%M'),
            'time_7':forms.TimeInput(format='%H:%M'),
            'time_8':forms.TimeInput(format='%H:%M'),
            'time_9':forms.TimeInput(format='%H:%M'),
            'time_10':forms.TimeInput(format='%H:%M'),
            'time_11':forms.TimeInput(format='%H:%M'),
            'time_12':forms.TimeInput(format='%H:%M'),

            'schedule_1':forms.Textarea(attrs={'cols': '50', 'rows': '2'}),
            'schedule_2':forms.Textarea(attrs={'cols': '50', 'rows': '2'}),
            'schedule_3':forms.Textarea(attrs={'cols': '50', 'rows': '2'}),
            'schedule_4':forms.Textarea(attrs={'cols': '50', 'rows': '2'}),
            'schedule_5':forms.Textarea(attrs={'cols': '50', 'rows': '2'}),
            'schedule_6':forms.Textarea(attrs={'cols': '50', 'rows': '2'}),
            'schedule_7':forms.Textarea(attrs={'cols': '50', 'rows': '2'}),
            'schedule_8':forms.Textarea(attrs={'cols': '50', 'rows': '2'}),
            'schedule_9':forms.Textarea(attrs={'cols': '50', 'rows': '2'}),
            'schedule_10':forms.Textarea(attrs={'cols': '50', 'rows': '2'}),
            'schedule_11':forms.Textarea(attrs={'cols': '50', 'rows': '2'}),
            'schedule_12':forms.Textarea(attrs={'cols': '50', 'rows': '2'}),

            #'category':forms.Chararea(max_length=100),
            #'contributer':forms.Chararea(max_length=50),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('itinerary', 'title', 'text', 'rate_1', 'rate_2', 'record')
