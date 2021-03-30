#include<bits/stdc++.h>
using namespace std;

int main(){
    
    int n,h;
    cin>>n>>h;

    int sum=0;
    int value;
    vector<int> v;

    for(int i=0; i<n; i++){
        cin>>v[i];
        if(v[i]<=h){
            sum+=1;
        }else{
            sum+=2;
        }
    }

    cout<<sum;

    return 0;
}