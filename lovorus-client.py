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

from json import loads
from xmlrpc.client import ServerProxy
from os import system
from sys import argv

def ping_server(server_addr):
    print("Checking the server status...")
    status = system("ping -c 1 -w 5 " + server_addr + " > /dev/null 2>&1")
    if status == 0:
        return ("Up", server_addr)
    else:
        return ("Down", server_addr)

def print_info_disk(info, data_disk):
    print("Total\t\t\t: %.2f kB\t\t%.2f MB\t%.2f GB" \
          % (data_disk[info]['kB'], data_disk[info]['MB'], data_disk[info]['GB']))

def main(server_addr):
    server = ServerProxy("http://" + server_addr + ":13000/", allow_none=True)
    (status_server, addr) = ping_server(server_addr)
    print("%s status\t: %s" % (addr, status_server))
    if status_server == "Up":
        try:
            data_disk = loads(server.server_disk_usage())
            print_info_disk("Total", data_disk)
            print_info_disk("Used", data_disk)
            print_info_disk("Free", data_disk)
        except ConnectionRefusedError:
            print("But, lovorus-server.py is not running on the server")

if __name__ == '__main__':
    if len(argv) == 2:
        main(argv[1])
    else:
        print("Parameter kurang")
