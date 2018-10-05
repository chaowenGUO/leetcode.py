class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dictionary = {'{':'}', '[':']', '(':')'}
        stack = []
        for bracket in s:
            if bracket in dictionary: stack.append(dictionary.get(bracket))
            else:
                if not stack or stack.pop() != bracket: return False
        return not stack
