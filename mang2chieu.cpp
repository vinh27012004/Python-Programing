#include<iostream>
#define MAXC 3
#define MAXD 3
typedef int matran[MAXC][MAXD];
using namespace std;
void nhap(matran &a)
{
  for(int i=0; i<MAXC; i++)
        for(int j=0; j<MAXD; j++)
        {
            cout<<"Nhap phan tu a["<<i<<"]["<<j<<"]: ";
            cin>>a[i][j];
        }  
}
void xuat(matran a)
{
    for(int i=0; i<MAXC; i++)
    {
        for(int j=0; j<MAXD; j++)
            cout<<a[i][j]<<" ";
        cout<<endl;
    }
}
void tong2matran(matran a, matran b, matran c)
{
    for(int i=0; i<MAXC; i++)
        for(int j=0; j<MAXD; j++)
            c[i][j]=a[i][j]+b[i][j];

}
void tongduongcheomatran(matran a,int &s){
    for(int i = 0; i < MAXC; i++)
        for(int j = 0; j < MAXD; j++)
            if(i == j)
                s += a[i][j];
}
int main(){
    int s;
    matran a;
    cout<<"Nhap ma tran a: "<<endl;
    nhap(a);
    xuat(a);
    tongduongcheomatran(a,s);
    cout << "S = " << s << endl;
    return 0;
}

