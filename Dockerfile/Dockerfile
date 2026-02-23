# Use the official Apache HTTP server as the base image
# FROM httpd:2.4
FROM python:latest
RUN pip install flask

# Copy custom website files into the Apache document root
# COPY ./public-html/ /usr/local/apache2/htdocs/
COPY ./static /home/microweb_app/static
COPY ./templates /home/microweb_app/templates
COPY ./flask_app.py /home/microweb_app/

# Expose port 80 to the host
EXPOSE 5050

# Default command to start Apache in the foreground
# CMD ["httpd-foreground"]
CMD python /home/microweb_app/flask_app.py
