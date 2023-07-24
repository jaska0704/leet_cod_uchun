nomer=13 #leetcod dagi masala raqami

class Solution:
    def romanToInt(self, s: str) -> int:
        dct={'I':1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50, 'XC':90, 'C':100, 'CD':400, 'D':500, 'CM':900, 'M':1000}
        an=0
        for i in range(len(s)):
            if i+1 != len(s) and dct[s[i]]<dct[s[i+1]]:
                an=an-dct[s[i]]
            else:
                an=an+dct[s[i]]
        return an
 #--------------------------------------------------------------------------------------------------
   
nomer=217

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
    
#------------------------------------------------------------------
nomer=136

class Solution:
    def singleNumber(self, nums:list[int]):
        for i in nums:
            if nums.count(i)==1:
                return i