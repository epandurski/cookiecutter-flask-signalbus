#!/usr/bin/env python

import sys
import logging
import argparse
from contextlib import suppress

parser = argparse.ArgumentParser(description='Send pending signals over the message bus.')
parser.add_argument('wait', nargs='?', metavar='WAIT_SECONDS', type=float,
                    help='the number of seconds to wait')


def flush_signalbus(**kwargs):
    from wsgi import app

    if 'signalbus' in app.extensions:
        logger = logging.getLogger(__name__)
        with app.app_context():
            try:
                signal_count = app.extensions['signalbus'].flush(**kwargs)
            except Exception:
                logger.exception('Caught error while sending pending signals.')
                sys.exit(1)
            if signal_count > 0:
                logger.warning('%i pending signals have been sent.', signal_count)


if __name__ == '__main__':
    args = parser.parse_args()

    # Set system environment variables if an ".env" file is present.
    with suppress(ImportError):
        from dotenv import load_dotenv
        load_dotenv()

    kw = {} if args.wait is None else {'wait': args.wait}
    flush_signalbus(**kw)
