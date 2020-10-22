import unittest

def div(ls, divisor):
    result = []
    idx = 1
    while idx < len(ls):
        result.append(ls[idx] / divisor)
        idx = idx + 1
    return result

#class Tests(unittest.TestCase):
    def test_div(self):
        result = div([6,8,12], 2)
        self.assertTrue(result == [3,4,6])

#if __name__ == '__main__':
    unittest.main()


#def div_1(ls,ls2):
    z = []
    y = 0
    for x in ls:
        for h in ls2:
            if x == h:
                z.append(x)
    return  z
#print(div_1([1,2,3,4,8,9],[11,12,13,14,8,9]))

#class Tests(unittest.TestCase):
    def test_div_1(self):
        result = div_1([1,2,3,4,8,9],[11,12,13,14,8,9])
        self.assertTrue(result == [8,9])

#if __name__ == '__main__':
    unittest.main()
def div_1(ls,ls2):
    z = []
    y = 0
    for x in ls:
        for h in ls2:
            if x == h:
                z.append(x)
    z = set(z)
    return  z
print(div_1([1,2,3,4,8,9],[11,12,13,14,8,9,8]))

class Tests(unittest.TestCase):
    def test_div_1(self):
        result = div_1([1,2,3,4,8,9],[11,12,13,14,8,9])
        self.assertTrue(result == {8,9})

if __name__ == '__main__':
    unittest.main()

