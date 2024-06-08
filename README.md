# propertyfy

## Overview
Created Full Stack web application using Django for listing the real estate properties. On this web application allow users to sell, rent, or lease properties such as apartments, flats, and bungalows. The application includes user authentication and autherisation, CRUD operations for property listings, a contact form for inquiries, and an integrated map to display property locations using TomTom geocoder and map services.

## Features

   1. User Authentication: Users can sign up, log in, and change their passwords.
   2. Property Listings: Users can create, view, update, and delete property listings with details such as title, description, address, price, and type (sell, rent, lease).
   3. Contact Us Form: Users can fill out a form with their name, email, subject, and message to send inquiries or feedback. These inquiries are sent to the admin via Mailtrap.
   4. Property Map: The application converts property addresses into latitude and longitude using TomTom geocoder and displays all properties on a map using TomTom map services.


## Technology Stack

    Django: Web framework used to build the application.
    SQLite: Database used to store user and property data.
    WTForms: Library used for form handling.
    Geocoder: Used to convert property addresses into latitude and longitude.
    TomTom Maps: Used to display property locations on an interactive map.
    Mailtrap: Email service used to handle inquiry submissions.
    HTML/CSS: Front-end design and styling.

## Detailed Functionality

   1. User Authentication
        Sign Up: Users can create an account by providing a username, email, and password.
        Log In: Registered users can log in using their credentials.
        Change Password: Logged-in users can change their password.

   2. Property Listings
        Create: Users can list a property by providing details such as title, description, address, price, and type (sell, rent, lease).
        Read: Users can view detailed information about each property.
        Update: Users can edit the details of an existing property listing.
        Delete: Users can remove a property listing from the database.

   3. Contact Us Form
        Users can submit inquiries or feedback through the contact form with the following details:
            Name
            Email
            Subject
            Message
        Upon submission, the inquiry is sent to the admin using the Mailtrap email service.

   4. Property Map
        When listing a property, the address is converted into latitude and longitude using the TomTom geocoder.
        All listed properties are displayed on an interactive map using TomTom map services.
