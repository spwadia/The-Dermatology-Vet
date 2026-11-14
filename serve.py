#!/usr/bin/env python3
"""Tiny static server for local preview:  python3 serve.py [port]"""
import os
import sys
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 4173

handler = partial(SimpleHTTPRequestHandler, directory=ROOT)
httpd = ThreadingHTTPServer(("127.0.0.1", PORT), handler)
print("Serving %s on http://127.0.0.1:%d" % (ROOT, PORT), flush=True)
httpd.serve_forever()
