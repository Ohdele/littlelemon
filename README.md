# Little Lemon Restaurant Booking API Documentation

## Overview

This project focuses on building a backend API for the **Little Lemon Restaurant** to handle bookings and integrate with a **MySQL database**. The API allows users to make bookings, retrieve bookings, and delete bookings. This document outlines the steps taken to build the application, the architecture, and how it integrates with MySQL for data persistence.

## Key Features

1. **Database Integration**: The backend is connected to a MySQL database to store, retrieve, and delete booking data.
2. **Booking API**: RESTful API endpoints are provided to interact with the booking system.
3. **CRUD Operations**: The API supports Create, Read, Update, and Delete operations on bookings.
4. **User Interaction**: The API interacts with the frontend to allow users to make, view, and delete bookings.

## Tools & Technologies

- **Python**: The backend is built using Python.
- **Django**: Django framework is used for building the API.
- **Django Rest Framework (DRF)**: A toolkit for building Web APIs in Django.
- **MySQL**: Used to store booking data persistently.
- **Postman**: Used to test API endpoints.
- **Git**: Version control for tracking project changes.

## Setup Instructions

1. **Install Dependencies**: Install Python, Django, djangorestframework, and MySQL client using the following command:
    ```bash
    pip install django djangorestframework mysqlclient
    ```
2. **Database Configuration**: Set up MySQL on machine, create a database, and configure it in `settings.py`.
3. **Migrations**: Run the following commands to create database tables:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

## API Endpoints to Test

### 1. **GET /api/bookings/**

- **Description**: Retrieves the list of all bookings.
  **URL** http://127.0.0.1:8000/api/bookings/
- **Method**: GET
- **Response**: Returns a list of bookings in JSON format.

### 2. **POST /api/bookings/**

- **Description**: Creates a new booking.
- **Method**: POST
- **Request Body**:
    ```json
    {
        "name": "Ruben Diaz",
        "no_of_guests": 4,
        "booking_date": "2024-11-23T18:30:00Z"
    }
    ```
- **Response**: Returns the created booking data in JSON format.

### 3. **DELETE /api/bookings/{id}/**

- **Description**: Deletes a booking by ID.
- **Method**: DELETE
- **Response**: Returns HTTP status 204 if successful or HTTP status 404 if the booking is not found.

## Testing Instructions

- **Postman**: Use Postman to test the above API endpoints.
    - **GET**: Test retrieving bookings by sending a GET request to `/api/bookings/`.
    - **POST**: Test creating a booking by sending a POST request with booking data to `/api/bookings/`.
    - **DELETE**: Test deleting a booking by sending a DELETE request to `/api/bookings/{id}/` where `{id}` is the booking ID to delete.

## Conclusion

This project demonstrates how to connect a Django-based backend API to a MySQL database, allowing users to make, view, and delete bookings for the **Little Lemon Restaurant**. The project includes a fully functional RESTful API, tested using Postman.
