# -*- coding: utf-8 -*-

import unittest

from lantz.core import Driver, Feat, DictFeat, Action, ureg
from lantz.core import mfeats
from lantz.sims import wrap_driver_cls


class TestClass(Driver):

    # Feat

    @Feat
    def feat_both(self):
        raise Exception('Should not be here')

    @feat_both.setter
    def feat_both(self, value):
        raise Exception('Should not be here')

    @Feat
    def feat_only_get(self):
        raise Exception('Should not be here')

    feat_only_set = Feat()

    @feat_only_set.setter
    def feat_only_set(self, value):
        raise Exception('Should not be here')

    # Feat

    @Feat(units='Hz')
    def ufeat_both(self):
        raise Exception('Should not be here')

    @ufeat_both.setter
    def ufeat_both(self, value):
        raise Exception('Should not be here')


    # DictFeat

    @DictFeat
    def dfeat_both(self, key):
        raise Exception('Should not be here')

    @dfeat_both.setter
    def dfeat_both(self, key, value):
        raise Exception('Should not be here')

    @DictFeat
    def dfeat_only_get(self, key):
        raise Exception('Should not be here')

    dfeat_only_set = Feat()

    @dfeat_only_set.setter
    def dfeat_only_set(self, key, value):
        raise Exception('Should not be here')


class TestMClass(Driver):

    mintfeat = mfeats.IntFeat('bla', 'bla {}')

    mintdfeat = mfeats.IntDictFeat('bla {key}', 'bla {key} {value}', keys={'a', 'b'})


class TestAClass(Driver):

    @Action()
    def myaction(self, value):
        raise Exception('Should not be here')

    @Action()
    def myotheraction(self, value):
        raise Exception('Should not be here')


S = wrap_driver_cls(TestClass, dict(feat_both=1, feat_only_get=2, feat_only_set=3,
                                    dfeat_both=dict(a=1), dfeat_only_get=dict(b=2), dfeat_only_set=dict(c=3),
                                    ufeat_both=1))

T = wrap_driver_cls(TestMClass)

TO = wrap_driver_cls(TestMClass, dict(mintfeat=1, mintdfeat=dict(a=1)))


U = wrap_driver_cls(TestAClass, dict(myaction=42))


class TestSimWrapper(unittest.TestCase):

    def test_feat(self):
        x = S()
        x.initialize()
        self.assertEqual(x.feat_both, 1)
        self.assertEqual(x.feat_only_get, 2)
        with self.assertRaises(AttributeError):
            print(x.feat_only_set)

        x.feat_both = 2
        self.assertEqual(x.feat_both, 2)

        self.assertEqual(x.ufeat_both, 1 * ureg.Hz)

        self.assertEqual(x.dfeat_both['a'], 1)
        self.assertEqual(x.dfeat_only_get['b'], 2)
        with self.assertRaises(AttributeError):
            print(x.dfeat_only_set['c'])

        x.dfeat_both['a'] = 2
        self.assertEqual(x.dfeat_both['a'], 2)

    def test_instance_independence(self):
        x1 = S()
        x1.initialize()
        x2 = S()
        x2.initialize()

        self.assertEqual(x1.feat_both, 1)
        self.assertEqual(x2.feat_both, 1)
        x2.feat_both = 2
        self.assertEqual(x1.feat_both, 1)
        self.assertEqual(x2.feat_both, 2)

        self.assertEqual(x1.dfeat_both['a'], 1)
        self.assertEqual(x2.dfeat_both['a'], 1)
        x2.dfeat_both['a'] = 2
        self.assertEqual(x1.dfeat_both['a'], 1)
        self.assertEqual(x2.dfeat_both['a'], 2)

    def test_mfeat(self):
        x1 = T()
        x1.initialize()
        self.assertEqual(x1.mintfeat, 0)
        self.assertEqual(x1.mintdfeat['a'], 0)

    def test_override_mfeat(self):
        x1 = TO()
        x1.initialize()
        self.assertEqual(x1.mintfeat, 1)
        self.assertEqual(x1.mintdfeat['a'], 1)

    def test_action(self):
        x1 = U()
        x1.initialize()
        out = x1.myaction(0)
        self.assertEqual(out, 42)

        with self.assertRaises(Exception):
            print(x1.myotheraction(0))


if __name__ == '__main__':
    unittest.main()
