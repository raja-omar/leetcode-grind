class Solution(object):

    # Example:
    # anagram, nagaram - same letters, same frequency of each letter in each word
    def isAnagram(self, s, t):

        # If two strings have different length then they cant be anagrams so return false straight away
        if len(s) != len(t):
            return False

        # Using hashmap to store frequency of each letter in each string
        sFreq = {}
        tFreq = {}
        
        # Loops to store frequency of each character
        for char in s:
            sFreq[char] = sFreq.get(char, 0) + 1
        for char in t:
            tFreq[char] = tFreq.get(char, 0) + 1

        # Both hashmaps would be the same if, for example, each letter of  string 's' is present in string 't' and has the
        # same frequency in both strings. This satsifies the condition for the words to be anagrams of eachother and so return True
        return tFreq == sFreq

        
        