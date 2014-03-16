//
//  main.cpp
//  1001
//
//  Created by Schmatz on 3/16/14.
//  Copyright (c) 2014 Schmatz. All rights reserved.
//


#include <iostream>

using namespace std;

#include <iostream>

using namespace std;

int main() {
    int cycleLength = 0;
    int integerWithLongestCycle;
    
    for (int i = 1000; i >= 1; i--) {
        if (cycleLength >= i) {
            break;
        }
        
        int remainderList[1000] = {};
        int value = 1;
        int position = 0;
        
        while (remainderList[value] == 0 && value != 0) {
            remainderList[value] = position;
            value *= 10;
            value %= i;
            position++;
        }
        
        if (position - remainderList[value] > cycleLength) {
            cycleLength = position - remainderList[value];
            integerWithLongestCycle = i;
        }
    }
    
    cout << "The integer with the longest reciprocal cycle length is " << integerWithLongestCycle << ", with a cycle length of " << cycleLength << '.' << endl;
}