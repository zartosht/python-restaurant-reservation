# Restaurant Reservation System

This is a REST API built with Django for managing reservations at various restaurants. The system allows users to create, update, and delete reservations, and administrators can manage the restaurant information.

## Description

This project is designed to provide a seamless reservation experience for both customers and restaurant administrators. Customers can easily reserve tables at their favorite restaurants, while administrators can update restaurant details and manage reservations.

## Getting Started

### Dependencies

- Docker
- Docker Compose

Ensure you have Docker and Docker Compose installed on your system. If not, you can download them from [Docker's official website](https://www.docker.com/products/docker-desktop).

### Installation

To set up your local development environment, please follow the steps below:

1. Clone the repository:
    ```bash
    git clone https://github.com/zartosht/python-restaurant-reservation.git
    cd python-restaurant-reservation
    ```

2. Create a `.env` file at the root of your project directory and add the necessary environment variables:
    ```env
    DEBUG=1
    POSTGRES_DB=postgres
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_HOST=db
    POSTGRES_PORT=5432
    ```

### Executing Program

To get your environment up and running, follow these steps:

1. Start all services using Docker Compose:
    ```bash
    docker-compose up --build
    ```

2. After the services have started, apply the migrations:
    ```bash
    docker-compose exec web python manage.py migrate
    ```

3. Create a superuser to access the Django admin:
    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```

4. Access the application by navigating to:
    ```
    http://localhost:8000
    ```

5. To stop the application, use the following command:
    ```bash
    docker-compose down
    ```

## Help

If you encounter any issues, please check if your Docker services are running correctly and that all environment variables are set properly.

## Authors

Contributors names and contact info:

- Your Name  
- Contact Info

## Version History

- 0.1
    - Initial Release

## License

This project is licensed under the [MIT License](LICENSE.txt) - see the LICENSE file for details.

## Acknowledgments

Here are some resources that have been invaluable in the creation of this project:

- [Django Documentation](https://docs.djangoproject.com/en/3.2/)
- [Django REST Framework Documentation](https://www.django-rest-framework.org/)
- [Docker Documentation](https://docs.docker.com/)
- [PostgreSQL](https://www.postgresql.org/)
