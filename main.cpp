#include "menuItem.h"


int main()
{
    // Create a MenuItem object named burger using the default constructor
    MenuItem burger = MenuItem();

    // Set the burger object's name to "Burger" using the appropriate setter method
    burger.setName("Burger");
    
    // Set the burger object's price to 8.5 using the appropriate setter method
    burger.setPrice(8.5);

    // Create a MenuItem object named pizza using the parameterized constructor
    // Pass "Pizza" as the name and 18.55 as the price
    MenuItem pizza = MenuItem("Pizza", 18.55);

    // Create a MenuItem object named sandwich by copying the information from burger
    // This uses the copy constructor
    MenuItem sandwich = burger;

    // Update the sandwich object's name to "Sandwich" using the setter method
    sandwich.setName("Sandwich");

    // Create an array of MenuItem objects named items with size 3
    // Assign burger to index 0, pizza to index 1, and sandwich to index 2
    MenuItem items[3];
    items[0] = burger;
    items[1] = pizza;
    items[2] = sandwich;

    cout << "Restaurant Menu" << endl;

    // Use a loop to display information for each MenuItem in the array
    // Call the displayMenuItemData() method for each object in the for loop
    for(int i = 0; i < 3; i++)
    {
        cout << i + 1 << ". ";
        items[i].displayMenuItemData();
    }

    //To pass the test your code should have exact output as the output.txt so do not modify it.
    //Check the item name spelling/case and the newlines are exactly same in your output
    
    return 0;
}