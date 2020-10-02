#include<iostream>
using namespace std;
template<class E,class G>//function templates with multiple templates
void fun(E b,G c)// function templates
{cout<<"value of b="<<b<<endl;
cout<<"value of c="<<c<<endl;}
template<class E>void fun(E u)//function overloading
{
	cout<<"value of u="<<u<<endl;
	
}template<class F>// class templates
class A{
public:
F n1=9;F n2=8;
void add(){cout<<"addition of n1 and n2\n"<<n1+n2;
}
};
//******************//
template<typename T>//function template with single parameter
T mymax(T x,T y)
{
	return(x>y)?x:y;
}template<class L,class M>//class template with multiple parameter
class w{
	L a;
M b;
public:
w(L x,M y)
{
	a=x;
	b=y;
}void display(){
	cout<<"values of x and y are"<<a<<b<<endl;
}
};template<class N,int size>
class z{public:N arr[size];
void insert(){
	int i=1;
	for(int j=0;j<size;j++){
		arr[j]=i;
		i++;
	}
}void display(){
	for(int i=0;i<size;i++)
	{
		cout<<arr[i]<<" ";
	}
}
};

int main() 
{  fun(12,7);//using function template with multiple parameter
    fun(12);//function overloading
    cout<<mymax<int>(1,2)<<endl;//using function template with one datatype
	A<int>d;//class template with single parameter
	d.add();
	w<int,float>q(2,1.8);//class template with multiple parameter
	q.display();
	z<int,10>t1;//nontype template arguments
	t1.insert();
	t1.display();
	return 0;
}
