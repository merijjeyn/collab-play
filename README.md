# Collab Play

This project is implemented with pygame and bootstrapped and packaged with briefcase.

Collab Play provides a simple party game can be run on macOs, windows, ios, and android. In this party game everyone can join and control a single player collaboratively. As you know, the pong game has two sides so it is a two player game. But we believe more people bring more fun. So, instead of 2 players Collab Play allows as many people to connect as your network and server supports( more than 100 players in if a standart computer is host)

### Running on development mode
Run 'briefcase dev' in the location of the project folder

### Generating a package
on macOS, inside the project folder, run:
- briefcase build
- briefcase package --no-sign

this generates a package with no signature. It might raise a security issue on some versions of macOS
To generate packages for Windows, Linux, iOS or Android, see the documentation for briefcase

### Objectives and Challenges Faced Along the Way
The initial idea for this project was to generate a working application for most platforms including macOS, iOS, Windows and Linux. So that it would be really easy for everyone to create and join a game no matter what their environment is. With that in mind, we decided to use Unreal Engine to build our game. Also we would have gained some experience with that tool as well. The first challenge we faced was setting up and getting started with Unreal Engine. Our computers could not really handle the load so we decided to simply use a python library to bootstrap and package our code for different platforms called briefcase together with pygame. Then we faced some trouble adapting pygame to iOS and Android devices but decided to pursue that functionality later if we come back to this project.

Another objective we had in mind was to somehow establish peer to peer connections between the players so that the latency inside the game would be minimized. We researched some approaches for this and came across a method called NAT punchthrough. Essentially, a machine connects to a server and that server tries to somehow guess the port that machine used to connect to its modem, since the ip address of many devices are hidden by their modem. This seemed like a great challenge but we decided not to pursue it because of deadline limitations. So we just went with setting up a relay server where the connections can flow through which worked like a charm.

We used a mechanism which is similiar to a relay server. The main challange was maintaining low latency. To deal with latency we did not use any framework. The server works with python sockets like we used in the previous assignments. 

### Work done by Meric Ungor

I worked on setting up the project, the mechanics of the game itself, and the networking capabilities of the client. so basically, I worked mostly on the client part.

### Work done by Kayacan Vesek

I worked creating the server side, and deploying to the azure ubuntu instance.
