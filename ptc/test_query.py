import unittest
from sqlalchemy_declarative import Person

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


class Test_query(unittest.TestCase):
    session = mockSession()
    session.query('')._filter(Person.name == '')._count = 0



# class Test_query(unittest.TestCase):
#     def setUp(self):
#         self._mox = mox.Mox()
#
#     def _create_session_mock(self):
#         from sqlalchemy.orm.session import Session
#         return self._mox.CreateMock(Session)
#
#     def _create_query_mock(self):
#         from sqlalchemy.orm.query import Query
#         return self._mox.CreateMock(Query)
#
#     def _create_desc_mock(self):
#         from sqlalchemy_declarative import Person
#         return self._mox.CreateMock(Person.name)
#
#
#     def tearDown(self):
#         self.mox.UnsetStubs()
#
#     def test_find_latest(self):
#         from myapp.models.repositories import PostRepository
#         from myapp.models import Post
#
#         expected_result = 'test'
#
#         session_mock = self._create_session_mock()
#         query_mock = self._create_query_mock()
#         desc_mock = self._create_desc_mock()
#
#         # Monkey patch
#         tmp = Post.date.desc
#         Post.date.desc = desc_mock
#
#         session_mock.query(Post).AndReturn(query_mock)
#         query_mock.order_by(Post.date.desc().AndReturn('test')).AndReturn(query_mock)
#         query_mock.offset(0).AndReturn(query_mock)
#         query_mock.limit(10).AndReturn(expected_result)
#
#         self._mox.ReplayAll()
#         r = PostRepository(session_mock)
#
#         result = r.find_latest()
#         self._mox.VerifyAll()
#
#         self.assertEquals(expected_result, result)
#
#         Post.date.desc = tmp
#
