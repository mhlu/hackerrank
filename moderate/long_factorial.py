#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    vector<int> res;
    int n;
    res.push_back(1);
    cin>>n;
    for (int i=1; i<=n; i++) {
        int c = 0;
        for (int j=0; j<res.size(); j++) {
            int tmp, m;
            tmp = res[j]*i+c;
            m = tmp%10;
            c = (tmp - m)/10;
            res[j] = m;
        }
        while (c != 0) {
            res.push_back(c%10);
            c = c/10;
        }
    }
    for (int j=res.size()-1; j>=0; j--) {
        cout<<res[j];
    }
    cout<<endl;
    return 0;
}
