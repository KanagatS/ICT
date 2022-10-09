#include <bits/stdc++.h>

#define sep ' '
#define ll long long

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
      
    int n, m, k; cin >> n >> m >> k;
    cout << ((n * m) % k == 0 ? "YES" : "NO");
      
    return 0;
}