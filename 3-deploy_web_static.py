#!/usr/bin/python3
# a fabfile that creates and distributes an archive to your web
# servers, using the function deploy:
import os.path
from datetime import datetime
from fabric.api import env
from fabric.api import local
from fabric.api import put
from fabric.api import run

env.hosts = ['100.25.41.245', '54.172.27.227']


def do_pack():
    """
    generates a .tgz archive from the contents of the web_static folder
    """
    tarfile_name = "web_static_" + str(datetime.datetime.now().year) + str(datetime.datetime.now().month) + str(
        datetime.datetime.now().day) + str(datetime.datetime.now().minute) + str(
        datetime.datetime.now().second) + ".tgz"
    if os.path.isdir("versions") is False:
        dir_creation = local("mkdir -p versions")
        if dir_creation.failed is True:
            return None
    command = "tar -czvf versions/{} web_static".format(tarfile_name)

    # create the tar file
    local_command = local(command)
    if local_command.failed is True:
        return None
    else:
        return "versions/{}".format(tarfile_name)


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
    if run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(basename,
                                                                                               basename)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".format(basename)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(basename)).failed is True:
        return False
    return True


def deploy():
    """creates and distributes an archive to a web server."""
    filepath = do_pack()  # stores the filepath returned by do_pack
    if filepath is None:
        return False
    return do_deploy(filepath)
