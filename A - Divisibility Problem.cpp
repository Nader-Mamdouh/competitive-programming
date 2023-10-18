#include <bits/stdc++.h>
using namespace std;
int main()
{
    long long  n;
    cin >> n;
    while (n--)
    {
        long long a, b,temp;

        cin >> a >> b;
        if (a == b || a % b == 0)cout << 0 << endl;
        else if (a < b)cout << b - a << endl;
        else cout << b - a % b << endl;
    }
    return 0;
}
