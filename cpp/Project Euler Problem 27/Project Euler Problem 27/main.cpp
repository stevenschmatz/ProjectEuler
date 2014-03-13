//
//  main.cpp
//  Project Euler Problem 27
//
//  Created by Schmatz on 3/13/14.
//  Copyright (c) 2014 Schmatz. All rights reserved.
//

#include <iostream>
#include <math.h>
#include <set>

#define MAX_NUM 10000

class Solution {
public:
    int primes[MAX_NUM];
    
    void gen_sieve_primes(void)
    {
        for (int p=2; p<MAX_NUM; p++) // for all elements in array
        {
            if(primes[p] == 0) // it is not multiple of any other prime
                primes[p] = 1; // mark it as prime
            
            // mark all multiples of prime selected above as non primes
            int c=2;
            int mul = p * c;
            for(; mul < MAX_NUM;)
            {
                primes[mul] = -1;
                c++;
                mul = p*c;
            }
        }
    }
    
} sol;

int main()
{
    sol.gen_sieve_primes();
    std::cout << sol.primes[3] << std::endl;
    return 0;
}