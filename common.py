host = '0.tcp.ngrok.io'
pub_port = 2222   # the subscriber port may not necessarily be the same as the publisher port
sub_port = 16946  # because of the way that ngrok forwards ports


class Topics:  # ALL TOPICS MUST BE BYTES
    KBD_EVENT = bytes(0)
