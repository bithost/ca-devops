FROM php:8.0-apache

COPY source/ /var/www/html
# Ensure that www-data has the right permissions on /var/www/html
RUN chown -R www-data:www-data /var/www/html

# Switch to the www-data user, a non-root user for security

USER www-data
# Set the entrypoint for the container
EXPOSE 84