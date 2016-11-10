'''
    Given a string, the task is to find whether it contains an additive sequence or not.
    A string contains an additive sequence if its digits can make a sequence of numbers in which every number is addition of previous two numbers.
    You are required to complete the function which returns true if the string is a valid sequence else returns false.
'''

class Additive():

    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """

        def isValid(num):
            return len(num) == 1 or num[0] != '0'

        def search(a, b, c):
            d = str(int(a) + int(b))
            if not isValid(d) or not c.startswith(d):
                return False
            if c == d:
                return True
            return search(b, d, c[len(d):])

        size = len(num)
        for x in range(1, int(size/2) + 1):
            for y in range(x + 1, size):
                a, b, c = num[:x], num[x:y], num[y:]
                if not isValid(a) or not isValid(b):
                    continue
                if search(a, b, c):
                    return True
        return False

obj = Additive()
print(obj.isAdditiveNumber('1235813'))