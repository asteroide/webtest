from flask import Flask
from flask_restful import Resource, Api
import logging, random, string

app = Flask(__name__)
api = Api(app)


class ROOT(Resource):
    def get(self):
        return 'Please use: /api1 /api2 /api3 to generate logs and /logs to get 10 last lines.'


class API1(Resource):
    def get(self):
        codes = ['200', '300', '400', '500']
        urls = ['/url1/', '/url2/', '/url3/']
        FORMAT = '%(asctime)-15s|%(levelname)s|%(ipsrc)s|%(ipdst)s|%(url)s|%(code)s'
        logging.basicConfig(
            format=FORMAT,
            filename='data.log',
            level=logging.DEBUG)

        logger = logging.getLogger('tcpserver')

        d = {'ipsrc': '192.168.0.'+str(random.randrange(1,255)), 'ipdst': '192.168.0.'+str(random.randrange(1,255)), 'url': random.choice(urls), 'code': random.choice(codes)}
        logger.warning('Random payload: %s', ''.join(random.choice(string.ascii_lowercase) for i in range(10)), extra=d)
        return 'Random log generated.'


class API2(Resource):
    def get(self):
        codes = ['200', '300', '400', '500']
        urls = ['/url1/', '/url2/', '/url3/']
        FORMAT = '%(asctime)-15s|%(levelname)s|%(ipsrc)s|%(ipdst)s|%(url)s|%(code)s'
        logging.basicConfig(
            format=FORMAT,
            filename='data.log',
            level=logging.DEBUG)

        logger = logging.getLogger('tcpserver')

        d = {'ipsrc': '192.168.0.'+str(random.randrange(1,255)), 'ipdst': '192.168.0.'+str(random.randrange(1,255)), 'url': random.choice(urls), 'code': random.choice(codes)}
        logger.warning('Random payload: %s', ''.join(random.choice(string.ascii_lowercase) for i in range(10)), extra=d)
        return 'Random log generated.'


class API3(Resource):
    def get(self):
        codes = ['200', '300', '400', '500']
        urls = ['/url1/', '/url2/', '/url3/']
        FORMAT = '%(asctime)-15s|%(levelname)s|%(ipsrc)s|%(ipdst)s|%(url)s|%(code)s'
        logging.basicConfig(
            format=FORMAT,
            filename='data.log',
            level=logging.DEBUG)

        logger = logging.getLogger('tcpserver')

        d = {'ipsrc': '192.168.0.'+str(random.randrange(1,255)), 'ipdst': '192.168.0.'+str(random.randrange(1,255)), 'url': random.choice(urls), 'code': random.choice(codes)}
        logger.warning('Random payload: %s', ''.join(random.choice(string.ascii_lowercase) for i in range(10)), extra=d)
        return 'Random log generated.'


class LOGS(Resource):
    def get(self):
        return open('data.log').readlines()[-11:]


api.add_resource(ROOT, '/')
api.add_resource(API1, '/api1')
api.add_resource(API2, '/api2')
api.add_resource(API3, '/api3')
api.add_resource(LOGS, '/logs')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8002)
