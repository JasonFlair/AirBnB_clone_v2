#!/usr/bin/python3
"""
a fabfile that distributes an archive to your web
servers, using the function do_deploy:
"""
from fabric.api import *
import tarfile
import os.path

env.hosts = ['100.25.41.245', '54.172.27.227']


def do_deploy(archive_path):
    """
     a Fabric script (based on the file 1-pack_web_static.py) that distributes an archive to your web servers,
     using the function do_deploy:
     Args: archive_path the path to the archive file
     Returns: True if verything works, no errors
    """
    filename, file_extension = os.path.splitext(archive_path)
    basename = os.path.basename(filename)
    tarfile_name = basename + ".tgz"

    if os.path.isfile(archive_path) is False:
        return False

    print("Uploading the project archive")
    if put(archive_path, "/tmp/{}".format(tarfile_name)).failed is True:
        return False
    run("mkdir -p /data/web_static/releases/{}".format(basename))
    if run("tar -xzvf /tmp/{} -C /data/web_static/releases/{}".format(
            tarfile_name, basename)).failed is True:
        return False
    run("rm /tmp/{}".format(tarfile_name))
    if run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(basename, basename)).failed is True:
        return False
    if run("rm /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{} /data/web_static/current").failed is True:
        return False
    return True
