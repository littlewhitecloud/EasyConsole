#include <iostream>
/*
EasyConsole C++ Version
Bug++:
	Can not exit correctly
	And more...
*/
int main() {
	char op[114514];
	while (std::cout << "PS: >",std::cin >> op, op != "exit")
		system(op);
	return 0;
}
