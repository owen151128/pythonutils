# -*- coding: utf-8 -*-

import subprocess


def execute(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, cwd=workDir)
    # p.wait()

    i = p.stdout.readline()

    while i != b'':
        print(i.decode('utf8').rstrip('\n'))
        i = p.stdout.readline()
