import plotly.express as px
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
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


@login_required
def report_delete_view(request, pk):
    report = Report.objects.get(pk=pk)
    report.delete()
    return redirect("report-list")


@login_required
def report_list_view(request):
    reports = Report.objects.all()
    paginator = Paginator(reports, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    fig = px.line(
        x=[t.time for t in page_obj],
        y=[temp.temp for temp in page_obj],
        labels={"x": "Time of day", "y": "Temperature"},
    )

    chart = fig.to_html(full_html=False)
    context = {"page_obj": page_obj, "form": ReportForm(), "chart": chart}
    return render(request, "reports/report_list.html", context)


class ReportCreateView(LoginRequiredMixin, CreateView):
    model = Report
    form_class = ReportForm
    success_url = reverse_lazy("report-list")


class ReportUpdateView(LoginRequiredMixin, UpdateView):
    model = Report
    fields = "__all__"


class ReportDetailView(LoginRequiredMixin, DetailView):
    model = Report
