import unittest
from multi_value_dictionary import Dictionary


class Testing(unittest.TestCase):
    def test_add(self):

        d = Dictionary()
        d.add("foo", "bar")
        d.add("baz", "fang")

    def test_keys(self):

        d = Dictionary()
        d.add('foo', 'bar')
        d.add('baz', 'bang')

        keys = d.keys()
        exp_keys = ['foo', 'baz']
        self.assertEqual(keys, exp_keys)

    def test_members(self):

        d = Dictionary()
        d.add('foo', 'bar')
        d.add('foo', 'baz')
        d.add('foo', 'baz')
        
        members = d.members('foo')
        exp_members = ['bar', 'baz']

        self.assertEqual(members, exp_members)

    def test_clear(self):
        d = Dictionary()
        d.add('foo', 'bar')
        d.add('bang', 'zip')
        d.clear()
        self.assertEqual(len(d.keys()), 0)



    def test_keyexists(self):

        d = Dictionary()
        self.assertFalse(d.keyexists('foo'))
        d.add('foo', 'bar')
        self.assertTrue(d.keyexists('foo'))

    def test_memberexists(self):
        d = Dictionary()
        self.assertFalse(d.memberexists('foo', 'bar'))
        d.add('foo', 'bar')
        self.assertTrue(d.memberexists('foo', 'bar'))
        self.assertFalse(d.memberexists('foo', 'baz'))

    def test_allmembers(self):
        d = Dictionary()
        d.add('foo', 'bar')
        d.add('foo', 'baz')
        self.assertEqual(d.allmembers(), ['bar', 'baz'])
        d.add('bang', 'bar')
        d.add('bang', 'baz')
        self.assertEqual(d.allmembers(), ['bar', 'baz', 'bar', 'baz'])

    def test_items(self):
        d = Dictionary()
        d.items()

        





if __name__ == '__main__':
    unittest.main()