###  Docker MySQL Test Database
This will create a test MySQL database instance to verify SQL to Pandas statement result. 

### To Start Mysql Docker
* Run following command
```bash
$ cd docker
$ docker-compose -f mysql.yml up
```

### Log into PhpMyAdmin
* http://localhost:8183/
* username: `root` and password is `root`
* Note: no need to fill in the hostname part