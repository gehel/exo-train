import unittest

from exo_train.train import Train


class TrainTest(unittest.TestCase):

    def test_passenger_train(self):
        train = Train("HPP")
        self.assertEqual("<HHHH::|OOOO|::|OOOO|", str(train))

    def test_restaurant_train(self):
        train = Train("HPRP")
        self.assertEquals("<HHHH::|OOOO|::|hThT|::|OOOO|", str(train))

    def test_double_headed_train(self):
        train = Train("HPRPH")
        self.assertEquals("<HHHH::|OOOO|::|hThT|::|OOOO|::HHHH>", str(train))

    def test_modify_train(self):
        train = Train("HPRPH")
        train.detachEnd()
        self.assertEquals("<HHHH::|OOOO|::|hThT|::|OOOO|", str(train))
        train.detachHead()
        self.assertEquals("|OOOO|::|hThT|::|OOOO|", str(train))

    def test_cargo_train(self):
        train = Train("HCCC")
        self.assertEquals("<HHHH::|____|::|____|::|____|", str(train))
        train.fill()
        self.assertEquals("<HHHH::|^^^^|::|____|::|____|", str(train))
        train.fill()
        self.assertEquals("<HHHH::|^^^^|::|^^^^|::|____|", str(train))
        train.fill()
        self.assertEquals("<HHHH::|^^^^|::|^^^^|::|^^^^|", str(train))
        with self.assertRaises(RuntimeError):
            train.fill()

    def test_mixed_train(self):
        train = Train("HPCPC")
        self.assertEquals("<HHHH::|OOOO|::|____|::|OOOO|::|____|", str(train))
        train.fill()
        self.assertEquals("<HHHH::|OOOO|::|^^^^|::|OOOO|::|____|", str(train))
        train.fill()
        self.assertEquals("<HHHH::|OOOO|::|^^^^|::|OOOO|::|^^^^|", str(train))
        with self.assertRaises(RuntimeError):
            train.fill()
