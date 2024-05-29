#include <iostream>

using namespace std;

// Tinh uoc chung lon nhat bang thuat toan euclid mo rong: 
int gcd(int a, int b, int &x, int &y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }

    int x1, y1;
    int d = gcd(b, a % b, x1, y1);  // De quy voi cac so doi bi dao nguoc

    x = y1;
    y = x1 - (a / b) * y1;
    return d;
}

// Ham tinh nghich dao modulo a: 
int mod_inverse(int a, int n) {
    int x, y;
    int d = gcd(a, n, x, y);

    // Kiem tra xem uoc chung lon nhat co bang 1 khong
    if (d != 1) {
        cout << "Ko ton tai nghich dao modulo cho " << a << " mod " << n << endl;
        return -1;  
    }

    
    return (x + n) % n;  
}

int main() {
    int a, n;

    cout << "Enter a: ";
    cin >> a;

    cout << "Enter n: ";
    cin >> n;

    int inverse = mod_inverse(a, n);

    if (inverse == -1) {
    } else {
        cout << "Nghich dao modulo cua " << a << " mod " << n << " is: " << inverse << endl;
    }

    return 0;
}