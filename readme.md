# Solid Jelly

**Repo for the engine to track specific cryto currency markets.**

___

## Preparing : 

0. Clone the repo
1. Copy `env.txt` to `app/.env`
2. Change the specific fields in `app/.env`
3. Update the entrypoint.sh file permissions locally, run: `$ chmod +x app/entrypoint.sh`
4. Build the image, run: `$ docker-compose build`
4. Run the container, run : `$ docker-compose up -d`
5.  Follow outputs alive and track errors, to make continuous development, run: `$ docker logs --follow web-app`

"""
### API Endpoints :

**This API only works for `BTCUSDT` and `ETHUSDT` markets for now**

To check last 24h (daily) statistics of BTCUSDT market : 
```
GET> http://localhost:8006/trader/btcusdt/1/
```

To check last week (weekly) statistics of BTCUSDT market : 
```
GET> http://localhost:8006/trader/btcusdt/7/
```

To check last month (monthly) statistics of BTCUSDT market : 
```
GET> http://localhost:8006/trader/btcusdt/30/
```

To check last 24h (daily) statistics of ETHUSDT market : 
```
GET> http://localhost:8006/trader/ethusdt/1/
```

To check last week (weekly) statistics of ETHUSDT market : 
```
GET> http://localhost:8006/trader/ethusdt/7/
```

To check last month (monhly) statistics of ETHUSDT market : 
```
GET> http://localhost:8006/trader/ethusdt/30/
```

## Usefull Commands

```
# Start services at background :
    $ docker-compose up -d --build
```

```
# Follow outputs alive and track errors, to make continuous development : 
    $ docker logs --follow web-app
```

```
# One-shot command :  
    $ docker-compose up -d --build; docker logs --follow web-app
```

```
# Build the image: 
    $ docker-compose build
```

```
# Once the image is built, run the container : 
    $ docker-compose up -d
```

```
# Build the new image and spin up the two containers:
    $ docker-compose up -d --build
```

```
Run the migrations:
    $ docker-compose exec web python manage.py migrate --noinput
```

```
To remove the volumes along with the containers :
    $ docker-compose down -v
```

```
Ensure the default Django tables were created: 
    $ docker-compose exec db psql --username=enivicivokki_user --dbname=enivicivokki_db
    # \l
    # \c enivicivokki_db
    # \dt
    # \q
```

```
# You can check that the volume was created as well by running:
    $ docker volume inspect django-on-docker_postgres_data
```

```
# Run migrations manually : 
    $ docker-compose exec web python manage.py flush --no-input
    $ docker-compose exec web python manage.py migrate
```


