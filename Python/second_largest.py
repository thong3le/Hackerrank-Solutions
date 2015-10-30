
int(raw_input())
nums = map(int, raw_input().split())
m = max(nums)

print max(n for n in nums if n!=M) 