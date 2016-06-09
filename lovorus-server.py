#!/bin/env python3
# The MIT License (MIT)
#
# Copyright (c) 2016 La Ode Muh. Fadlun Akbar
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from xmlrpc.server import SimpleXMLRPCServer
from shutil import disk_usage
from json import dumps

kilo_bytes = 1024
mega_bytes = 1024 * 1024
giga_bytes = 1024 * 1024 * 1024

def send_to_client():
    (total, used, free) = disk_usage ("/")
    server_disk_usage = {
        "Total" : {
            "kB" : float(total)/kilo_bytes,
            "MB" : float(total)/mega_bytes,
            "GB" : float(total)/giga_bytes
        },
        "Used" : {
            "kB" : float(used)/kilo_bytes,
            "MB" : float(used)/mega_bytes,
            "GB" : float(used)/giga_bytes
        },
        "Free" : {
            "kB" : float(free)/kilo_bytes,
            "MB" : float(free)/mega_bytes,
            "GB" : float(free)/giga_bytes
        }
    }

    return dumps(server_disk_usage)

def main():
    server = SimpleXMLRPCServer(("", 13000))
    server.register_function(send_to_client,"server_disk_usage")
    server.serve_forever()

if __name__ == '__main__':
    main()
