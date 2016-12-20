import unittest


class Train(object):
    def __init__(self, config):
        self._str = config


class TrainTest(unittest.TestCase):
    
    def test_passenger_train(self):
        train = Train("HPP")
        self.assertEqual("<HHHH::|OOOO|::|OOOO|", train.print())

    def test_restaurant_train(self):
        train = Train("HPRP")
        self.assertEquals("<HHHH::|OOOO|::|hThT|::|OOOO|", train.print())

    def test_double_headed_train(self):
        train = Train("HPRPH")
        self.assertEquals("<HHHH::|OOOO|::|hThT|::|OOOO|::HHHH>", train.print())

    def test_modify_train(self):
        train = Train("HPRPH")
        train.detachEnd()
        self.assertEquals("<HHHH::|OOOO|::|hThT|::|OOOO|", train.print())
        train.detachHead()
        self.assertEquals("|OOOO|::|hThT|::|OOOO|", train.print())

    def test_cargo_train(self):
        train = Train("HCCC")
        self.assertEquals("<HHHH::|____|::|____|::|____|", train.print())
        train.fill()
        self.assertEquals("<HHHH::|^^^^|::|____|::|____|", train.print())
        train.fill()
        self.assertEquals("<HHHH::|^^^^|::|^^^^|::|____|", train.print())
        train.fill()
        self.assertEquals("<HHHH::|^^^^|::|^^^^|::|^^^^|", train.print())
        self.assertFalse(train.fill())

    def test_mixed_train(self):
        train = Train("HPCPC")
        self.assertEquals("<HHHH::|OOOO|::|____|::|OOOO|::|____|", train.print())
        train.fill()
        self.assertEquals("<HHHH::|OOOO|::|^^^^|::|OOOO|::|____|", train.print())
        train.fill()
        self.assertEquals("<HHHH::|OOOO|::|^^^^|::|OOOO|::|^^^^|", train.print())
        self.assertFalse(train.fill())

if __name__ == '__main__':
    unittest.main()
