import math
import filecmp
import unittest
import sys
import time


def ceil(number):
    return math.ceil(number)


def factorial(number):
    return math.factorial(number)


def pow(x, y):
    return math.pow(x, y)


def file_compare(file1, file2):
    return filecmp.cmp(file1, file2)


class MathTest(unittest.TestCase):
    def test_ceil(self):
        self.assertEqual(ceil(100.000000000001), 101)
        self.assertEqual(ceil(999999.9), 1000000)
        self.assertEqual(ceil(1.000000000001), 2)
        self.assertEqual(ceil(float(sys.maxsize)+0.01), sys.maxsize+1)
        # ???
        # self.assertEqual(ceil((float(sys.maxsize)*-1)),
        #                 (sys.maxsize*-1))

        with self.assertRaises(OverflowError):
            ceil(float("inf"))
        with self.assertRaises(TypeError):
            ceil(None)
        with self.assertRaises(TypeError):
            ceil('test')

    def test_factorial(self):
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(10), 3628800)
        self.assertGreater(factorial(100), 10000000)
        self.assertEqual(factorial(10), 1*2*3*4*5*6*7*8*9*10)
        self.assertEqual(factorial(0), 1)
        with self.assertRaises(ValueError):
            factorial(3.1416)
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(TypeError):
            factorial(None)
        start_time = time.perf_counter()
        factorial(100000)
        duration = time.perf_counter() - start_time
        self.assertLess(duration, 1)
        self.assertGreater(factorial(100000), 1000)

    def test_pow(self):
        self.assertEqual(pow(2, 2), 4)
        self.assertEqual(pow(9, 9), 387420489)
        # ??
        self.assertEqual(pow(0, 0), 1)
        self.assertEqual(pow(0, 1), 0)
        self.assertEqual(pow(1, 0), 1)
        self.assertEqual(pow(0, 1), 0)
        self.assertEqual(pow(1, -11), 1)
        self.assertEqual(pow(2, -11), 0.00048828125)
        self.assertEqual(pow(10, 0.5), 3.1622776601683795)
        self.assertEqual(pow(0.5, 10), 0.0009765625)
        self.assertEqual(pow(27, 3), 27*27*27)
        self.assertEqual(pow(99, -4), 1/(99*99*99*99))
        self.assertEqual(pow(55, 1/2), math.sqrt(55))
        with self.assertRaises(TypeError):
            pow(10, 'a')
        with self.assertRaises(TypeError):
            pow('a', 10)

        def test_filecmp(self):
            pass

if __name__ == '__main__':
    unittest.main()
