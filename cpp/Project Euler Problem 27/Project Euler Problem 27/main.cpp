//
//  main.cpp
//  Project Euler Problem 27
//
//  Created by Schmatz on 3/16/14.
//  Copyright (c) 2014 Schmatz. All rights reserved.
//

//  PROMPT:
//  find a and b in [n**2 + an + b] such that it produces the greatest number of consecutive primes, starting at n = 0. (|a| and |b| < 1000)
//
//  IDEAS:
//  1. Because of n = 0 case, b has to be prime. -> generate all primes from 2 to 1000, about 173 primes.
//  2. Since [n**2 + an + b] > 1, [n**2 + an] > [1 - b].
//      Thus, a > [(1 - b - n**2)/n) = [(1 - (b + (n**2))/n]
//      At the lowest bound at n = 1, a > [(1 - (b + 1))/1] -> a > -b.
//
//  Thus, iterate through b primes 2 to 1000, and for each b iterate through a values from -b to 1000.
//  For each pair (a, b), evaluate expression and break when primality test reveals false.

#include <iostream>
#include <vector>
#include <algorithm>

class Solution {
public:
    
    std::vector<int> generate_primes(int n)
    {
    std::vector<int> primes;
    primes.push_back(2);
    for(int i=3; i < n; i++)
    {
        bool prime=true;
        for(int j=0;j<primes.size() && primes[j]*primes[j] <= i;j++)
        {
            if(i % primes[j] == 0)
            {
                prime=false;
                break;
            }
        }
        if(prime)
        {
            primes.push_back(i);
        }
    }
    return primes;
}
    
    std::vector<int> primes = generate_primes(1000*1000);

    int number_of_primes(int a, int b) {
        int primeCount = 0;
        int n = 0;
        while (true) {
            int evaluation = n*n + a*n + b;
            if (!std::binary_search(primes.begin(), primes.end(), evaluation)) {
                break;
            }
            primeCount++;
            n++;
            }
        return primeCount;
    };
    
    int solve() {
        int maximumA = 0;
        int maximumB = 0;
        int mostPrimes = 0;
        
        int a, b;
        
        int b_index = 0;
        while (true) {
            b = primes[b_index];
            if (b >= 1000) break;
            a = -b;
            while (true) {
                if (a >= 1000) break;
                int primeCount = number_of_primes(a, b);
                if (primeCount > mostPrimes) {
                    mostPrimes = primeCount;
                    maximumA = a;
                    maximumB = b;
                }
                a++;
            }
            b_index++;
        }
        
        return maximumA*maximumB;
    }

} solution;

int main() {
    std::cout << "The product of a and b is " << solution.solve() << '.' << std::endl;
    return 0;
}