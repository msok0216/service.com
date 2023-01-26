FROM python:3.8
# RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
ENV FLASK_APP=backend
ENV PYTHONUNBUFFERED 1
EXPOSE 5000
ADD . ./backend
CMD ["flask", "--debug","run", "-h", "0.0.0.0"]