from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)

def new_app():
    rutas = [('/', ListHandler)]
    return Application(rutas, debug = False)

def main():
    try:
        rutas = [('/', ListHandler),('/onoff',OnOff)]
        app = Application(rutas, debug=False)
        app.listen(80)
        IOLoop.instance().start()

    except KeyboardInterrupt:
        exit()

class ListHandler(RequestHandler):
    def get(self):
        self.render('luz.html')

    def post(self):
        GPIO.output(3,not GPIO.input(3))
        self.get()

class OnOff(RequestHandler):
    def get(self):
        GPIO.output(3,not GPIO.input(3))
        self.write('')

if __name__ == "__main__":
    main()
