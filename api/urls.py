from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt

from api.views import *

urlpatterns = [

	re_path("provider/((?P<pk>\d+)/)?", csrf_exempt(ProviderView.as_view())),
	re_path("customer/((?P<pk>\d+)/)?", csrf_exempt(CustomerView.as_view())),
	re_path("scale/((?P<pk>\d+)/)?", csrf_exempt(ScaleView.as_view())),
	re_path("smartedgesensor/((?P<pk>\d+)/)?", csrf_exempt(SmartEdgeSensorView.as_view())),
	re_path("totemove/((?P<pk>\d+)/)?", csrf_exempt(ToteMoveView.as_view())),
	re_path("scaleentry/((?P<pk>\d+)/)?", csrf_exempt(ScaleEntryView.as_view())),
	re_path("haulentry/((?P<pk>\d+)/)?", csrf_exempt(HaulEntryView.as_view())),
	re_path("ledger/((?P<pk>\d+)/)?", csrf_exempt(LedgerEntryView.as_view())),
	re_path("logisticsstate/((?P<pk>\d+)/)?", csrf_exempt(LogisistcsStateView.as_view())),
]