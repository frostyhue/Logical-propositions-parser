if __name__ == "__main__" and __package__ is None:
    from sys import path
    from os.path import dirname as dir

    path.append(dir(path[0]))
    __package__ = "examples"

import unittest
import Interpreter

class TestInterpreter(unittest.TestCase):

    def test_pass(self):
        self.assertEqual(1, 1, 'Expected 1 to equal 1')

    def test_fail(self):
        self.assertEqual(1, 2, 'uh-oh')

if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestInterpreter)
    test_result = unittest.TestRunner().run(test_suite)
