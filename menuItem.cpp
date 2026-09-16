#include "menuItem.h"

MenuItem::MenuItem()
{
    name = "N/A";
    price = 0.0;
}

MenuItem::MenuItem(string n, double p)
{
    name = n;
    price = p;
}

MenuItem::MenuItem(const MenuItem &rh)
{
    name = rh.name;
    price = rh.price;
}

void MenuItem::setName(string n)
{
    name = n;
}

void MenuItem::setPrice(double p)
{
    price = p;
}

string MenuItem::getName()
{
    return name;
}

double MenuItem::getPrice()
{
    return price;
}

void MenuItem::displayMenuItemData()
{
    cout << name << ": " << price << endl;
}

