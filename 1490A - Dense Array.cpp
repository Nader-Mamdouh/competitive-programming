#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long t;
    cin >> t;
    while (t--)
    {
        long long n, count = 0;
        cin >> n;
        int arr[1000];
        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
        }
        for (int i = 0; i < n - 1; i++)
        {
            if (arr[i] > arr[i + 1])
            {
                int mini = arr[i + 1];
                int maxi = arr[i];
                while (mini * 2 < maxi)
                {
                    mini *= 2;
                    count++;
                    //cout << mini << "$$$$" << endl;
                }
                //arr[i + 1] = mini; // Update the larger element to the new value.
            }
            else if (arr[i] < arr[i + 1])
            {
                int mini = arr[i];
                int maxi = arr[i + 1];
                while (mini * 2 < maxi)
                {
                    mini *= 2;
                    count++;
                    //cout << mini << "####" << endl;
                }
                //arr[i] = mini; // Update the smaller element to the new value.
            }
        }
        cout << count<< endl;
    }
    return 0;
}
