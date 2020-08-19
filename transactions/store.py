from collections import defaultdict, deque

class Transaction(object):
    def __init__(self, **kwargs):
        self.tx_id = kwargs.get('tx_id', 0)
        self.amount = kwargs.get('amount', 0)
        self.kind = kwargs.get('kind', 'default')
        self.parent = kwargs.get('parent', None)
        self.children = kwargs.get('children', [])

class TransactionStore(object):
    def __init__(self):
        self.transactions = {}
        self.kinds = defaultdict(list)

    def get_transaction_by_id(self, tx_id):
        if tx_id in self.transactions:
            return self.transactions[tx_id]
        return None

    def get_all_by_kind(self, kind):
        if kind in self.kinds:
            return self.kinds[kind.lower()]
        return []

    def get_transitive_sum(self, tx_id):
        total = 0
        queue = deque([tx_id])

        while queue:
            cur = queue.popleft()
            transaction = self.get_transaction_by_id(cur)
            if not transaction:
                continue
            total += transaction.amount
            queue.extend(transaction.children)

        return total

    def create_transaction(self, tx_id, amount, kind, parent):
        parent_tx = None
        if parent:
            parent_tx = self.get_transaction(parent)
            if not parent_tx:
                raise Exception('Invalid parent id')

        transaction = Transaction(tx_id=tx_id, amount=amount, kind=kind, parent=parent)
        self.transactions[tx_id] = transaction
        self.kinds[kind.lower()].append(tx_id)
        if parent_tx:
            parent_tx.children.append(tx_id)

transaction_store = TransactionStore()


