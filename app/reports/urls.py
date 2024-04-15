from django.urls import path

from .views import ReportCreateView, ReportDetailView, ReportListView, ReportUpdateView

urlpatterns = [
    path("", ReportListView.as_view(), name="report-list"),
    path("create/", ReportCreateView.as_view(), name="report-create"),
    path("<int:pk>/", ReportDetailView.as_view(), name="report-detail"),
    path("<int:pk>/update/", ReportUpdateView.as_view(), name="report-update"),
]
