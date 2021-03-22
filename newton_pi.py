#!/usr/bin/env python3

#Computes Pi using Newton's method as described here: https://www.youtube.com/watch?v=gMlf1ELvRzc

#Computes Pi using Binomial Theorem by computing Int[Sqrt(1-x^2)dx,{x,0,1/2}]==Pi/12+Sqrt(3)/8

#[Wolfram Alpha](https://www.wolframalpha.com/input/?i=Int%5BSqrt%281-x%5E2%29dx%2C%7Bx%2C0%2C1%2F2%7D%5D-sqrt%283%29%2F8-pi%2F12)

# Int[Sqrt(1-x^2)dx,{x,0,1/2}]=[x-1/2x^3/3-1/8x^5/5-1/16x^7/7-5/128x^9/9-... ] {x,0,1/2} 
#     = [a_0 x - a_1 x^3/3 - a_2 x^5/5 - a_3 x^7/7 - a_4 x^9/9 - ...] at x = 1/2, where
# a_0 = 1
# a_n = 1/n (3-2n)/2 a_{n-1}


from mpmath import mp

def coef(n):
    #n-th coeffiecent
    if (n == 0):
        return mp.mpf(1.0)
    n_mp = mp.mpf(n)
    a = (mp.mpf(3)-mp.mpf(2)*n_mp)/n_mp/mp.mpf(2) * coef(n-1)
    return(-a)

def term(x,n):
    #n-th therm of polynomial evaluated in point x
    if (n == 0):
        return(x)
    v = coef(n) / (2*n + 1)  * x**(2*n+1)
    return(v)

def common_start(sa, sb):
    """ returns the longest common substring from the beginning of sa and sb """
    def _iter():
        for a, b in zip(sa, sb):
            if a == b:
                yield a
            else:
                return

    return ''.join(_iter())


x = mp.mpf(0.5)
sum = mp.mpf(0.0)
mp.dps = 100
k = mp.sqrt(3)/8

print("{: <4} {: <10} {: <10} {: <50}".format('Iter','Term','Error','Pi (only correct digits)'), sep = '\t')
for i in range(50):
    v = term(x,i)
    sum += v
    my_pi = 12*(sum-k)

    print("{: <4} {: <10} {: <10} {: <50}".format(i,
        mp.nstr(v,strip_zeros=False),
        mp.nstr(mp.pi-my_pi,strip_zeros=False),
        common_start(str(mp.pi),str(my_pi)),
        sep = '\t'))
