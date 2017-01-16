#MinGW Package Manager

**Note: Not affiliated with the official MinGW project**

Installing third-party libraries with MinGW is painful, but it doesn't have to be. MGPM is a lightweight utility that allows you to easily install or remove packages globally, removing the need for include directory or link directory flags for your projects. MGPM also doesn't require a package manifest file; headers should be top-level in `your-package/include` and linker input should be in `your-package/lib` and `your-package/bin` as appropriate.

##Installation

### MGPM command
It is recommended you copy the `mgpm.py` file, rename it to `mgpm`, and place it in your system path. Python 3 must be your python interpreter, and must be available with the `python` command.

This is not required to use MGPM; it is a single-file Python 3 script, so it can be placed and run any way you wish.

The first time you run MGPM on a system, it will prompt you for the path to your MinGW installation. It will probably be `C:\MinGW` or `C:\TDM-GCC` or a similar name. 

##Usage

To install a package, navigate to its directory and run the command `mgpm install <your-name-here>`, substituting in the package name.

To update a package to a newer version, navigate to the new version's directory and run the command `mgpm update <name>`

To remove a package, run the command `mgpm remove <name>`

To see if a package is installed, run the command `mgpm has <name>`

To see all installed packages, run the command `mpgm list`
