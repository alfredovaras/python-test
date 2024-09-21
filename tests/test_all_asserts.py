import unittest

SERVER = "server_b"

class AllAssertsTests(unittest.TestCase):

    def test_assert_equal(self):
        self.assertEqual(10,10)
        self.assertEqual("Hola", "Hola")

    def test_assert_true_or_false(self):
        self.assertTrue(True)
        self.assertFalse(False)

    def test_assert_raises(self):
        with self.assertRaises(ValueError):
            int("no_soy_un_numero")

    def test_assert_in(self):
        self.assertIn(1, [1,2,3,4,5])
        #self.assertIn("hola", "Hola mundo")
        self.assertNotIn(6, [1,2,3,4,5])

    def test_assert_dicts(self):
        self.assertDictEqual(
            {"a":1, "b":2},
            {"a":1, "b":2}
            )
        self.assertSetEqual(
            {1,2,3},
            {3,2,1}
            )

    @unittest.skip("trabajo en progreso, será habilitada nuevamente")
    def test_skip(self):
        self.assertEqual("Hola", "Chao")

    @unittest.skipIf(SERVER == "server_b", "saltado porque no estamos en el servidor")
    def test_skipif(self):
        self.assertEqual("Hola", "Chao")

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(100,50)
