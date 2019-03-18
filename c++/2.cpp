#include<iostream>
using namespace std;

int main() {
	int a, b, s;
	a = 1;
	b = 1;
	s = 0;
	while (b < 4000000){
		if (b % 2 == 0){s += b;}
		int temp;
		temp = a;
		a = b;
		b = a + temp;
	}
	cout<<s<<endl;
}
