#!/bin/bash

# Archivo de bandera para saber si la configuración inicial ya se realizó
FLAG_FILE=".setup_complete"


# Si el archivo de bandera no existe, es la primera vez que se ejecuta
if [ ! -f "$FLAG_FILE" ]; then
  echo "----------------------------------------------------"
  echo "Realizando configuración inicial (primera ejecución)..."
  echo "----------------------------------------------------"
  
  # Iniciar los contenedores en segundo plano
  echo "Levantando los servicios con Docker Compose..."
  docker compose --env-file .env.dev up --build 




  # Crear el archivo de bandera para no volver a ejecutar esto
  #touch $FLAG_FILE
  echo "\nConfiguración inicial completada."

else
  echo "----------------------------------------------------"
  echo "La configuración inicial ya se ha realizado."
  echo "Solo se levantará el servidor."
  echo "----------------------------------------------------"
  docker-compose up -d
fi

# Mostrar la URL para acceder al proyecto
echo "\n----------------------------------------------------"
echo "✅ ¡Proyecto listo!"
echo "Puedes acceder a la aplicación en:"
echo "👉 http://localhost:8000"
echo "----------------------------------------------------"
