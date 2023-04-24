#include <iostream>

using namespace std;
int main(){
	int x, y, result;
	cout << "Enter two numbers" << endl;
	cin >> x >> y;
	try {
		if (y==0) {
			throw "Division by zero";
		}
		result = x / y;
		cout << "Result" << result << endl;
	}
	catch (const char* error) {
		cout << "Error" << error << endl;
	}
	return 0;
}





