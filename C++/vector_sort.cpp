#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int n, i, e;
    vector<int> v;
    cin >> n;
    for (i = 0; i < n; i++){
        cin >> e;
        v.push_back(e);
    }
    
    sort(v.begin(), v.end());
    
    for (i = 0; i < n; i++){
        cout << v[i] << ' ';
    }
    
    return 0;
}