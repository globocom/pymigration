# -*- coding: utf-8 -*-
import os

abs_path = os.path.abspath('')

folder = "%s/pymigrations" % abs_path

def current_version():
    path = "%s/current_version.txt" % folder
    with open(path, "r+") as f:
        content = f.read()
    return content

def set_current_version(version):
    path = "%s/current_version.txt" % folder
    with open(path, "w") as f:
        content = f.write(version)
    return content