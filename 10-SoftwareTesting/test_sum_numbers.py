import unittest

from sum_numbers import sum_even


class TestSumEven(unittest.TestCase):
    def test_sum_even(self):
        # Testuj sumę liczb naturalnych parzystych 
        # z dowolnego przedziału m,n
        m = 1
        n = 5
        result = sum_even(m,n)
        self.assertEqual(result, 6)

    def test_sum_even_fromeven(self):
        # Testuj sumę liczb naturalnych parzystych 
        # z przedziału m,n, gdzie m parzyste
        m = 2
        n = 5
        result = sum_even(m,n)
        self.assertEqual(result, 6)

    def test_sum_even_nm(self):
        # Testuj sumę liczb naturalnych parzystych 
        # z przedziału m,n, gdzie n<m
        m = 5
        n = 2
        result = sum_even(m,n)
        self.assertEqual(result, 0)
        
    def test_sum_even_mmnijsze(self):
        #obliczanie sumy liczb naturalnych parzystych z przedziału <m,n>, gdy m<0
        m = -20
        n = 5
        result = sum_even(m,n)
        self.assertEqual(result, 6)
        
    def test_sum_even_rzeczywisty(self):
        #obliczanie sumy gdy m i/lub n są liczbami rzeczywistymi
        m = 2.1234
        n = 5.234
        ressult = sum_even(m,n)
        self.assertEqual(result, )       

if __name__ == '__main__':
    unittest.main()