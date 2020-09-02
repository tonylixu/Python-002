def use_fast_slow_pointers(n):
    def helper(n):
        total = 0
        print(f'n={n}')
        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10
        print(f'total = {total}')
        return total

    slow, fast = n, helper(n)
    while slow != fast:
        slow = helper(slow)
        fast = helper(helper(fast))
    return slow == 1

num = 19
print(use_fast_slow_pointers(num))