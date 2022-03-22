import unittest


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def test_main(self):
        self.assertEqual(True,True)

if __name__=="__main__":
    unittest.main()