# Create network inside docker and make two containers to communicate

## Create network

1. List available docker networks
```shell
tadas@code:~/academy/lesson11/task1$ docker network list
NETWORK ID     NAME      DRIVER    SCOPE
9f0f4edcd56a   bridge    bridge    local
c45ed6207843   host      host      local
384db4d4f468   none      null      local
```
2. Create new secure docker network
```shell
tadas@code:~/academy/lesson11/task1$ docker network create secure-net
28159cb722a222203c7c899fd9f9182e61be78cfed5c91582ecad5df467703fb
tadas@code:~/academy/lesson11/task1$ docker network list
NETWORK ID     NAME         DRIVER    SCOPE
9f0f4edcd56a   bridge       bridge    local
c45ed6207843   host         host      local
384db4d4f468   none         null      local
28159cb722a2   secure-net   bridge    local
```
3. Create two new containers and assign this secure network
```shell
tadas@code:~/academy/lesson11/task1$ docker run --rm --net secure-net --name secure_nginx -d nginx
tadas@code:~/academy/lesson11/task1$ docker run --net tulip-net -it busybox sh
```
4. Get docker cintainer IP to test 
```shell
tadas@code:~/academy/lesson11/task1$ docker inspect secure_nginx | grep "IPAddress"
            "SecondaryIPAddresses": null,
            "IPAddress": "",
                    "IPAddress": "172.18.0.2",
tadas@code:~/academy/lesson11/task1$ docker inspect clever_banach | grep "IPAddress"
            "SecondaryIPAddresses": null,
            "IPAddress": "172.17.0.2",
                    "IPAddress": "172.17.0.2",
tadas@code:~/academy/lesson11/task1$ docker inspect intelligent_borg | grep "IPAddress"
            "SecondaryIPAddresses": null,
            "IPAddress": "",
                    "IPAddress": "172.18.0.3",
```
5. Running ping to see who can ping
```shell
tadas@code:~/academy/lesson11/task1$ docker run --net secure-net -it busybox sh
/ # ping 172.17.0.2
PING 172.17.0.2 (172.17.0.2): 56 data bytes
^C
--- 172.17.0.2 ping statistics ---
4 packets transmitted, 0 packets received, 100% packet loss
/ # ping 172.18.0.2
PING 172.18.0.2 (172.18.0.2): 56 data bytes
64 bytes from 172.18.0.2: seq=0 ttl=64 time=0.111 ms
64 bytes from 172.18.0.2: seq=1 ttl=64 time=0.063 ms
64 bytes from 172.18.0.2: seq=2 ttl=64 time=0.068 ms
64 bytes from 172.18.0.2: seq=3 ttl=64 time=0.092 ms
^C
--- 172.18.0.2 ping statistics ---
4 packets transmitted, 4 packets received, 0% packet loss
round-trip min/avg/max = 0.063/0.083/0.111 ms
/ # exit
```