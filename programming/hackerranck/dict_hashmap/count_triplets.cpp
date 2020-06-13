#include<bits/stdc++.h>
using namespace std;

const size_t SIZE = 6;

map<long long,long long> l,r;

int main()
{
	long long a[SIZE] = {1, 1, 1, 1, 1, 1}, k = 1, ans=0;
	for(int i=0;i<SIZE;i++)
		r[a[i]]++;
	for(int i=0;i<SIZE;i++)
	{
		r[a[i]]--;
		if(a[i]%k==0)
		{
			ans+=l[a[i]/k]*r[a[i]*k];
		}
		l[a[i]]++;
	}
	printf("%lld\n",ans);
	return 0;
}