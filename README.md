##FAST-FOOD-FAST
#### Travis-Badge
[![Build Status](https://travis-ci.org/Peace-Apple/Fast-Food-Fast.svg?branch=challenge2)](https://travis-ci.org/Peace-Apple/Fast-Food-Fast)

#### Coveralls-Badge
[![Coverage Status](https://coveralls.io/repos/github/Peace-Apple/Fast-Food-Fast/badge.svg?branch=challenge2)](https://coveralls.io/github/Peace-Apple/Fast-Food-Fast?branch=challenge2)

#### Codeclimate-Badge
[![Maintainability](https://api.codeclimate.com/v1/badges/44992971357dd65c83a0/maintainability)](https://codeclimate.com/github/Peace-Apple/Fast-Food-Fast/maintainability)

### About
This is a food service delivery app for a restaurant.

### Features
1. User can post a new order for food.
2. User can get a list of orders.
3. User can fetch a specific order.
4. User can update the order status.

### Links

#### Gh-pages:  
https://peace-apple.github.io/Fast-Food-Fast/

This link takes you where the user interface template is hosted on gh-pages.

#### Heroku: 

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
     virtualenv venv
     source /venv/bin/activate
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
|`/api/v1/orders/`                                    |GET   |Gets all orders              |
|`/api/v1/orders/<int:order_id>/`                     |GET   |Gets a specific specific order  |
|`/api/v1/orders/`                                    |POST  |Posts an order                        |
|`/api/v1/orders/<int:order_id>/`                     |PUT   |Updates the status of an order      |

#### Testing

- To run the tests, run the following commands

```bash
pytest
```

#### Built With

* [Flask](http://flask.pocoo.org/docs/1.0/) - The web framework used
* [Python](https://www.python.org/) - Framework language
* HTML
* CSS

## Authors

* **Peace Acio** - *Initial work* - [Peace-Apple](https://github.com/Peace-Apple)

## Acknowledgments

* Andela Uganda







