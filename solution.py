class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict_cnt = {}
        for x in nums:
            if dict_cnt.get(x) is None :
                dict_cnt[x]=1
            else:
                dict_cnt[x]+=1
                return True
        return False
        
