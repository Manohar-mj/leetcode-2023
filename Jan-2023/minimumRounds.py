class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        task=Counter(tasks)
        if 1 in task.values(): return -1
        ans=0
        for n in task.values():
            ans+= n//3 + bool(n%3)
        return ans
