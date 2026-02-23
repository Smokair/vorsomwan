docker build -t netacad-nigeria-apache2 .
docker run -dit --name netacad-nigeria-app -p 8082:80 netacad-nigeria-apache2
