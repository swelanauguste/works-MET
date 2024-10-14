from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import ReportForm
from .models import Report


def report_delete_view(request, pk):
    report = Report.objects.get(pk=pk)
    report.delete()
    return redirect("report-list")


class ReportListView(ListView):
    model = Report
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ReportForm()  # add form to context
        return context

    # ordering = ["-date_time"]


class ReportCreateView(CreateView):
    model = Report
    form_class = ReportForm
    success_url = reverse_lazy("report-list")


class ReportUpdateView(UpdateView):
    model = Report
    fields = "__all__"


class ReportDetailView(DetailView):
    model = Report
