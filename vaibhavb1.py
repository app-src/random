nums=[1,2,3,4]


def countWays(nums):
    n = len(nums)
    pre = [0] * n
    for i in range(n):
        pre[i] = pre[i - 1] + nums[i]
    
    def check(l, r):
        s1 = pre[l]
        s2 = pre[r] - pre[l]
        s3 = pre[-1] - pre[r]
        if s2 <= (s1 + s3):
            return True
        return False
    
    ans, mod = 0, 10**9 + 7
    for i in range(n - 2):
        lo, hi = i + 1, n - 2
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if check(i, mid):
                lo = mid
            else:
                hi = mid
        if check(i, hi):
            ans += hi - i
        elif check(i, lo):
            ans += lo - i
        ans %= mod
    return ans

print(countWays(nums))