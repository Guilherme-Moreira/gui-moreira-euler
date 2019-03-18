#include<iostream>
using namespace std;

int main() {
	int s1 = 0;
	int s2 = 0;
	for (int i = 1; i < 101; i++){
		s1 += i;
		s2 += i * i;
	}
	s1 = s1 * s1;
	cout<<s1-s2<<endl;
}
