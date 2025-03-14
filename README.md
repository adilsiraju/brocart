# Brocart (E-Commerce)
![image](https://github.com/user-attachments/assets/69eb1880-192c-4c03-a332-829eb4c23338)

Brocart is a minimal Django-based e-commerce application that demonstrates basic functionalities of an online store. It includes features for managing products, customers, and orders.

## Key Features
- **Product Management**: Add, edit, and delete products with fields such as title, price, description, and image.
- **Customer Management**: Manage customer profiles linked to Django’s built-in User model.
- **Order Processing**: Create and manage orders with different statuses like "Processed" and "Delivered".
- **Admin Integration**: Utilize Django’s admin interface for easy management of products, customers, and orders.
- **Media Handling**: Upload and manage product images using Django’s ImageField.

## Project Structure
- **brocart/**: Main Django project folder containing settings, URLs, and WSGI configuration.
  - **settings.py**: Configuration for the Django project, including installed apps and database settings.
  - **urls.py**: URL routing for the project.
  - **wsgi.py**: WSGI configuration for deployment.
- **customers/**: App for managing customer data.
  - **models.py**: Defines the Customer model.
  - **views.py**: Views for handling customer-related requests.
- **orders/**: App for managing orders.
  - **models.py**: Defines the Order and OrderedItem models.
  - **views.py**: Views for handling order-related requests.
- **products/**: App for managing products.
  - **models.py**: Defines the Product model.
  - **views.py**: Views for handling product-related requests.
  - **urls.py**: URL routing for product-related views.
- **static/**: Directory for static files like CSS and images.
- **templates/**: Directory for HTML templates.
  - **blank_layout.html**: Base layout template.
  - **index.html**: Home page template.
  - **products.html**: Template for listing products.
  - **product_detail.html**: Template for product details.
- **themes/**: App for managing site themes.
  - **models.py**: Defines the SiteSettings model.

## Notable Files
- **manage.py**: Command-line utility for administrative tasks.
- **db.sqlite3**: SQLite database file.
- **.gitignore**: Specifies files and directories to be ignored by Git.

## Templates
- **navbar.html**: Navigation bar template.
- **products_list_content.html**: Template for displaying a list of products.
- **home_content.html**: Template for the home page content.
- **hero.html**: Template for the hero section on the home page.

## Static Files
- **css/style.css**: Stylesheet for the application.
- **images/**: Directory for image files used in the application.

Feel free to explore and extend this project to suit your needs.
