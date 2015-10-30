#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cassert>
using namespace std;

class Student {
    private:
        int score[5];
    public:
        void Input(){cin >> score[0] >> score[1] >> score[2] >> score[3] >> score[4];}
        int CalculateTotalScore(){ return (score[0] + score[1] + score[2] + score[3] + score[4]);}
};

int main() {
   int n;
     cin>>n;
     Student s[n];
     for(int i=0;i<n;i++)
      s[i].Input();
     int count=0;
     int krish_score=s[0].CalculateTotalScore();
     for(int i=1;i<n;i++)
    {
      int total=s[i].CalculateTotalScore();
      if(total>krish_score)
        count++;
    }
     cout<<count;
    return 0;
}