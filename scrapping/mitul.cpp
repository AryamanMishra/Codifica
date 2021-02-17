#include<bits/stdc++.h>
using namespace std;
int main() {
    // string contest = "https://codeforces.com/contest/1478/problem/A";
    // string problemSet = "https://codeforces.com/problemset/problem/1475/H1";
    string code = "";
    string problemLink;
    cin>>problemLink;
    // when we traverse from left to right the first digits are the contest code and the first capital letter is the problem code in the URLs
    for (int i=0;i<problemLink.length();i++) {
        if (problemLink[i] >= '0' && problemLink[i] <='9') {
            code += problemLink[i];
        }
        else if (problemLink[i] >= 'A' && problemLink[i] <= 'Z' ) {
            code += problemLink[i];
        }
    }
    cout<<code<<endl;
}
