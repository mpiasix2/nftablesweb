FROM python:3.8-slim-buster

RUN apt-get update && apt-get upgrade -y
RUN apt-get install ssh -y &&
RUN apt-get install iputils-ping -y &&
RUN apt-get install nano -y &&
RUN apt-get install sshpass -y &&
RUN ansible-galaxy collection install ansible.posix

RUN mkdir -p /root/.ssh && chmod 0700 /root/.ssh
RUN test -f /root/.ssh/id_rsa || (ssh-keygen -t rsa -N "" -f /root/.ssh/id_rsa)
RUN chmod 0600 /root/.ssh/id_rsa
RUN chown root:root /root/.ssh/id_rsa

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --no-cache-dir
COPY . .

EXPOSE 80
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:app"]
