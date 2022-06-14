# ZidShip

Implementation for shipment gateway

## Technologies
-   Anaconda
-   Python
-   Django
-   Django Rest Framework
-   MySQL

## Postman collection
```https://www.getpostman.com/collections/f9dfc7d8150ca9d2f0cf```

# Useful Links:
## https://www.anaconda.com/products/distribution

# Installation
- Install Anaconda
    From link at Useful Links section, after installing Anaconda open anaconda prompt
    and install following packages using ``` conda install ``` command or using ``` pip ```
    - Install Django
        ``` pip install django ```
        ``` conda install django ```
    - Install Django Rest Framework
        ``` pip install djangorestframework ```
        ``` conda install djangorestframework```
    - Install MySQL
        ``` pip install mysql ```

## Run Steps
1- Clone repository:
```
git clone https://github.com/Andrew-Samir/shipment_gateway
```
2- Open Anaconda Prompt from start menu
3- Head to project directory
```
cd shipment_gateway
```
4- Migrate Database
```
python3 manage.py migrate
```
5- Run development server
```
python3 manage.py runserver
```
# Open API Documentation at: ```http://127.0.0.1:8000/```

