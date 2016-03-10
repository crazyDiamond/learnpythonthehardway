class mockFilter(object): #This is the ONE parameter constructor
    def __init__(self):
        self._count = 0
        self._first = object()

    def first(self):  #This is the another method that's just coming along for the ride.
        return self._first

    def count(self):  #This is the needed Count method
        return self._count

class mockQuery(object): #This is the ONE parameter constructor
    def __init__(self):
        self._filter = mockFilter()

    def filter(self, placeHolder): #This is used to mimic the query.filter() call
        return self._filter

class mockSession(object):
    def __init__(self):
        self._query = mockQuery()
        self.dirty = []

    def flush(self):
        pass

    def query(self, placeHolder):  #This is used to mimic the session.query call
        return self._query

