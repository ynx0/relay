import keyboard as kbd
import zmq
import common
from logzero import logger

TARGET_DELTA = 0.02


def main():
    ctx = zmq.Context()
    sub = ctx.socket(zmq.SUB)

    logger.info("Subscribing to to: %s:%s" % (common.host, common.port))

    sub.connect('tcp://%s:%s' % (common.host, common.port))

    sub.subscribe(topic=common.Topics.KBD_EVENT)

    last_event = kbd.KeyboardEvent(kbd.KEY_UP, 0)

    def should_exec(event: kbd.KeyboardEvent):
        nonlocal last_event  # what the heck python
        delta = event.time - last_event.time
        last_event = event
        print("Delta is" + str(delta))
        return delta > TARGET_DELTA

    while True:

        kbd_event: kbd.KeyboardEvent = sub.recv_pyobj()

        if should_exec(kbd_event):
            key = kbd_event.name
            kbd.send(key, True, False) if kbd_event.event_type == kbd.KEY_DOWN else str('a')  # kbd.release(key)
            logger.info("Pressed key: " + str(kbd_event))
            print("=================")
        else:
            print("Skipping duplicate event")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.debug("Quitting due to Ctrl+C")
