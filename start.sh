sudo docker build -t resume-api:latest ./
sudo docker run --rm --name resume-api -p 8000:8000 -v "$(pwd)"/api/:/opt/resume-api/api resume-api:latest
