#ifndef MENUITEM_H
#define MENUITEM_H
#include <iostream>
using namespace std;

class MenuItem
{
    string name;
    double price;
    public:
        MenuItem();
        MenuItem(string,double);
        MenuItem(const MenuItem&);

        void setName(string);
        void setPrice(double);

        string getName();
        double getPrice();

        void displayMenuItemData();
};

#endif