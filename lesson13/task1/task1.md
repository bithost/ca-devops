# create redis flask application. Flask should be able to connect to redis database

https://collabnix.com/dockerize-an-api-based-flask-app-and-redis-using-docker-desktop/



curl localhost:5000


redis-cli -p 6379
>monitor

╭─ ~/ca-devops/lesson13/task1 │ on master !1 ······························· ✔ │ at 16:31:30 
╰─ redis-cli -p 6379
127.0.0.1:6379> keys *
1) "hits"
127.0.0.1:6379> KEYS *
1) "hits"
127.0.0.1:6379> TYPE hits
string
127.0.0.1:6379> GET hits
"3"
127.0.0.1:6379> GET hits
"4"
127.0.0.1:6379> 

https://medium.com/@volochkov/asynchronous-tasks-with-flask-rq-and-redis-in-docker-fcc61033e1b