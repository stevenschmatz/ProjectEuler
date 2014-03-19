//
//  branch.cpp
//  Project Euler Problem 243
//
//  Created by Schmatz on 3/18/14.
//  Copyright (c) 2014 Schmatz. All rights reserved.
//

#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

/*primes is a list of primes, n is all the primes you want to generate.. from 2 to n*/
void genPrimes(vector<int>&primes,int n){
	for(int i=2;i<=n;i++){
		int root=int(sqrt(i))+1;    /*remember the square root*/
		bool found=false;       /*prime found?*/
		for(vector<int>::const_iterator it = primes.begin();it!=primes.end()&& *it<root;it++){
			if(i% *it==0){found=true;break;} /*this is not prime*/
		}
		if(!found)primes.push_back(i); /*this is a prime*/
	}
}

int main() {
    return 0;
}