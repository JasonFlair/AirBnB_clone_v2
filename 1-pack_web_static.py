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
    command = "tar -C versions -czvf {} web_static/".format(tarfile_name)

    # create the tar file
    with settings(warn_only=True):
        """
        warn_only setting is set to True, so the local() function will not raise an exception 
        if the command returns a non-zero exit code."""
        local_command = local(command)
        if local_command.failed:
            local("mkdir versions")
            local(command)
