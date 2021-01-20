class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x)[::-1] == str(x):
            return True
        return False

if __name__ == '__main__':
    s = Solution()
    r = s.isPalindrome(123321)
    print(f"res:{r}")
    r = s.isPalindrome(-121)
    print(f"res:{r}")
    r = s.isPalindrome(10)
    print(f"res:{r}")