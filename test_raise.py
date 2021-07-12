import unittest
import Sotrudnik


class TestRaise(unittest.TestCase):
    def setUp(self):
        first = 'roma'
        last = 'hatkev'
        pay = ''

        self.createobj = Sotrudnik.Employee(first, last, pay)

    def test_give_dflt(self):
        self.createobj.give_raise()
