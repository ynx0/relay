import keyboard as kbd
import zmq
from logzero import logger
import common

# TODO
# add add an unstick hotkey that automatically
# releases all (the hotkeys type) keys
# and also add a pause hotkey for
# the host so that the host can stop and start broadcast
# also make a module that exposes a class
# that can connect to any ip

# also, make the connect ping the host first to see if it is reachable,
# or at least try to do something that will make sure that you are getting bytes in,
# rather than blocking on .*_recv()

# also, add better quitting of the sub program
# because it requires an object to be recieved before it listens for Ctrl+C
# because it needs to go through one cycle of the look before it checks for
# the 'alt+bkspc' keybind, and thus doesn't exit the loop until an object is recieved

# also


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
