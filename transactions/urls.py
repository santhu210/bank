from django.urls import include, path
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from transactions.api.record import RecordTransaction
from transactions.api.list import TransactionList
from transactions.api.sum import TransactionSum

urlpatterns = [
    url(r'^transactions/(?P<tx_id>\d+)/', csrf_exempt(RecordTransaction.as_api_view())),
    url(r'^types/(?P<type>[a-zA-Z0-9-_]+)/', csrf_exempt(TransactionList.as_api_view())),
    url(r'^sum/(?P<tx_id>\d+)/', csrf_exempt(TransactionSum.as_api_view()))
]