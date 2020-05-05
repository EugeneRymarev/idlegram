import getopt
import sys

from telethon import TelegramClient

import proxy
import secret

default_proxy = None
try:
    opts, args = getopt.getopt(sys.argv[1:], 'p', ['proxy'])
    for opt, arg in opts:
        if opt in ('-p', '--proxy'):
            default_proxy = proxy.proxy
except getopt.GetoptError:
    sys.exit(2)

client = TelegramClient(
    'idlegram_session',
    secret.api_id,
    secret.api_hash,
    proxy=default_proxy
).start()


def main():
    final_credits = 'Idle Telegram Daemon is running'
    print(final_credits)
    client.run_until_disconnected()


if __name__ == '__main__':
    main()
