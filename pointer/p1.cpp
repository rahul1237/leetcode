#include<bits/stdc++.h>
using namespace std;

int main(){
    
    int a=10;

    // created a pointer variable!
    int* aptr;
    // this stores the address of 'a'
    aptr=&a;

    // returns the address of 'a'
    cout<<aptr<<endl;
    // return the value of 'a'
    cout<<a<<endl;
    // returns itself address!
    cout<<&a<<endl;
    // returns itself address!
    cout<<&aptr<<endl;
    // returns the value which is present at that point!
    cout<<*aptr<<endl;

    // updates the value which is present at that memory location!
    *aptr=20;
    cout<<a<<endl;
    cout<<*aptr<<endl;

    cout<<endl;
    cout<<endl;
    cout<<endl;
    cout<<endl;
    cout<<endl;

    // incrementing and decrementing the address of a which is present in 'aptr'
    cout<<aptr<<endl;   
    aptr++;
    cout<<aptr<<endl;   

    cout<<aptr<<endl;   
    aptr--;
    cout<<aptr<<endl;   

    return 0;
}