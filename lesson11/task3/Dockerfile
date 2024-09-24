FROM php:8.0-apache

# Create a directory for logs in the 'data' volume
RUN mkdir -p /var/log/apache2 && \
    ln -sf /dev/stdout /var/log/apache2/access.log && \
    ln -sf /dev/stderr /var/log/apache2/error.log

# Copy the contents of the 'source' directory to the Apache document root
COPY source/ /var/www/html

# Expose port 80
EXPOSE 83