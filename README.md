# Cross-platform C Library Manager

Installing third-party libraries (those your distro doesn't provide, or any library on Windows) 
for C and C++ is painful, but it doesn't have to be. 
XCLM is a lightweight utility that allows you to easily install or remove packages globally, removing the need for include directory or link directory flags for your projects. XCLM also doesn't require a package manifest file; headers should be top-level in `your-package/include` and linker input should be in `your-package/lib` and `your-package/bin` as appropriate. These files will be played in your `$root/include`, `$root/lib` and `$root/lib` folders respectively. On a Unix-derived system, `$root` is likely to be the system root (`/`), on a Windows system it will be the path to your MinGW installation.

## Installation

### XCLM command
It is recommended you copy the `xclm.py` file, rename it to `xclm`, and place it in your system path.

This is not required to use XCLM; it is a single-file Python 3 script, so it can be placed and run any way you wish.

If XCLM cannot locate its configuration file, it will prompt for a path to your compiler root. See above for platform-specific advice on locating your compiler root.

## Usage

To install a local package, navigate to its directory and run the command `xclm install <your-name-here>`, substituting in the package name.

To update a local package to a newer version, navigate to the new version's directory and run the command `xclm update <name>`

To remove a package, run the command `xclm remove <name>`

To see if a package is installed, run the command `xclm has <name>`

To see all installed packages, run the command `mpgm list`
