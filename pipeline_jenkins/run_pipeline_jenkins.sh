docker run --rm --privileged -p 8080:8080 -v jenkins-data:/var/jenkins_home \
-v $(which docker):/usr/bin/docker -v /var/run/docker.stock:/var/run/docker.sock \
-v "$HOME":/home --name jenkins_server jenkins/jenkins:lts7


