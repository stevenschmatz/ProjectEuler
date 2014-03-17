//
//  main.cpp
//  Project Euler Problem 32
//
//  Created by Schmatz on 3/17/14.
//  Copyright (c) 2014 Schmatz. All rights reserved.
//

//  PROMPT:
//  Find sum of products for which expression [a * b = p] is 1 thru 9 pandigital
//
//  IDEAS:
//  1.  No zeroes can be in a, b, or p
//  2.  If last digit of a and b are the same, doesn't work
//  3.  Special Cases:
//          If last digits = (3, 5), p last digit = 5
//          If last digits = (1, x), p last digit = x

#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

bool is_pandigital_product(int a, int b)
{
    string aString = to_string(a);
    string bString = to_string(b);
    string pString = to_string(a*b);
    
    stringstream ss;
    ss << aString << bString << pString;
    string pandigitalString = ss.str();
    
    sort(pandigitalString.begin(), pandigitalString.end());
    
    return pandigitalString == "123456789";
}

int main() {
    
    int sum = 0;
    
    set<int> values;
    
    for (int i=1; i < 1000; i++) {
        for (int j=i; j < 10000/i; j++) {
            if (is_pandigital_product(i, j)) {
                cout << i << " * " << j << " = " << i*j << endl;
                if (!binary_search(values.begin(), values.end(), i*j)) {
                    values.insert(i*j);
                }
            }
        }
    }
    
    for (std::set<int>::iterator it=values.begin(); it!=values.end(); ++it) {
        sum += *it;
    }
    cout << sum << endl;
    
    return 0;
}