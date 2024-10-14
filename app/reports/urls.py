from django.urls import path

from .views import (
    ReportCreateView,
    ReportDetailView,
    ReportListView,
    ReportUpdateView,
    report_delete_view,
)

urlpatterns = [
    path("", ReportListView.as_view(), name="report-list"),
    path("create/", ReportCreateView.as_view(), name="report-create"),
    path("detail/<int:pk>/", ReportDetailView.as_view(), name="report-detail"),
    path("delete/<int:pk>/", report_delete_view, name="report-delete"),
    path("update/<int:pk>/", ReportUpdateView.as_view(), name="report-update"),
]
