# Vendor-Management-System

The repository contains a Django REST API Framework with Django rest framework

## Prerequisite

- Python version (3x recommended)
- Django version 3.2.9
- Django rest framework

# Setup instruction

## Create a Virtual Environment:
- pip install virtualenvwrapper-win
- mkvirualenv environmentname

## Installing django version

  pip install django.
  pip install django-rest_frameowrk.

## To create django project and app
  - django-admin startproject Vendorsystem.
  - cd Vendorsystem.
  - python manage.py startapp Vendor.
## Superuser creation and Token generation
   - python manage.py createsuperuser
   - curl -X POST -d "username=your_superuser_username&password=your_superuser_password" http://localhost:8000/api-token-auth/

## To run the server

   Python manage.py runserver

## External database tool to connect django project

   Postgresql version x64

## Setup for connecting django project to database.

   - 'ENGINE': 'django.db.backends.postgresql',
        - 'NAME': 'Database Name',
        - 'USER': 'postgres',
        - 'PASSWORD': 'Password',
        - 'HOST': 'localhost'
    
## Access Django Admin:
Open the Django admin at http://127.0.0.1:8000/admin/ and log in using the superuser credentials. this is to access the database as a admin user.

## how to run a api endpoint:
- first we need to make sure that we migrated the models to database
- then we need to start the server using "python manage.py runserver" command.
- then we need to open another cmd prompt and open virtual environment and open the project folder and provide curl or httpie commands.

## API Endpoints

   ### Vendor Profile Management

      ● POST /api/vendors/: Create a new vendor.
      ● GET /api/vendors/: List all vendors.
      ● GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.
      ● PUT /api/vendors/{vendor_id}/: Update a vendor's details.
      ● DELETE /api/vendors/{vendor_id}/: Delete a vendor.

  ### Purchase Order Tracking

      ● POST /api/purchase_orders/: Create a purchase order.
      ● GET /api/purchase_orders/: List all purchase orders with an option to filter by vendor.
      ● GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
      ● PUT /api/purchase_orders/{po_id}/: Update a purchase order.
      ● DELETE /api/purchase_orders/{po_id}/: Delete a purchase order.

  ### Performance Evaluation

      ● GET /api/vendors/{vendor_id}/performance: Retrieve a vendor's performance metrics

  ### About this API endpoint:
  
  - here this endpoint is used to retrieve the performance metrics of a vendor with given vendor_id. this performance metrics contains on_time Delivery rate, quality rating average, 
    average response time, fulfilment rate
  - On time delivery rate is calculated each time a PO status changes to "completed". this is the average of no of po delivered before the delivery_date and no of total po's 
    delivered.
  - quality rating average is calculated after every po completion and it is the average of all ratings given to that specific vendor.
  - average response time is calculated each time a po is acknowledged by the vendor. it is the time difference between issue_date and acknowledgment_date for each po, and then the 
    average of these times for all po's of the vendor.
  - fulfillment rate is calculated when po status is set to "completed". this is the average of no of successfully fulfilled pos (status = "completed" without issues) by the total no 
    of pos issued to the vendor.

[django_developer_assignment.pdf](https://github.com/pramo22/Vendor-Management-System/blob/master/django_developer_assignment.pdf)
