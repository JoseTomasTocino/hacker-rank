#include <cmath>
#include <cstdio>
#include <vector>
#include <map>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;


int main()
{
    unsigned long N, K;

    cin >> N;
    cin >> K;

    int B[N];
    // int SSS[N + K - 1];
    // Holds the current element of S
    char c;
    int S;

    map<int, int> cache;

    for (size_t i = 0; i < N; ++i)
    {
        // Read a char, convert it to integer
        scanf(" %c", &c);
        S = c - '0';

        if (i == 0)
        {
            B[0] = S;
            cache[0] = B[0];
        }

        else if (i < K)
        {
            B[i] = cache[i - 1] ^ S;
            cache[i] = cache[i - 1] ^ B[i];
        }

        else if (i >= K)
        {
            B[i] = B[i - K + 1];

            for (size_t j = i - K + 2; j < i; ++j)
            {
                B[i] ^= B[j];
            }

            B[i] ^= S;
        }
    }

    for (size_t i = 0; i < N; ++i)
        cout << B[i];

    cout << endl;

    return 0;
}