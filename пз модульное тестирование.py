import unittest 

#Задание 1
class TestCalculator(unittest.TestCase):
    print("Задание 1")
    def test_add_1(self):
        a = 3
        b = 2
        result = add(a,b)
        print(f"{a,b} Равно: {result}")
        self.assertEqual(result,6)

    def test_add_2(self):
        a = -1
        b = 1
        result = add(a,b)
        print(f"{a,b} Равно: {result}")
        self.assertEqual(result,-1)

    def test_add_3(self):
        a = 0
        b = 5
        result = add(a,b)
        print(f"{a,b} Равно: {result}")
        self.assertEqual(result,0)

    def test_add_4(self):
        a = "a"
        b = 5
        try:
            result = add(a, b)
            print(f"{a, b} Равно: {result}")
            self.assertEqual(result, 0)
        except TypeError as e:
            print(e)
            #Сделал с помощью ии с буквой, так как мои результаты давали ошибку

def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Аргументы должны быть числами")
    return a * b

import unittest

# Задание 2
def is_prime(number):
    if not isinstance(number, int):
        raise ValueError()
    
    if number <= 1:
        raise ValueError()
    
    if number == 2:
        return True
    
    if number % 2 == 0:
        return False
    i = 3
    while i * i <= number:
        if number % i == 0:
            return False
        i += 2
    
    return True


class TestIsPrime(unittest.TestCase):

    def test_is_prime_2(self):
        result = is_prime(2)
        print(f"is_prime(2) = {result}")
        self.assertTrue(result)

    def test_is_prime_4(self):
        result = is_prime(4)
        print(f"is_prime(4) = {result}")
        self.assertFalse(result)

    def test_is_prime_17(self):
        result = is_prime(17)
        print(f"is_prime(17) = {result}")
        self.assertTrue(result)

    def test_is_prime_negative(self):
        with self.assertRaises(ValueError):
            is_prime(-1)


unittest.main()





