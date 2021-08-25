# LikeMinds Demo

## Overview :-
This is a demo project.


## INSTALLATION :-
1. Clone the repo in your local system.

2. Create a virtual environment.
    - MAC users :-
        Refer to :- https://gist.github.com/pandafulmanda/730a9355e088a9970b18275cb9eadef3

    - Windows and Linux users :-
        Refer to :- https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/

3. Install Requirements
    Change directory to the root folder and run
    
    `pip install -r requirements.txt` 

4. Make migrations and migrate.
    Run these commands

    `python manage.py makemigrations` and `python manage.py migrate`

5. Start the server.

    `python manage.py runserver`

6. You are good to go. Happy hacking !


## API Description :- 
1. Homepage :- http://127.0.0.1:8000

2. Create Item :- http://127.0.0.1:8000/create_item

3. Add Item to Inventory :- http://127.0.0.1:8000/add_to_inventory

4. Add User :- http://127.0.0.1:8000/add_user

5. Add Items to User Cart :- http://127.0.0.1:8000/add_to_user_cart

6. Update Items in User Cart :- http://127.0.0.1:8000/update_user_cart

7. Remove Items from User Cart :- http://127.0.0.1:8000/remove_user_cart

8. Get User Cart Details :- http://127.0.0.1:8000/getCart

9. Checkout User Cart :- http://127.0.0.1:8000/cartCheckOut

Note :- The details on each request could be found in the postman collection file ( -> Likeminds.postman_collection.json )