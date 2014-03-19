//
//  main.cpp
//  Project Euler Problem 243
//
//  Created by Schmatz on 3/17/14.
//  Copyright (c) 2014 Schmatz. All rights reserved.
//

#include <iostream>

using namespace std;

unsigned GCD(unsigned u, unsigned v) {
    while ( v != 0) {
        unsigned r = u % v;
        u = v;
        v = r;
    }
    return u;
}

int resilience_numerator(int d) {
    int resilientCount = 0;
    for (int i = 1; i < d; i++) {
        if (GCD(d, i) == 1) resilientCount += 1;
    }
    return resilientCount;
}

int main() {
    int i = 0;
    const double ratio = 15499 / 94744;
    while (true) {
        i += 1;
        if (resilience_numerator(i) < ((i-1) * ratio)) break;
    }
    cout << i << endl;
    return 0;
}
