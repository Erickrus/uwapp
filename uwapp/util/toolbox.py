# -*- coding: utf-8 -*-
import os
import errno
import shutil

from datetime import datetime



def get_library_path():
    path = __file__
    return path[:path.find("uwapp")-1]


def mkdir(dirname):
    try:
        os.mkdir(dirname)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass

def copy(from_path, to_path):
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)

def get_timestamp(fmt='%Y-%m-%d %H:%M:%S'):
    return datetime.now().strftime(fmt)

def read_file(filename):
    f = open(filename, "r", encoding="utf-8")
    lines = "\n".join(f.readlines())
    f.close()
    return lines

def write_file(filename, content):
    f = open(filename, "w", encoding="utf-8")
    f.write(content)
    f.close()
