# Default Dockerfile
FROM 982466450/deepface:latest
LABEL maintainer="developers <zly@982466450.com>" version="1.0.0"

COPY ./start.sh /deepface/start.sh
COPY ./app.py /deepface/app.py
COPY ./1.jpg /deepface/1.jpg
COPY ./2.jpg /deepface/2.jpg

EXPOSE 5000
WORKDIR /deepface

CMD ["/deepface/start.sh"]
