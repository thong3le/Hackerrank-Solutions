#include <iostream>
#include <algorithm>
#include <deque> 
using namespace std;

void printdq(deque<int> dq){
    for (deque<int>::iterator it = dq.begin(); it != dq.end(); it++){
        printf("%d ", *it);
    }
    printf("\n");
}
int main() {
    int tc, i;
    scanf("%d", &tc);
    for (i = 0; i < tc; i++){
        int n, k, j, e, maxdq = -99999999;
        deque<int> dq;
        scanf("%d %d", &n, &k);
        //printf("%d %d\n", n, k);
        for (j = 0; j < k; j++){
            scanf("%d", &e);
            dq.push_back(e);
            if (maxdq < e) maxdq = e;
        }
        printf("%d ", maxdq);
        //printdq(dq);
        for (j = k; j < n; j++){
            scanf("%d", &e);
            dq.push_back(e);
            if (maxdq < e) maxdq = e;
            if (maxdq == *dq.begin()) maxdq = * max_element(dq.begin() + 1, dq.end());
            dq.pop_front();
            printf("%d ", maxdq);
            //printdq(dq);
        }
        printf("\n");
    }
    return 0;
}