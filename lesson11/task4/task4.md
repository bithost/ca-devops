# Create a docker file that run as non root user
docker build -t apache_user .

docker run --rm -it -d -p 84:80/tcp apache_user:latest 


root@e29a275f8fec:/var/www/html# ps aux | grep apache
root           1  0.3  0.5  78080 23284 pts/0    Ss+  18:28   0:00 apache2 -DFOREGROUND
www-data      18  0.0  0.1  78112  7212 pts/0    S+   18:28   0:00 apache2 -DFOREGROUND
www-data      19  0.0  0.1  78112  7212 pts/0    S+   18:28   0:00 apache2 -DFOREGROUND
www-data      20  0.0  0.1  78112  7212 pts/0    S+   18:28   0:00 apache2 -DFOREGROUND
www-data      21  0.0  0.1  78112  7212 pts/0    S+   18:28   0:00 apache2 -DFOREGROUND
www-data      22  0.0  0.1  78112  7212 pts/0    S+   18:28   0:00 apache2 -DFOREGROUND


changing to USER www-data
www-data       1  0.2  0.6  78080 23748 pts/0    Ss+  18:29   0:00 apache2 -DFOREGROUND
www-data      17  0.0  0.1  78112  7220 pts/0    S+   18:29   0:00 apache2 -DFOREGROUND
www-data      18  0.0  0.1  78112  7220 pts/0    S+   18:29   0:00 apache2 -DFOREGROUND
www-data      19  0.0  0.1  78112  7220 pts/0    S+   18:29   0:00 apache2 -DFOREGROUND
www-data      20  0.0  0.1  78112  7220 pts/0    S+   18:29   0:00 apache2 -DFOREGROUND
www-data      21  0.0  0.1  78112  7220 pts/0    S+   18:29   0:00 apache2 -DFOREGROUND
www-data      38  0.0  0.0   3240   648 pts/1    S+   18:29   0:00 grep apache