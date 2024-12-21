# Project: Django REST API for Product, Discount, and Order Management

## Overview
This project is a Django-based REST API system designed to handle:

1. **Product Management**
   - Different product types with unique pricing rules.
   - Real-time pricing calculations based on product type and quantity.

2. **Discount Management**
   - Flexible discount types with priority-based application.
   - Tiered discounts for quantity-based and value-based discounts.

3. **Order Management**
   - Dynamic order total calculation based on products and discounts.
   - Multi-product and multi-discount support.

4. **RESTful API Implementation**
   - Endpoints for managing products, discounts, and orders.

 
### Setup
1. **Run the server**:
   ```bash
   python manage.py runserver
   ```
2. **Use Postman or cURL** to test the endpoints.

### Test Cases
1. **Add a Product**:
   - Endpoint: `POST /api/products/`
   - Body:
     ```json
     {
         "name": "Winter Jacket",
         "base_price": 100.0,
         "product_type": "seasonal"
     }
     ```
2. **Get Product Price**:
   - Endpoint: `GET /api/products/{id}/get_price/?quantity=25`

3. **Add an Order**:
   - Endpoint: `POST /api/orders/`
   - Body:
     ```json
     {
         "products": [
             {"id": 1, "quantity": 25},
             {"id": 3, "quantity": 1}
         ],
         "discounts": [1, 2]
     }
     ```

4. **Retrieve Order Total Price**:
   - Endpoint: `GET /api/orders/{id}/total_price/`

## How to Run Locally
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Start the development server:
   ```bash
   python manage.py runserver
   ```

## License
This project is open-source and available under the MIT License.

