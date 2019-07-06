FROM python:alpine3.7

WORKDIR /var/www

RUN apk update && apk upgrade && apk add bash nano build-base libffi-dev openssl-dev \
#	&& pip install poetry \
#	&& python -m venv app_env && source app_env/bin/activate \
#	&& poetry completions bash > /etc/bash_completion.d/poetry.bash-completion \
#	&& poetry new py_poet \
#	&& cd py_poet \
#	&& poetry add flask \
#	&& poetry install \
	&& pip install flask \
	&& pip install sqlalchemy>=1.2.9 \
	&& pip install pymysql \
	&& pip install cryptography

#CMD "source /var/www/app_env/bin/activate"
#CMD "python /var/www/app.py"
