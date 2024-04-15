from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy
from .forms import ReportForm
from .models import Report


class ReportListView(ListView):
    model = Report

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ReportForm()  # add form to context
        return context

    # ordering = ["-date_time"]


class ReportCreateView(CreateView):
    model = Report
    form_class = ReportForm
    success_url = reverse_lazy('report-list')


class ReportUpdateView(UpdateView):
    model = Report
    fields = "__all__"


class ReportDetailView(DetailView):
    model = Report
