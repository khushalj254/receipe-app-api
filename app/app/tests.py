"""
Sample test
"""
from django.test import SimpleTestCase
from app import calc


class CalcTest(SimpleTestCase):
    """Test calc module"""

    def test_add_numbers(self):
        """test add function"""
        res = calc.add(6, 5)

        self.assertEqual(res, 11)

    def test_substract_numnbers(self):
        """test substract function"""
        res = calc.substract(10, 15)

        self.assertEqual(res, 5)
