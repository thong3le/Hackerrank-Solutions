#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;


int main() {
    int n, i, y, x;
    cin >> n;
    set<int> myset;
    for (i = 0; i < n; i++){
        cin >> y >> x;
        if (y == 1){
           myset.insert(x); 
        }
        else if (y == 2){
           myset.erase(x); 
        }
        else {
            set<int>::iterator it = myset.find(x);
            if (it != myset.end()) cout << "Yes" << endl;
            else cout << "No" << endl;
        }
    }
    return 0;
}