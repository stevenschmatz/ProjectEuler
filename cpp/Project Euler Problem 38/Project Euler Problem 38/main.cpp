//
//  main.cpp
//  Project Euler Problem 38
//
//  Created by Schmatz on 3/17/14.
//  Copyright (c) 2014 Schmatz. All rights reserved.
//

#include <iostream>
#include <string>
#include <stdlib.h>
#include <math.h>

using namespace std;

int pandigital(int n) {
    string nString = to_string(n);
    string resultString = "";
    
    int i = 1;
    while (i < 10) {
        resultString += to_string(n*i);
        if (resultString.length() == 9) {
            string resultStringCopy = resultString;
            sort(resultString.begin(), resultString.end());
            if (resultString == "123456789") {return atoi(resultStringCopy.c_str());}
            else {return 0;}
        }
        
        if (resultString.length() > 9) {
            return 0;
        }
        i++;
    }
    
    return atoi(resultString.c_str());
}
    
int main() {
    int currentMax = 0;
    for (int i = 1; i < pow(10,5); i++) { // sqrt of pow(10, 10), which is max possible int
        if (pandigital(i) > currentMax) {
            currentMax = pandigital(i);
        }
    }
    
    cout << currentMax << endl;
    
    return 0;
}