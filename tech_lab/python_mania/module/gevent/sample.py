import gevent
from gevent import socket
urls = ['www.google.com', 'www.example.com', 'www.python.org', 'www.zengjuchen.info']
jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]
gevent.joinall(jobs, timeout=3)
print [job.value for job in jobs]
