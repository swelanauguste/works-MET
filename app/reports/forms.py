from django import forms

from .models import Report


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = "__all__"
        exclude = ['archive']
        widgets = {
            "time": forms.TimeInput(),
            "date": forms.DateInput(attrs={"type": "date"}),
            "rr_time": forms.TimeInput(),
        }
        labels = {
            'st': 'st',
            'date': 'date',
            'time': 'time',
            'vis': 'vis',
            't_cld': 't_cld',
            'dd': 'dd',
            'fff': 'fff',
            'temp': 'temp',
            'dp': 'dp',
            # 'vp': 'vp',
            'rh': 'rh',
            'msl': 'msl',
            'qnh': 'qnh',
            'w': 'w',
            'ww': 'ww',
            't_lcld': 't_lcld',
            'cld': 'cld',
            'low': 'low',
            'mid': 'mid',
            'high': 'high',
            'high2': 'high2',
            'max': 'max',
            'min': 'min',
            'rr': 'rr',
            'rr_time': 'rr_time',
        }
