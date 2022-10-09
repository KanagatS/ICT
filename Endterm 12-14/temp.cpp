#include <iostream>
#include <string>

using namespace std;

int main() {
    string s;
    cin >> s;
    int sm = 0;
    
    for (int i = 0; i < s.size(); i++) sm += s[i] - 48;

    cout << sm;

    return 0;
}