import fibonacci
import unittest


class TestFib(unittest.TestCase) :

    def test_series(self) :
        expected_result = [1, 1, 2, 3, 5, 8]
        test_result = fibonacci.fib(10)
        self.assertEqual(expected_result, test_result)
        print(expected_result)

    def test_series_1(self) :
        expected_result = [1, 1, 2, 3, 5, 8, 13, 21, 34]
        test_result = fibonacci.fib(50)
        self.assertEqual(expected_result, test_result)
        print(expected_result)

    def test_series_2(self) :
        expected_result = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        test_result = fibonacci.fib(100)
        self.assertEqual(expected_result, test_result)
        print(expected_result)

    def test_series_3(self) :
        expected_result = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
                           144, 233, 377, 610, 987]
        test_result = fibonacci.fib(1000)
        self.assertEqual(expected_result, test_result)
        print(expected_result)


if __name__ == '__main__' : unittest.main()
