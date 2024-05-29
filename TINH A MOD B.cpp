#include <iostream>
using namespace std; 
int mod_inverse(int a, int b, int n); 
int main()
{
    int a, b, n; 
    cout << " Nhap gia tri a:"; cin >> a; 
    cout << " Nhap gia tri b:"; cin >> b; 
    cout << " Nhap gia tri n:"; cin >> n; 
    int result = mod_inverse(a, b, n); 

    cout << " KQ:" << result << endl; 
    
}

int mod_inverse(int a, int b, int n) {
    int result = 1; 
    a = a % n; 

    while (b > 0) {
        if (b % 2 == 1) {
            result = (result * a) % n; 
        }
        b = b / 2; 
        a = (a * a) % n; 
    }

    return result; 
}