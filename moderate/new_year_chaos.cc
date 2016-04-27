#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

void count(vector<int> &arr, vector<int> &inv_cnt) {

    if ( arr.size() < 2 ) {
        return; 
    }

    if ( arr.size() == 2 ) {
        int inverse =  arr[0] < arr[1] ? 0 : 1; 
        if(inverse) {
            inv_cnt[arr[0]-1] = 1;
            int tmp = arr[0];
            arr[0] = arr[1];
            arr[1] = tmp;
        }
        return;
    }

    int mid = arr.size()/2;
    vector<int> left(arr.begin(), arr.begin()+mid);
    vector<int> right(arr.begin()+mid, arr.end());

    count(left, inv_cnt);
    count(right, inv_cnt);

    int i = 0;
    int j = 0;
    int k = 0;
    int counter = 0;

    while ( i != left.size() && j != right.size() ) {
        if ( left[i] < right[j] ) {
            arr[k] = left[i];
            inv_cnt[left[i]-1] += counter;
            i++;
        } else {
            arr[k] = right[j];
            counter++;
            j++;
        }
        k++;
    }


    while ( i != left.size() ) {
        arr[k] = left[i];
        inv_cnt[left[i]-1] += counter;
        i++;
        k++;
    }

    while ( j != right.size() ) {
        arr[k] = right[j];
        j++;
        k++;
    }
}

int main(){
    int T;
    cin >> T;
    for(int a0 = 0; a0 < T; a0++){
        int n;
        cin >> n;
        vector<int> q(n);
        vector<int> inv_cnt(n, 0);
        for(int q_i = 0;q_i < n;q_i++){
           cin >> q[q_i];
        }
        
        count(q, inv_cnt);
        
        int cnt, ii;
        for(cnt=0, ii=0; ii<n; ii++) {
            if ( inv_cnt[ii] > 2 ) {
                cout<<"Too chaotic"<<endl;
                break;
            }
            cnt += inv_cnt[ii];
        }
        if (ii == n) {
            cout<<cnt<<endl;
        }
        // your code goes here
    }
    return 0;
}
