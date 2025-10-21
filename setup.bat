@echo off
REM Archivo de bandera para saber si la configuración inicial ya se realizó
set FLAG_FILE=.setup_complete

REM Si el archivo de bandera no existe, es la primera vez que se ejecuta
if not exist "%FLAG_FILE%" (
  echo ----------------------------------------------------
  echo Realizando configuracion inicial (primera ejecucion^)...
  echo ----------------------------------------------------
  
  REM Iniciar los contenedores en segundo plano
  echo Levantando los servicios con Docker Compose...
  docker compose --env-file .env.dev up --build
  
  
  
  
  REM Crear el archivo de bandera para no volver a ejecutar esto
  REM type nul > %FLAG_FILE%
  echo.
  echo Configuracion inicial completada.
  
) else (
  echo ----------------------------------------------------
  echo La configuracion inicial ya se ha realizado.
  echo Solo se levantara el servidor.
  echo ----------------------------------------------------
  docker-compose up -d
)

REM Mostrar la URL para acceder al proyecto
echo.
echo ----------------------------------------------------
echo [32m✓[0m Proyecto listo!
echo Puedes acceder a la aplicacion en:
echo http://localhost:8000
echo ----------------------------------------------------
