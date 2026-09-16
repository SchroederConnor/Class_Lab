menu: menuItem.o main.o
	g++ -o menu menuItem.o main.o 
menuItem.o: menuItem.cpp menuItem.h
	g++ -c menuItem.cpp
main.o: main.cpp menuItem.h
	g++ -c main.cpp 
clean: 
	rm *.o menu