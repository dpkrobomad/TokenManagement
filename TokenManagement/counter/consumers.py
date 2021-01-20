from channels import Group


def ws_connect(message):
    Group('data').add(message.reply_channel)


def ws_disconnect(message):
    Group('data').discard(message.reply_channel)   