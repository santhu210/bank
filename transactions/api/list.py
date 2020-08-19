from transactions.store import transaction_store
from transactions.api.base import ApiBase

class TransactionList(ApiBase):
    def __init__(self, **kwargs):
        super(TransactionList, self).__init__(**kwargs)

    def get_or_create(self):
        self.data = {}
        
        kwargs = self.kwargs
        self.kind = kwargs.get('type', None)
        
        if not self.kind:
            self.set_bad_req('Invalid transaction type')
            return self.data

        self.get_transactions()
        return self.data

    def get_transactions(self):
        self.data = transaction_store.get_all_by_kind(self.kind)

