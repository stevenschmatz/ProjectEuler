#include <iostream>
#include <vector>

using namespace std;

int euclidGCD (int a, int b) {
    if (b == 0) {
        return a;
    } else {
        return euclidGCD(b, a % b);
    }
}

vector<int> getDigits (int n) {
    vector<int> digits;
    
    while (n > 0) {
        int nextDigit = n % 10;
        
        digits.insert(digits.begin(),nextDigit);
        n -= nextDigit;
        n /= 10;
    }

    return digits;
}

class Fraction {
public:
    int numerator, denominator;
    
    void setValues(int numerat, int denominat) {
        numerator = numerat;
        denominator = denominat;
    };
    
    void printValues() {
        std::cout << numerator << '/' << denominator << std::endl;
    }
    
    void reduce() {
        int GCD = euclidGCD(numerator, denominator);
        while (GCD != 1) {
            GCD = euclidGCD(numerator, denominator);
            numerator /= GCD;
            denominator /= GCD;
        }
    }
    
    void curiousReduce() {
        vector<int> numeratorDigits, denominatorDigits;
        numeratorDigits = getDigits(numerator);
        denominatorDigits = getDigits(denominator);
        if (numeratorDigits[1] == denominatorDigits[0]) {
            numerator -= numeratorDigits[1];
            numerator /= 10;
            denominator -= denominatorDigits[0] * 10;
        }
    };
    
};

bool fractionsAreEqual(Fraction one, Fraction two) {
    one.reduce();
    two.reduce();
    if (one.numerator == two.numerator && one.denominator == two.denominator) {
        return true;
    }
    return false;
}

class Solution {
    
public:

    bool isCurious (int a, int b) {
        if (a >= b) {
            return false;
        }
        
        Fraction myFrac, curiousFrac;
        myFrac.setValues(a, b);
        curiousFrac.setValues(a, b);
        
        curiousFrac.curiousReduce();
        
        if (curiousFrac.numerator == a && curiousFrac.denominator == b) {
            return false;
        }
        
        return fractionsAreEqual(myFrac, curiousFrac);
    }
    
    void solve() {
        
        int numeratorProduct = 1;
        int denominatorProduct = 1;
        
        for (int numerator = 10; numerator < 100; numerator++) {
            for (int denominator = numerator; denominator < 100; denominator++) {
                if (isCurious(numerator, denominator)) { // 16/64, 19/95, 26/65, 49/98
                    numeratorProduct *= numerator;
                    denominatorProduct *= denominator;
                }
            }
        }
        
        Fraction solutionFrac;
        solutionFrac.setValues(numeratorProduct, denominatorProduct);
        solutionFrac.reduce();
        std::cout << "The solution to Problem 33 is " << solutionFrac.denominator << std::endl;
    }
    
    
} Solution;

int main() {
    Solution.solve();
    return 0;
}