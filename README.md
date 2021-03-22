# Pi_Newton_method
Compute Pi using Newton's method as described here: https://www.youtube.com/watch?v=gMlf1ELvRzc

Compute Pi using Binominal Theorem by computing Int[Sqrt(1-x^2)dx,{x,0,1/2}]=Pi/12+Sqrt(3)/8
[Wolfram Alpha](https://www.wolframalpha.com/input/?i=Int%5BSqrt%281-x%5E2%29dx%2C%7Bx%2C0%2C1%2F2%7D%5D-sqrt%283%29%2F8-pi%2F12)

Int[Sqrt(1-x^2)dx,{x,0,1/2}]=[x-1/2x^3/3-1/8x^5/5-1/16x^7/7-5/128x^9/9-... ] {x,0,1/2} = [a_0 x - a_1 x^3/3 - a_2 x^5/5 - a_3 x^7/7 - a_4 x^9/9 - ...] at x = 1/2, where

a_0 = 1
a_n = 1/n (3-2n)/2 a_{n-1}
