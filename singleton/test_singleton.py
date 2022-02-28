import unittest

from singleton_allocator import SingletonClass


class TestSingleton(unittest.TestCase):
    def setUp(self):
        self.singleton = SingletonClass()
        self.new_singleton = SingletonClass()

    def test_singleton(self):
        self.assertIs(self.singleton, self.new_singleton)
        self.singleton.variable = "Singleton Variable"
        self.assertEqual(self.new_singleton.variable, "Singleton Variable")


if __name__ == "__main__":
    unittest.main()
