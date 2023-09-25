#include <bits/stdc++.h>
using namespace std;
#define Nador ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);


int main() 
{
    Nador
        string s;
    vector<char> st;

    
        cin >> s;
        for (int i = 0; i < s.size(); i++)
        {
            //cout << st.back() << "---" << s[i] << "***" << endl;
            if (st.size() > 0 && st.back() == s[i])
                st.pop_back();
            else
                st.push_back(s[i]);
        }
        for (int i = 0; i < st.size(); i++)
            cout << st[i];
        cout << endl;
       

    return 0;
}
