# demo-django-celery

Prueba de django junto a celery sobre dokku.


## Instrucciones

Primero, se tiene que realizar un deploy sobre dokku así:


```
git remote add dokku dokku@enjambrelab.com.ar:demo-django-celery
```

Una vez creada la aplicación, se podría instalar y configurar redis para que
lo pueda utilizar la aplicación.


Desde un acceso como root, hay que instalar el plugin de redis:

```
dokku plugin:install https://github.com/dokku/dokku-redis.git redis
```


y para vincular la base de datos redis a la aplicación:

```
dokku redis:create redis-for-demo-django-celery
dokku redis:link redis-for-demo-django-celery demo-django-celery
```	

Luego, hay que inicializar los servicios de celery:

```
dokku ps:scale worker=2
```

y forzar al menos un commit para volver a realizar el deploy:

```
git commit --allow-empty -m "Forzando deploy."
```


