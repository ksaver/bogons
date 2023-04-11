# bogons
Script to check if IP addresses are local (bogons) or public.

## Examples of use

- With no arguments:

![image](https://user-images.githubusercontent.com/163230/231056559-e725c7fc-736a-4c5b-a872-1bebe8800d38.png)


- With a sinlge IP address:

```shell
> ./bogons.py -a 10.0.0.1
Bogon: 10.0.0.1
>
> ./bogons.py -a 127.0.0.1
Bogon: 127.0.0.1
>
> ./bogons.py -a 8.8.8.8
Public: 8.8.8.8
>
> ./bogons.py -a 208.80.153.224
Public: 208.80.153.224
>
```

- With a file containing a list of IP addresses:

```shell
> ./bogons.py -f ips.txt
Public: 199.187.193.xxx
Bogon: 10.252.11.xxx
Public: 201.149.59.xxx
Bogon: 10.252.21.xx
Public: 52.115.223.xxx
Bogon: 172.20.22.xx
Public: 94.130.13.x
Public: 52.46.154.xx
Public: 108.138.167.xx
Public: 18.160.156.xxx
```

- Showing only local IP addresses from a file:

```shell
> ././bogons.py -f ips.txt --only-local
10.252.11.xxx
10.252.21.xx
172.20.22.xx
```

- Showing only public IP addresses from a file:

```shell
./bogons.py -f ips.txt --only-public
199.187.193.xxx
201.149.59.x
52.115.223.xxx
94.130.13.x
52.46.154.xx
108.138.167.xx
18.160.156.xx
```
