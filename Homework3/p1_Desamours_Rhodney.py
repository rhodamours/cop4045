from testif import testif

class NVector(object):
    def __init__(self, *nums):
        num_list = []
        
        for num in nums:
            try:
                iter(num)
                for n in num:
                    num_list.append(n)
            except TypeError:
                num_list.append(num)
                
            self.elems = list(num_list)
    
    def __len__(self):
        return len(self.elems)
    
    def __getitem__(self, index: int):
        return self.elems[index]
    
    def __setitem__(self, index: int, value):
        self.elems[index] = value
        
    def __str__(self):
        return str(self.elems)
    
    def __eq__(self, vec: NVector):
        try:
            return self.elems == vec.elems
        except AttributeError:
            return False
        # attribute error if vector is not passed
    
    def __ne__(self, vec: NVector):
        try:
            return self.elems != vec.elems
        except AttributeError:
            return True
        # attribute error if vector is not passed
    
    def __add__(self, other):
        new_elems = []
        
        if type(other) is NVector:
            if len(self) == len(other):
                for i in range(len(self)):
                    new_elems.append(self[i] + other[i])
                    
            elif len(self) < len(other):
                for i in range(len(self)):
                    new_elems.append(self[i] + other[i])
                for i in range(len(self), len(other)):
                    new_elems.append(other[i])
                    
            elif len(self) > len(other):
                for i in range(len(other)):
                    new_elems.append(other[i] + self[i])
                for i in range(len(other), len(self)):
                    new_elems.append(self[i])
                    
        elif type(other) is int or type(other) is float:
            for elem in self.elems:
                new_elems.append(elem + other)
        
        return NVector(new_elems)
    
    def __radd__(self, other):
        return self + other
    
    def __mul__(self, other):
        result = 0
        
        if type(other) is NVector:
            if len(self) <= len(other):
                for i in range(len(self)):
                    result += self[i] * other[i]
            
            elif len(self) > len(other):
                for i in range(len(other)):
                    result += self[i] * other[i]
                    
        elif type(other) is int or type(other) is float:
            for elem in self.elems:
                result += elem * other
        
        return result
                
    def __rmul__(self, other):
        return self * other
    
    @classmethod
    def zeros(cls, n):
        return NVector([0] * n)

def main():
    goo = NVector(2, 4, 9)
    foo = NVector(2, 4, 9)
    moo = NVector(6, 8, 5)
    
    testif(len(goo) == 3, "len", "len is functional", "len failed")
    testif(foo[2] == 9, "getitem", "getitem is functional", "getitem failed")
    
    moo[1] = 45
    testif(moo[1] == 45, "setitem", "setitem is functional", "setitem failed")
    moo[1] = 8
    
    testif(str(foo) == "[2, 4, 9]", "str", "str is functional", "str failed")
    testif(foo == goo, "eq", "eq is functional", "eq failed")
    testif(foo != moo, "ne", "ne is functional", "ne failed")
    testif(goo + moo == NVector(8, 12, 14) and foo + 3 == NVector(5, 7, 12),
           "add", "add is functional", "add failed")
    testif(2 + moo == NVector(8, 10, 7), "radd", "radd is functional",
           "radd failed")
    testif(moo * foo == 89 and goo * 2 == 30, "mul", "mul is functional",
           "mul failed")
    testif(4 * foo == 60, "rmul", "rmul is functional", "rmul failed")
    testif(NVector.zeros(4) == NVector(0, 0, 0, 0), "zeros",
           "zeros is functional", "zeros failed")
            

if __name__ == '__main__':
    main()