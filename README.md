# Collab Play

This project is implemented with pygame and bootstrapped and packaged with briefcase

### Running on development mode
Run 'briefcase dev' in the location of the project folder

### Generating a package
on macOS, inside the project folder, run:
- briefcase build
- briefcase package --no-sign

this generates a package with no signature. It might raise a security issue on some versions of macOS
To generate packages for Windows, Linux, iOS or Android, see the documentation for briefcase

### Testing on 1 device
To create the host and multiple clients from the same machine, you can convert 'MULTIPLE_CLIENTS_ON_SAME_MACHINE' to True on network.py to specify the port you connect with and using different ports on different processes.