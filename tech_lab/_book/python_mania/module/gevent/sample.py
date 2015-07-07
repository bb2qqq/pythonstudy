import gevent
from gevent import socket
from gevent import Greenlet
urls = ['www.google.com', 'www.example.com', 'www.python.org', 'www.zengjuchen.info']
jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]
gevent.joinall(jobs, timeout=3)
print [job.value for job in jobs]


class MyNoopGreenlet(Greenlet):
    def __init__(self, seconds):
        Greenlet.__init__(self)
        self.seconds = seconds

    def _run(self):
        gevent.sleep(self.seconds)

    def __str__(self):
        return 'MyNoopGreenlet(%s)' % self.seconds
