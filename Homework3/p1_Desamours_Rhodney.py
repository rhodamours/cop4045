from testif import testif

class NVector(object):
    """N-dimensional vector of real numbers.
    
    Attributes:
        elems (list): The elements of the vector as a list.
    
    """
    
    elems: list = []
    
    def __init__(self, *nums):
        """Turns nums into a list that represents the elements of the vector.
        
        Args:
            nums: Any amount of numbers.
        """
        
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
        """Returns the number of elements in the vector."""
        return len(self.elems)
    
    def __getitem__(self, index: int):
        """Returns the element at the specified index."""
        return self.elems[index]
    
    def __setitem__(self, index: int, value):
        """Sets the element at the specified index to value."""
        self.elems[index] = value
        
    def __str__(self):
        """Returns the list of elements as a string."""
        return str(self.elems)
    
    def __eq__(self, other: NVector):
        """Returns true if the list of elements of self and other are equal."""
        
        try:
            return self.elems == other.elems
        except AttributeError:
            return False
    
    def __ne__(self, other: NVector):
        """Returns true if the list of elements of self and other
        are not equal."""
        
        try:
            return self.elems != other.elems
        except AttributeError:
            return True
    
    def __add__(self, other):
        """Adds other to self. If other is another NVector, adds the elements
        on aligning indexes. If other is a scalar, the scalar is added to
        every element in self.
        
        Args:
            other: The NVector or scalar to be added to self
            
        Returns:
            The result of the addition of self and other."""
        
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
        """Calls __add__() if other is not an NVector and is added to self
        in the form of other + self."""
        
        return self + other
    
    def __mul__(self, other):
        """Preforms the scalar multiplication of self and other. If other is
        an NVector, returns the dot product."""
        
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
        """Calls __mul__() if other is not an NVector
        and is multiplied with self in the form of other * self."""
        
        return self * other
    
    @classmethod
    def zeros(cls, n: int):
        """Returns a new NVector with dimension n
        where all elements are 0."""
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