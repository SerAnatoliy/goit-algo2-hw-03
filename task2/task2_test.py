import timeit
import unittest

from BTrees import OOBTree

from task2 import load_data_from_csv, add_item, range_query, DATA_URL


class TestBenchmark(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = load_data_from_csv(DATA_URL)

        cls.tree = OOBTree()
        cls.dictionary = {}

        for item in cls.data:
            add_item(cls.tree, item)
            add_item(cls.dictionary, item)

    def test_range_query(self):
        min_price = 100
        max_price = 300

        tree_results = range_query(self.tree, min_price, max_price)
        self.assertTrue(len(tree_results) > 0, "OOBTree query returned no results")

        dict_results = range_query(self.dictionary, min_price, max_price)
        self.assertTrue(len(dict_results) > 0, "Dict query returned no results")

        self.assertEqual(len(tree_results), len(dict_results), "Different number of results")

    def test_range_query_performance(self):
        min_price = 100
        max_price = 300

        tree_time = timeit.timeit(
            lambda: range_query(self.tree, min_price, max_price),
            number=100,
        )

        dict_time = timeit.timeit(
            lambda: range_query(self.dictionary, min_price, max_price),
            number=100,
        )

        print(f"Total range_query time for OOBTree: {tree_time:.6f} seconds")
        print(f"Total range_query time for Dict: {dict_time:.6f} seconds")

        self.assert_


if __name__ == "__main__":
    unittest.main()