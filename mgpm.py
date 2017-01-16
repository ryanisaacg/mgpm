#!python
import json
import os
from shutil import copy
import sys

try:
    with open('~/.mgpmrc', 'r') as f:
        config = json.loads(f.read())
except FileNotFoundError:
    config = json.loads("{}")
    config['__INSTALL_PATH'] = input('Path to MinGW root: ')

install = config['__INSTALL_PATH']

#Install/remove/update return True if they have affected the installation

def install(name, path):
    if name in config:
        return False
    else:
        includes = os.listdir(path + '/include')
        libs = os.listdir(path +  '/lib')
        bins = os.listdir(path + '/bin')
        config['name'] = { 'include' : includes, 'lib' : libs, 'bin' : bins }
        map(lambda x: copy(path + '/include/' + x, install + '/include'), includes)
        map(lambda x: copy(path + '/lib/' + x, install + '/lib'), libs)
        map(lambda x: copy(path + '/bin/' + x, install + '/lib'), bins)
        with open('~/.mgpmrc', 'w') as f:
            f.write(json.dumps(config))
        return True
def remove(name):
    if not name in config:
        return False
    else:
        map(lambda x: os.remove(install + '/include/' + x), config[name]['include'])
        map(lambda x: os.remove(install + '/lib/' + x), config[name]['lib'])
        map(lambda x: os.remove(install + '/lib/' + x), config[name]['bin'])
        with open('~/.mgpmrc', 'w') as f:
            f.write(json.dumps(config))
        return True
def update(name, path):
    if remove(name):
        return install(name, path)
    return False
def has(name):
    return name in config

if len(sys.argv) < 2:
    command = "null"
else:
    command = sys.argv[1]
if len(sys.argv) < 3:
    package = "null"
else:
    package = sys.argv[2]

if command == "install":
    modified = install(package, '.')
    if not modified:
        print("Package " + package + " is already installed.")
    else:
        print(package + " installed successfully.")
elif command == "remove":
    modified = install(package)
    if not modified:
        print("Package " + package + " is not installed.")
    else:
        print(package + " has been removed succesfully.")
elif command == "update":
    modified = update(package, '.')
    if not modified:
        print("Package " + package + " has not been updated. Is it installed?")
    else:
        print(package + " has been updated succesfully.")
elif command == "has":
    if has(package):
        print(package + " is installed.")
    else:
        print(package + " is not installed.")
elif command == 'list':
    for pack in config.keys():
        if pack != "__INSTALL_PATH":
            print(pack)
else:
    print('Please enter a command. Command syntax is mgpm [install/remove/has/list/update] [package name]')
