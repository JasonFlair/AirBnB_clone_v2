#!/usr/bin/python3
"""
a fabfile that generates a .tgz archive from the contents of the web_static folder
of your AirBnB Clone repo, using the function do_pack
"""
from fabric.api import *
import datetime


def do_pack():
    """
    generates a .tgz archive from the contents of the web_static folder
    """
    tarfile_name = "web_static_" + str(datetime.datetime.now().year) + str(datetime.datetime.now().month) + str(
        datetime.datetime.now().day) + str(datetime.datetime.now().minute) + str(
        datetime.datetime.now().second) + ".tgz"
    local("mkdir -p versions")
    command = "tar -czvf versions/{} web_static".format(tarfile_name)

    # create the tar file
    local(command)
