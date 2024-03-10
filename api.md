# API DOCUMENTATION

## Ecommerce Backend

This project contains APIs for an Ecommerce website. It includes logic(django apps) such as Accounts, Order, Product. while the django project named backend contains configuration of settings and urls.

BASE_URL = https://e-commerce-backend-fe1r.onrender.com/ or http://127.0.0.1:8000/ depending on whether you are using the deployed api or you cloned the repository

## Authentication Endpoints

### Obtain JWT Token
- **URL:** `/api/token/`
- **Method:** POST
- **Description:** Endpoint to obtain JWT token by providing valid credentials.
- **Parameters:**
  - `username`: User's username
  - `password`: User's password
- **Response:** JWT token on successful authentication.

### Refresh JWT Token
- **URL:** `/api/token/refresh/`
- **Method:** POST
- **Description:** Endpoint to refresh JWT token.
- **Parameters:**
  - `refresh`: Refresh token
- **Response:** New JWT token on successful refresh.

## User Management Endpoints

### User Registration
- **URL:** `/api/signup/`
- **Method:** POST
- **Description:** Endpoint to register a new user.
- **Parameters:**
  - `username`: User's username
  - `email`: User's email address
  - `password`: User's password
  - `first_name`: User's first name
  - `last_name`: User's last name
- **Response:** User data along with JWT token on successful registration.

## Product Endpoints

### List Latest Products
- **URL:** `/api/latest-products/`
- **Method:** GET
- **Description:** Endpoint to retrieve a list of latest products.
- **Response:** List of latest products.

### Search Products
- **URL:** `/api/products/search/`
- **Method:** GET
- **Description:** Endpoint to search for products.
- **Parameters:**
  - `query`: Search query
- **Response:** List of products matching the search query.

### Product Detail
- **URL:** `/api/products/<category_slug>/<product_slug>/`
- **Method:** GET
- **Description:** Endpoint to retrieve details of a specific product.
- **Response:** Details of the requested product.

### Category Detail
- **URL:** `/api/products/<category_slug>/`
- **Method:** GET
- **Description:** Endpoint to retrieve details of products within a specific category.
- **Response:** Details of products within the requested category.

## Order Endpoints

### Checkout
- **URL:** `/api/checkout/`
- **Method:** POST
- **Description:** Endpoint to process order checkout.
- **Parameters:**
  - Order details
- **Response:** Order confirmation.

### List Orders
- **URL:** `/api/orders/`
- **Method:** GET
- **Description:** Endpoint to retrieve a list of user orders.
- **Response:** List of user orders.

## API Schema and Documentation

### Swagger Schema
- **URL:** `/schema/`
- **Method:** GET
- **Description:** Endpoint to retrieve the API schema in JSON format.

### Swagger Documentation
- **URL:** `/schema/docs/`
- **Method:** GET
- **Description:** Endpoint to access interactive API documentation using Swagger UI.

## Connecting to the Frontend
To connect your frontend to the backend API:
1. Make sure your frontend application can send HTTP requests to the backend API endpoints using libraries like Axios or Fetch.
2. Use the provided API endpoints to perform user authentication, retrieve product information, and manage orders.
3. Handle JWT token management on the frontend side, including storing tokens securely and sending them with each request to protected endpoints.
4. Implement frontend views and components to interact with the API responses and display relevant data to users.

