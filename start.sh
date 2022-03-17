#!/bin/bash

echo
echo "[Info]: Maintainer: Hosein Yousefi <yousefi.hosein.o@gmail.com>"
echo

echo "!!!PAY ATTENTION!!!"
echo "[Info]: this script just for the initializing."
echo "[Info]: do not run it on second time."
echo
sleep 3

echo "[Info]: initial droput authentication setup"
sleep 1
echo

cd droput_authentication
python3 -m venv venv
. venv/bin/activate

echo "[Info]: installing python requirements"
sleep 1

pip install -r requirements.txt 1> /dev/null

echo "[Info]: initializing database"
sleep 2

flask db init 1> /dev/null
flask db migrate -m "init" 1> /dev/null
flask db upgrade &> /dev/null

echo "[Info]: run unit test"
sleep 2

coverage run -m pytest 1> /dev/null

echo "[Info]: run application"
sleep 2

flask run & 1> /dev/null
cd ..
sleep 2

echo
echo "[Info]: initial droput authentication setup"
sleep 1
echo

cd droput_message
python3 -m venv venv
. venv/bin/activate

echo "[Info]: installing python requirements"
sleep 1

pip install -r requirements.txt 1> /dev/null

echo "[Info]: initializing database"
sleep 2

flask db init 1> /dev/null
flask db migrate -m "init" 1> /dev/null
flask db upgrade &> /dev/null

echo "[Info]: run unit test"
sleep 2

coverage run -m pytest 1> /dev/null

echo "[Info]: run application"
sleep 2

flask run -p 5001 & 1> /dev/null
cd ..
sleep 2

echo
echo "!!!  ALL SET  !!!"
echo "droput authentication listen on port 5000"
echo "droput message listen on port 5001"
echo 
echo "You are able to read ApiCommands file to call suitable APIs."
echo "enjoy!"
echo
