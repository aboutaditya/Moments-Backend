# Moments-Backend

Moments Backend is a backend service for a photo-sharing iOS app that allows users to create events, upload photos, and manage albums. Built with **Django**, **Django REST Framework (DRF)**, and using **PostgreSQL** as the database, the app features JWT-based authentication for secure interactions.

## Features

- **User Registration & Authentication** (JWT)
- **Create Events** with QR Code Generation
- **Upload Photos** to Events
- **View Photos** for a Specific Event
- **Secure Endpoints** with Role-Based Access Control (RBAC)

## Technologies Used

- **Backend**: Django 5.1, Django REST Framework (DRF)
- **Database**: PostgreSQL
- **Authentication**: JWT (djangorestframework-simplejwt)
- **Optional**: Docker for containerization
- **iOS App**: Swift (for Moments iOS integration)

## Prerequisites

- **Python**: 3.11+
- **PostgreSQL**: Installed and running

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/your-username/moments-backend.git
cd moments-backend
