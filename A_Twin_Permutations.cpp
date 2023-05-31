#include<bits/stdc++.h>
using namespace std ;
typedef long long ll;
#define rep(i,a,n) for(int i=a;i<n;i++)
#define all(v) v.begin(),v.end()
ll expo1(ll a, ll b)  {ll res = 1;while (b > 0){if(b & 1)res=(res*a);a=(a*a);b = b >> 1;} return res;}
ll expo(ll a,ll b,ll MOD=1e9+7) {ll res = 1; a%=MOD; while(b>0){if(b&1)res=(res*a)%MOD;a=(a*a)%MOD;b=b>>1;} return res;}
void solve()
{
    int n;
    cin>>n;
    int a[n];
    rep(i,0,n)
    cin>>a[i];
    rep(i,0,n)
    cout<<n+1-a[i]<<" ";
    cout<<endl;
    return;
}
int main()
{
ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
int TESTS = 1;
 cin>>TESTS;
while(TESTS--)
solve();
return 0;
}