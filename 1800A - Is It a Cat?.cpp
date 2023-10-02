#include<bits/stdc++.h>
using namespace std;
#define Nador ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);


int main()
{
    Nador
        long long t;
         cin >> t;
    while (t--)
    {
        long long n;
        cin >> n;
        string s,s2;
        cin >> s;
        for (char c : s) 
        {
            s2 += tolower(c);
        }
       string:: iterator end = std::unique(s2.begin(), s2.end());
        s2.erase(end, s2.end());
        if (s2 == "meow")
        {
            cout << "YES" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }
    }

    return 0;
}
