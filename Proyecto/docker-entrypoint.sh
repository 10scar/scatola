#!/bin/bash

if [ "$DATABASE" = "mysql" ]
then
    echo "Waiting for mysql..."
    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done
    echo "MySQL started"
fi

echo "Appling database migrations..."
python manage.py makemigrations 
python manage.py migrate

echo "Building Tailwind CSS..."
python manage.py tailwind install
python manage.py tailwind build

echo "Poblando la base de datos con el temario..."
python manage.py shell -c "from preguntas.carga import temario; temario.poblar_datos()"

echo "Creando dos usuarios por defecto ..."
python manage.py shell -c "from usuarios.carga import users_default; users_default.poblar_datos()"

exec "$@"