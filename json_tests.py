import unittest
from serializers.json_serializer import JsonSerializer
import test_examples as te

js = JsonSerializer()


class TestingObjects(unittest.TestCase):
    def tearDown(self):
        dumper = js.dumps(self.tested_obj)
        self.loader = js.loads(dumper)
        self.assertTrue(self.loader == self.tested_obj)

    def test_none(self):
        self.tested_obj = None

    def test_bool_True(self):
        self.tested_obj = True

    def test_bool_False(self):
        self.tested_obj = False

    def test_int(self):
        self.tested_obj = 1234567

    def test_float(self):
        self.tested_obj = 1.2345678

    def test_complex(self):
        self.tested_obj = complex(1, 2)

    def test_str(self):
        self.tested_obj = "aefhiawdiawohofoahiwodijawf"

    def test_list(self):
        self.tested_obj = [1, 2, 3, 4, 5]

    def test_tuple(self):
        self.tested_obj = (1, 2, 3, 4, 5)

    def test_range(self):
        self.tested_obj = range(1, 5, 1)

    def test_bytes(self):
        self.tested_obj = bytes.fromhex("d0 9f d1 80 d0 b8 d0 b2 d0 b5 d1 82")

    def test_bytearray(self):
        self.tested_obj = bytes.fromhex("d0 a2 d0 b5 d1 81 d1 82 d0 b8 d0 bc")

    def test_set(self):
        self.tested_obj = {1, 2, 3, 4, 5}

    def test_frozenset(self):
        self.tested_obj = frozenset({1, 2, 3, 4, 5})

    def test_dict(self):
        self.tested_obj = {"a": 1, "b": 2, "c": 3}


class TestingFunctions(unittest.TestCase):
    def test_func_pass(self):
        tested_obj = te.func_pass
        dumper = js.dumps(tested_obj)
        loader = js.loads(dumper)
        self.assertEqual(tested_obj.__code__, loader.__code__)
        self.assertEqual(tested_obj(), loader())

    def test_func_add_ten(self):
        tested_obj = te.func_add_ten
        dumper = js.dumps(tested_obj)
        loader = js.loads(dumper)
        self.assertEqual(tested_obj.__code__, loader.__code__)
        self.assertEqual(tested_obj(10), loader(10))

    def test_func_with_recursion(self):
        tested_obj = te.func_with_recursion
        dumper = js.dumps(tested_obj)
        loader = js.loads(dumper)
        self.assertEqual(tested_obj.__code__, loader.__code__)
        self.assertEqual(tested_obj(5), loader(5))

    def test_func_with_import(self):
        tested_obj = te.func_with_import
        dumper = js.dumps(tested_obj)
        loader = js.loads(dumper)
        self.assertEqual(tested_obj.__code__, loader.__code__)
        self.assertEqual(tested_obj(0), loader(0))

    def test_func_with_globals(self):
        tested_obj = te.func_with_globals
        dumper = js.dumps(tested_obj)
        loader = js.loads(dumper)
        self.assertEqual(tested_obj.__code__, loader.__code__)
        self.assertEqual(tested_obj(), loader())

    def test_func_with_func(self):
        tested_obj = te.func_with_func
        dumper = js.dumps(tested_obj)
        loader = js.loads(dumper)
        self.assertEqual(tested_obj.__code__, loader.__code__)
        self.assertEqual(tested_obj(), loader())

    def test_func_with_closure(self):
        tested_obj = te.func_with_closure()
        dumper = js.dumps(tested_obj)
        loader = js.loads(dumper)
        self.assertEqual(tested_obj.__code__, loader.__code__)
        self.assertEqual(
            tested_obj.__closure__[0].cell_contents, loader.__closure__[0].cell_contents
        )

    def test_func_decorator(self):
        tested_obj = te.check_decorator
        dumper = js.dumps(tested_obj)
        loader = js.loads(dumper)
        self.assertEqual(tested_obj.__code__, loader.__code__)
        self.assertEqual(tested_obj(), loader())


if __name__ == "__main__":
    unittest.main()