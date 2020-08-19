from transactions.store import transaction_store
from transactions.api.base import ApiBase

class RecordTransaction(ApiBase):
    def __init__(self, **kwargs):
        super(RecordTransaction, self).__init__(**kwargs)

    def get_or_create(self):
        data = {}
        kwargs = self.kwargs
        self.tx_id = kwargs.get('tx_id', None)
        self.amount = self.request.POST.get('amount', None)
        self.kind = self.request.POST.get('type', None)
        self.parent_id = self.request.POST.get('parent_id', None)

        if not self.amount:
            self.set_bad_req('Amount is invalid')
            return data

        try:
            self.amount = float(self.amount)
        except:
            self.set_bad_req('Amount is invalid')
            return data

        if not self.tx_id:
            self.set_bad_req('Invalid transaction id')
            return data

        try:
            self.tx_id = int(self.tx_id)
        except:
            self.set_bad_req('Invalid transaction id')
            return data

        if self.tx_id in transaction_store.transactions:
            self.set_bad_req('Invalid transaction id, already exists')
            return data            

        if not self.kind:
            self.set_bad_req('Invalid transaction type')
            return data

        self.create_transaction()
        return data

    def create_transaction(self):
        transaction_store.create_transaction(self.tx_id, self.amount, self.kind, self.parent_id)

