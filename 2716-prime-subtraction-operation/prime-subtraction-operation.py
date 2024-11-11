class Solution:
    def isprime(self,n):
        for i in range(2, isqrt(n)+1):
            if n% i == 0:
                return False
        return True

    def primeSubOperation(self, nums: List[int]) -> bool:
        maxElement = max(nums)
        previous_prime = [0]*(maxElement+1)
        for i in range(2, maxElement+1):
            if self.isprime(i):
                previous_prime[i] = i
            else:
                previous_prime[i] = previous_prime[i - 1]

        for i in range(len(nums)):

            # In case of first index, we need to find the largest prime less
            # than nums[0].
            if i == 0:
                bound = nums[0]
            else:
                # Otherwise, we need to find the largest prime, that makes the
                # current element closest to the previous element.
                bound = nums[i] - nums[i - 1]

            # If the bound is less than or equal to 0, then the array cannot be
            # made strictly increasing.
            if bound <= 0:
                return False

            # Find the largest prime less than bound.
            largest_prime = previous_prime[bound - 1]

            # Subtract this value from nums[i].
            nums[i] -= largest_prime

        return True