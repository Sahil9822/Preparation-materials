/*
Mike had been provided with T integers and an integer S by his professor; he needs to identify the probability of getting a set of three integers the same as S from the T integers.
Mike is poor at interpreting floating-point numbers. Guide him to identify the probability based on a fraction, cut down to its lowest terms.

Input format
The first line contains two space-separated integers - T and S, which represent the total number of integers Mike had, and the value S whose S-same-triplet was required.

Output format
Display the probability of finding an S-equal triplet in terms of the lowest fraction.
For example, if the answer is 4/8, you must print 1/2, which is the lowest reduced fraction of 4/8.

Code constraints
1 ≤ T ≤ 106
1 ≤ Numbers ≤ 109
1 ≤ S ≤ 109

Sample testcases
Input 1
5 4
1 4 4 4 1

Output 1
1/10

Input 2
16 2
1 2 2 3 1 2 2 3 1 2 2 3 1 2 2 3

Output 2
1/10

Code:-*/
/*Soution:-*/
#include <stdio.h>
#define gc getchar_unlocked
#define pc putchar_unlocked
inline long long int sscan()
{
    long long int n=0;
    int ch=gc();
    while(ch < '0'|| ch > '9')
    ch=gc();
    while(ch >= '0' && ch <= '9')
    {
        n = (n <<3)+(n<<1) + ch-'0';
        ch=gc();
    }
    return n;
}

inline void lprint(long long int a)
{
    int i=0;
    char S[40];
    while(a>0)
    {
        S[i++]=a%10+'0';
        a=a/10;
    }
    --i;
    while(i>=0)
    pc(S[i--]);
}
long long int gcd(long long int a,long long int b)
{
    return(b==0)?a:gcd(b,a%b);
}
long long int gcd_bin(long long int u,long long int v)
{
    long long int t, k;
    u = u < 0 ? -u:u;
    v = v < 0 ? -v:v;
    if (u < v)
    {
        t = u;
        u = v;
        v = t;
    }
    if (v == 0)
    return u;
    k = 1;
    while (u & 1 == 0 && v & 1 == 0)
    {
        u >>= 1; v >>= 1;
        k >>= 1;
    }
    t = (u & 1)? -v:u;
    while (t)
    {
        while (t & 1 == 0)
        t >>= 1;
        if (t > 0)
        u = t;
        else
        v = -t;
        t = u - v;
    }
    return u*k;
}
int main()
{
    long long int n,x,k,num,count,i,res1,res2,res3;
    n = sscan();
    k = sscan();
    count=0;
    for(i=0;i<n;i++)
    {
        num=sscan();
        if(num==k) count++;
    }
    if(count==0)
    {
        printf("0/1\n");
    }
    else
    {
        res1=count*(count-1)*(count-2);
        res2=n*(n-1)*(n-2);
        res3=gcd(res1,res2);
        lprint(res1/res3);
        printf("/");
        lprint(res2/res3);
        printf("\n");
    }
    return 0;
}
