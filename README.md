##FAST-FOOD-FAST
#### Travis-Badge


#### Coveralls-Badge


#### Codeclimate-Badge


### About
This is a food service delivery app for a restaurant.

### Features
a. Create user accounts that can signin/signout from the app.
b. Client can place an order for food.
c. Admin can get list of orders.
d. Admin can get a specific order.
e. Admin can update the status of an order.
f. Client can get the menu.
g. Admin can add food option to the menu.
h. User can view the order history 

### Links

#### Gh-pages:  
https://peace-apple.github.io/Fast-Food-Fast/

This link takes you where the user interface template is hosted on gh-pages.

#### Heroku: 

This link takes you to the api that is hosted on heroku.

### Getting Started 
The following will get you started
#### Prerequisites
You will need to install the following

```bash
- git : To clone, update and make commits to the repository
- python3: The base language used to develop the api
- pip: A python package used to install project requirements
```
#### Installation
The ft-challenge-one folder houses the user interface. To access the user interface, open the index.html.
The ft-challenge-two folder contains the system backend services.
- To install the requirements, run:
- [Python](https://www.python.org/) A general purpose programming language
- [Pip](https://pypi.org/project/pip/) A tool for installing python packages
- [Virtualenv](https://virtualenv.pypa.io/en/stable/)  A tool to create isolated Python environments

#### Development setup
- Create a virtual environment and activate it
    ```bash
     Create: virtualenv venv
     On windows: source /venv/scripts/activate
     On linux: /venv/bin/activate
     
    ```
- Install dependencies 
    ```bash
    pip3 install -r requirements.txt
    ```
- Run the application
    ```bash
    cd Fast-Food-Fast
    python run.py
    ```
- Thereafter you can access the system api Endpoints:

| End Point                                           | Verb |Use                                       |
| ----------------------------------------------------|------|------------------------------------------|
|`/api/v2/auth/signup/`                               |POST  |User signup                         |
|`/api/v2/auth/login/`                                |POST  |User login                          |
|`/api/v2/users/orders/`                              |POST  |Posts an order for food             |
|`/api/v2/users/orders/               `               |GET   |Gets the order history for a particular user|
|`/api/v2/orders/`                                    |GET   |Retrieves all orders          |
|`/api/v2/orders/<int:order_id>/`                     |GET   |Retrieves a specific order          |
|`/api/v2/orders/<int:order_id>/`                     |PUT   |Updates the status of an order      |
|`/api/v2/menu/`                                      |GET   |Gets menu items      |
|`/api/v2/menu/`                                      |POST  |Adds menu items     |

#### Testing

- To run the tests, run the following commands

```bash
pytest --cov
```

#### Built With

* [Flask](http://flask.pocoo.org/docs/1.0/) - The web framework used
* [Python](https://www.python.org/) - Framework language
* HTML
* CSS

## Authors

* **Peace Acio** - *Initial work* - [Peace-Apple](https://github.com/Peace-Apple)

## Acknowledgments

* Andela Software Development Community








