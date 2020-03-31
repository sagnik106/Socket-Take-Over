# Socket-Take-Over
A project on sockets to take over the computer of the another person on the same network. It basically gives you access to the target's terminal whether a UNIX system or a DOS system with some special commands

## Requirements/Libraries:
* Python 3.6.9
* Socket

## Steps
1. Run the server.py file in the target machine that is connected to the same network as the attacker
1. Take note of the target machine's MAC Address or their curect ip address.
1. If you cannot get a hold of the ip address of the target then feed the MAC address of the target into [networkarp.py](https://github.com/sagnik106/Socket-Take-Over/blob/master/networkarp.py) to get their ip address from the network arp table
1. Feed the ip address either way in the [client.py](https://github.com/sagnik106/Socket-Take-Over/blob/master/client.py) file
1. Run the [client.py](https://github.com/sagnik106/Socket-Take-Over/blob/master/client.py) file on the attacker's machine.

## Special Commands:
* ```filetx <Absolute or relative address of file to transfer>```

## File Configuration
* [client.py](https://github.com/sagnik106/Socket-Take-Over/blob/master/client.py)
* [server.py](https://github.com/sagnik106/Socket-Take-Over/blob/master/server.py)
* [networkarp.py](https://github.com/sagnik106/Socket-Take-Over/blob/master/networkarp.py)
