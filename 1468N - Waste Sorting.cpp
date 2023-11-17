#include <bits/stdc++.h>
using namespace std;
void Nador()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
}
int main() 
{
    Nador();
    long long t;
    cin >> t;
    while (t--)
    {
        long long c1, c2, c3;
        cin >> c1 >> c2 >> c3;
        long long a, b, c, a1, b1;
        cin >> a >> b >> c >> a1 >> b1;
        bool flag1 = false;
        bool flag2 = false;
        if ((c1 - a >= 0) && (c2 - b >= 0) && (c3 - c >= 0))
        {
            c1 -= a;
            c2 -= b;
            c3 -= c;
            if (c1 - a1 >= 0)
            {
                c1 -= a1;
                flag1 = true;
            }
            else {
                a1 -= c1;
                if (c3 - a1 >= 0)
                {
                    c3 -= a1;
                    flag1 = true;
                }
                else {
                    cout << "NO" << endl;
                    continue;
                }
            }
            if (c2 - b1 >= 0)
            {
                c2 -= b1;
                flag2 = true;
            }
            else {
                b1 -= c2;
                if (c3 - b1 >= 0)
                {
                    c3 -= b1;
                    flag2 = true;
                }
                else {
                    cout << "NO" << endl;
                    continue;
                }
            }
            if (flag1 & flag2)
            {
                cout << "YES" << endl;
                continue;
            }
        }
        else {
            cout << "NO" << endl;
            continue;
        }
    }
    return 0;
}
