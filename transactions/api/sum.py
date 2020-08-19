from transactions.store import transaction_store
from transactions.api.base import ApiBase

class TransactionSum(ApiBase):
    def __init__(self, **kwargs):
        super(TransactionSum, self).__init__(**kwargs)

    def get_or_create(self):
        self.data = {}

        kwargs = self.kwargs
        self.tx_id = kwargs.get('tx_id', None)
        if not self.tx_id:
            self.set_bad_req('Invalid transaction id')
            return self.data

        try:
            self.tx_id = int(self.tx_id)
        except:
            self.set_bad_req('Invalid transaction id')
            return self.data

        self.get_sum()
        return self.data

    def get_sum(self):
        total = transaction_store.get_transitive_sum(self.tx_id)
        self.data['sum'] = total

