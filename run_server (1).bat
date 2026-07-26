@echo off
echo Starting Medicard WebVR Server...
echo Address: http://localhost:8080
start "" http://localhost:8080
python -m http.server 8080
pause
