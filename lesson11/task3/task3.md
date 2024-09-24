# Create container that writes data to docker volume

1. Get available volumes
```shell
tadas@code:~/academy/lesson11/task1$ docker volume ls
DRIVER    VOLUME NAME
local     volume_01
```

2. Create new volume
```shell
tadas@code:~/academy/lesson11/task3$ docker volume create data
data
tadas@code:~/academy/lesson11/task3$ docker volume ls
DRIVER    VOLUME NAME
local     data
local     volume_01
```

3. Run docker and attach that volume to it
```shell
tadas@code:~/academy/lesson11/task3$ docker run -it -d -v data:/data:rw ubuntu:22.04
```
4. Inspect volume to make sure it writes to it
```shell
tadas@code:~/academy/lesson11/task3$ docker volume inspect data
[
    {
        "CreatedAt": "2023-11-18T16:57:54Z",
        "Driver": "local",
        "Labels": null,
        "Mountpoint": "/var/lib/docker/volumes/data/_data",
        "Name": "data",
        "Options": null,
        "Scope": "local"
    }
]
tadas@code:~/academy/lesson11/task3$ sudo ls -lrs /var/lib/docker/volumes/data/_data
total 0
0 lrwxrwxrwx 1 www-data www-data 11 Nov  1 05:35 other_vhosts_access.log -> /dev/stdout
0 lrwxrwxrwx 1 www-data www-data 11 Nov  1 05:35 error.log -> /dev/stderr
0 lrwxrwxrwx 1 www-data www-data 11 Nov  1 05:35 access.log -> /dev/stdout

```
5. Connect to ubuntu writer container and run command
```shell
tadas@code:~/academy/lesson11/task3$ docker exec -it charming_fermat /bin/bash
```
```shell
root@951fb6f1fc03:/# while true; do echo "$(date +'%Y-%m-%d %H:%M:%S') - Some message" >> data/text.txt; sleep 5; done
```

6. Now let's run second container to read logs
```shell
tadas@code:~/academy/lesson11/task3$ docker exec -it ubuntu_reader /bin/bash
tadas@code:~/academy/lesson11/task3$ docker exec -it ubuntu_reader /bin/bash
root@f7ab21f86645:/# tail -f data/text.txt 
2023-11-18 18:06:52 - Some message
2023-11-18 18:06:57 - Some message
2023-11-18 18:07:02 - Some message
```

-------------------------
version: '3'

services:
  nginx:
    image: nginx
    ports:
      - "8080:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - data:/var/log/nginx


volumes:
  data:
    driver: local

----------------------
  error_log  /var/log/nginx/error.log;
http {
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    # Additional configuration goes here

    include /etc/nginx/conf.d/*.conf;
}
