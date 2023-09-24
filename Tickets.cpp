#include<bits/stdc++.h>
using namespace std;
#define Nador ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);


int main() 
{
    Nador
   
    long long n;
    cin >> n;
    queue<int>q;
    for (int i = 0; i < n; i++)
    {
        long long a, b;
        cin >> a >> b;
        if (a == 1)
        {
            q.push(b);
        }
        else
        {
           
            int x = q.front();
           
            if (b == x)
            {
                cout << "Yes" << endl;
            }
            else
            {
                cout << "No" << endl;
            }
            q.pop();
        }
    }
   

    return 0;
}
