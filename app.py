from flask import Flask, request, render_template
from datetime import datetime
from sqlalchemy import create_engine
import socket
import logging

ACCESS_PATH = "/var/www/access_logs/access.log"

logging.basicConfig(level=logging.DEBUG, filename=ACCESS_PATH, filemode='a+', format="[%(asctime)s-%(process)s-%(name)s] %(levelname)s: %(message)s")

app = Flask(__name__)

engine = create_engine('mysql+pymysql://admin:adminpass@db:3306/base')

now = datetime.now

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'GET':

    ip = request.remote_addr
    path = request.path
    host = request.host
    socket_host = socket.gethostname()

    logging.info(f'\n-----------------\nRequested Domain: {host}\nForwarded to Host: {socket_host}'
                  f'\nCaller IP Address: {ip}\nPath Requested: {path}\nTime: {now().isoformat()}'
                  f'\nAccess Route: {request.access_route}\nURL: {request.url}\nCookies: {request.cookies}'
                  f'\nFull Path: {request.full_path}\nReferrer: {request.referrer}\nUser Agent: {request.user_agent}')

    engine.execute(f"""INSERT INTO requests (requested_at, ip, host, requested_path)
	VALUES ('{now().strftime('%Y-%m-%d %H:%M:%S')}','{ip}', '{socket_host}', '{path}');
	""")

    result = engine.execute("SELECT * FROM requests ORDER BY id DESC LIMIT 25;")
    hf = result.keys()
    td = [i for i in result]

    return render_template('hello.html', header_fields=hf, table_data=td)

if __name__ == '__main__':
  app.run(host='0.0.0.0')
