#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

int getvalue(map<string, int> m, string x){
    map<string, int>::iterator it = m.find(x);
    if (it != m.end()) return m[x];
    else return 0;
}

int main() {
    int n, i, type, y;
    string x;
    cin >> n;
    map<string, int> m;
    for (i = 0; i < n; i++){
        cin >> type;
        cin >> x;
        if (type == 1){
            cin >> y;
            m[x] = getvalue(m, x) + y;
        }
        else if (type == 2){
            m.erase(x);
        }
        else {
            cout << getvalue(m, x) << endl;
        }
    }
    return 0;
}