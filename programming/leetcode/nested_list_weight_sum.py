# https://leetcode.com/problems/nested-list-weight-sum/

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        total = 0
        for el in nestedList:
            if el.isInteger():
                total += el.getInteger()
            else:
                total += self.__helper(el.getList())
        
        return total
    
    def __helper(self, nested_list: List[NestedInteger], depth=2):
        total = 0
        i = 0
        l = len(nested_list)
        while i < l:
            if nested_list[i].isInteger():
                total += depth * nested_list[i].getInteger()
            else:
                total += self.__helper(nested_list[i].getList(), depth+1)
            i += 1
        
        return total
    