# Step 1  install required python packages

pip install requirements.txt

# Step 2  Runserver to http://127.0.0.1:8000

python manage.py runserver

# Step 3  hit the end point  and upload photo

curl -X POST  -F "image=photo.png"  http://127.0.0.1:8000/api/
  
# Step 4 you will get the response with a audio link . Which alert the man about nearest Car

{"audio": "http://127.0.0.1:8000/media/voices/fc08c6c0-e7d3-4566-a40f-f46984a2019b.mp3"}
