//
//  main.cpp
//  Roman Numerals
//
//  Created by Schmatz on 3/22/14.
//  Copyright (c) 2014 Schmatz. All rights reserved.
//

#include <iostream>
#include <unordered_map>
#include <fstream>
#include <string>

using namespace std;

class Solution {
private:
    unordered_map<char, int> romanValues = {{'I', 1},{'V', 5},{'X', 10},{'L', 50},{'C', 100},{'D', 500},{'M', 1000}};

    int romanRead(string RomanNumerals) {
        int intForm = 0;
        for (int i = 0; i < RomanNumerals.length(); i++) {
            if (i < RomanNumerals.length() - 1) { // subtractive pair begin index cannot be last character
                if (RomanNumerals.at(i) == 'I' && (RomanNumerals.at(i+1) == 'V' || RomanNumerals.at(i+1) == 'X')) {
                    intForm -= romanValues['I'];
                    continue;
                }
                if (RomanNumerals.at(i) == 'X' && (RomanNumerals.at(i+1) == 'L' || RomanNumerals.at(i+1) == 'C')) {
                    intForm -= romanValues['X'];
                    continue;
                }
                if (RomanNumerals.at(i) == 'C' && (RomanNumerals.at(i+1) == 'D' || RomanNumerals.at(i+1) == 'M')) {
                    intForm -= romanValues['C'];
                    continue;
                }
            }
            intForm += romanValues[RomanNumerals.at(i)];
        }
        return intForm;
    }
    
    int romanLength(int n) {
        /*
        First digit = I, II, III, IV, V, VI, VII, VIII, IX             [1, 2, 3, 2, 1, 2, 3, 4, 2]
        Second digit = X, XX, XXX, XL, L, LX, LXX, LXXX, XC            [1, 2, 3, 2, 1, 2, 3, 4, 2]
        Third digit = C, CC, CCC, CD, D, DC, DCC, DCCC, CM             [1, 2, 3, 2, 1, 2, 3, 4, 2]
        Fourth digit onwards = M, so just add ((number - number % 1000) / 1000) to count.*/
        int romanDigitLength[10] = {0, 1, 2, 3, 2, 1, 2, 3, 4, 2};
        int length = 0;
        int i = 0;
        while (n > 0) {
            if (i > 2) {
                length += n;
                break;
            }
            length += romanDigitLength[n % 10];
            n -= n % 10;
            n /= 10;
            i += 1;
        }

        return length;
    }
    
    void readLines() {

    }
    
public:
    
    int solve() {
        int savedCharacters = 0;
        string line;
        ifstream myfile ("/Users/stevenschmatz/CS/project-euler/cpp/Project Euler Problem 89/Roman Numerals/roman.txt");
        if (myfile.is_open())
        {
            while (! myfile.eof() )
            {
                getline (myfile,line);
                savedCharacters += line.length() - romanLength(romanRead(line));
            }
            myfile.close();
        }
        return savedCharacters;
    }
    
} mySolution;


int main (int argc, char *argv[]) {
    cout << "The number of characters saved is " << mySolution.solve() << '.' << endl;
	return 0;
}