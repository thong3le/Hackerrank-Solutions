#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int n, i;
    cin >> n;
    vector<int> v(n);
    for (i = 0; i < n; i++){
        cin >> v[i];
    }
    int q, y;
    cin >> q;
    for (i = 0; i < q; i++){
        cin >> y;
        vector<int>::iterator low = lower_bound(v.begin(), v.end(), y);
        if (*low == y){
            cout << "Yes " << low - v.begin() + 1 << endl;
        }
        else {
            cout << "No " << low - v.begin() + 1 << endl;
        }
            
    }
    return 0;
}