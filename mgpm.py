#!python
import json
import os
import shutil
import sys

config_path = os.path.expanduser('~') + '/.mgpmrc'

try:
    with open(config_path, 'r') as f:
        config = json.loads(f.read())
except FileNotFoundError:
    config = json.loads("{}")
    config['__INSTALL_PATH'] = input('Path to MinGW root: ')
    with open(config_path, 'w+') as f:
        f.write(json.dumps(config))

install_dir = config['__INSTALL_PATH']

#Install/remove/update return True if they have affected the installation
def install(name, path):
    if name in config:
        return False
    else:
        includes = os.listdir(path + '/include') if os.path.exists(path + '/include') else []
        libs = os.listdir(path +  '/lib') if os.path.exists(path + '/lib') else []
        bins = os.listdir(path + '/bin') if os.path.exists(path + '/bin') else []
        config[name] = { 'include' : includes, 'lib' : libs, 'bin' : bins }
        def cpy(fname, src, dest):
            src = path + '/' + src + '/' + fname
            dest = install_dir + '/' + dest
            if os.path.isfile(src):
                shutil.copy(src, dest)
        for x in includes:
            cpy(x, 'include', 'include')
        for x in libs:
            cpy(x, 'lib', 'lib')
        for x in bins:
            cpy(x, 'bin', 'lib')
        with open(config_path, 'w') as f:
            f.write(json.dumps(config))
        return True
def remove(name):
    if not name in config:
        return False
    else:
        def rem(fname, dst):
            dst = install_dir + '/' + dst + '/' + fname
            if os.path.isfile(dst):
                os.remove(dst)
        for x in config[name]['include']:
            rem(x, 'include')
        for x in config[name]['lib']:
            rem(x, 'lib')
        for x in config[name]['bin']:
            rem(x, 'lib')
        del config[name]
        with open(config_path, 'w') as f:
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
    modified = remove(package)
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
