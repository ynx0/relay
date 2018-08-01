import keyboard as kbd
import zmq
from logzero import logger
import common


def main():
    ctx = zmq.Context()
    # noinspection PyUnresolvedReferences
    pub = ctx.socket(zmq.PUB)
    pub.bind('tcp://*:%s' % common.port)
    logger.info('Publishing on port: %s' % common.port)

    def send_data(event: kbd.KeyboardEvent):
        logger.info("Publishing key event: " + event.name + ' ' + event.event_type)
        pub.send_pyobj(event)

    kbd.hook(send_data)

    while True:
        pass


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.debug("Exitting due to Ctrl+C")
