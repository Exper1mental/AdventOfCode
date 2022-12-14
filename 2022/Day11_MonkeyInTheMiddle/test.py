# class Conv2PrimeFactors():        
#     def main(self, integer):
#         num_primes, prime_fac = self.converter(integer)
#         num_check = self.get_integer(num_primes, prime_fac)
#         print(integer, num_check, num_primes, prime_fac)
#         return num_primes, prime_fac
    
#     def converter(self, integer):
#         x = integer
#         nums = [i for i in range(1,x+1) if x%i==0]
#         num_primes, prime_fac = self.get_primes(nums)
#         prime_fac = self.get_multiples(num_primes, x)
#         return num_primes, prime_fac
    
#     def get_primes(self, nums):
#         num_primes = []
#         prime_fac = []

#         for i, num in enumerate(nums.copy()):
#             if num > 1:
#                 # Iterate from 2 to n / 2
#                 for j in range(2, int(num/2)+1):
#                     # If num is divisible by any number between
#                     # 2 and n / 2, it is not prime
#                     if (num % j) == 0: # is not a prime number
#                         break
#                 else: # is a prime number
#                     num_primes.append(num)
#                     prime_fac.append(0)
#         return num_primes, prime_fac
    
#     def get_multiples(self, num_primes, x):
#         i = 0
#         prime = num_primes[i]
#         prime_fac = [0]
#         while x > 1:
#             while x % prime == 0:
#                 if x == 1:
#                     break
#                 x = x // prime
#                 prime_fac[i] += 1
#             i += 1
#             if i != len(num_primes):
#                 prime = num_primes[i]
#                 prime_fac.append(0)
#             else:
#                 break
#         return prime_fac
    
#     def get_integer(self, num_primes, prime_fac):
#         num_check = 1
#         for i in range(len(num_primes)):
#             num_check *= num_primes[i]**prime_fac[i]
#         return num_check
    
# class PrimeExpMath():
#     # def add(self, v1_primes, v1_prime_exps, v2_primes, v2_prime_exps):
#     #     return primes, prime_exps
    
#     def multiply(self, v1_primes, v1_prime_exps, v2_primes, v2_prime_exps):
#         primes = list(set([*v1_primes, *v2_primes]))
#         prime_exps = [0] * len(primes)
#         for i, v in enumerate(primes):
#             for j, v1 in enumerate(v1_primes):
#                 if v == v1:
#                     prime_exps[i] += v1_prime_exps[j]
#             for j, v2 in enumerate(v2_primes):
#                 if v == v2:
#                     prime_exps[i] += v2_prime_exps[j]
#         return primes, prime_exps
    
#     def is_in(self, numer_primes, numer_prime_exps, denom_primes, denom_prime_exps):
#         for i, v1 in enumerate(denom_primes):
#             match = False
#             for j, v in enumerate(numer_primes):
#                 if v == v1:
#                     if numer_prime_exps[j] - denom_prime_exps[i] >= 0:
#                         match = True
#             if not match:
#                 return False
#         return True
    
# # divide = 5

# # print(g.fac(10))
# # for i in range(10):
# #     print(g.fib(i))

def hcf(a, b): # Highest Common Factor
    if(b == 0):
        return abs(a)
    else:
        return hcf(b, a % b)
    
def lcm(a, b): # Least Common Multiple
    if a > b:  
        greater = a
    else:  
        greater = b
    while True:  
        if((greater % a == 0) and (greater % b == 0)):  
            return greater  
        greater += 1

if __name__ == '__main__':
    a = 27
    b = 123
    m = hcf(10, 6)
    short = (a*b) % m
    long = ((a % m) * (b % m)) % m
    print(m, short, long)
        
    # a = lcm(2, 7)
    # a = lcm(a, 13)
    # a = lcm(a, 3)
    # a = lcm(a, 19)
    # a = lcm(a, 5)
    # a = lcm(a, 11)
    # a = lcm(a, 17)
    # print(2*7*13*3*19*5*11*17, a)
    # conv = Conv2PrimeFactors()
    
    a = 10
    a //= 2
    print(a)
    
    magic = 9699690
    b = [5, 17]
    print(magic//(5*17))
    
    # v1 = 500
    # v1_primes, v1_prime_exps = conv.main(v1)
    # print(v1_primes, v1_prime_exps)
    # print(conv.get_integer(v1_primes, v1_prime_exps))
    
    # v2 = 501
    # v2_primes, v2_prime_exps = conv.main(v2)
    # print(v2_primes, v2_prime_exps)
    # print(conv.get_integer(v2_primes, v2_prime_exps))
    
    # math = PrimeExpMath()
    # print()
    # print(math.multiply(v1_primes, v1_prime_exps, v2_primes, v2_prime_exps))
    
    # print()
    # v3 = 13
    # v3_primes, v3_prime_exps = conv.main(v3)
    # print(v3_primes, v3_prime_exps)
    # print(conv.get_integer(v3_primes, v3_prime_exps))
    # print(math.is_in(v1_primes, v1_prime_exps, v3_primes, v3_prime_exps))
    
    # print(conv.get_integer(v1_primes, v1_prime_exps) + conv.get_integer(v3_primes, v3_prime_exps))
    
    