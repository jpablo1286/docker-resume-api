if [ "$1" == "dev" ];
then
  cp Dockerfile-dev Dockerfile
  sudo docker build -t resume-api:latest ./
  sudo docker run --rm --name resume-api -p 8000:8000 -v "$(pwd)"/api/:/opt/resume-api/api resume-api:latest
else
  cp Dockerfile-prod Dockerfile
  sudo docker build -t resume-api:latest ./
  sudo docker run --rm --name resume-api -p 8000:8000 resume-api:latest
fi
