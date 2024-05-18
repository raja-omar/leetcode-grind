class Solution(object):
    def containsDuplicate(self, nums):
        # Using a set because indexing has O(1) time complexity
        hashset = set()
        # Check if the element is in the set, if it is then it means we're at duplicate and can just return True
        # meaning that the array "Contains Duplicate". Otherwise we put that element in set so that if we encounter its
        # duplicate at some point, we can KNOW its a duplicate (Same technique used in Two Sum)
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)