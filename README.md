# bogons.py

Script to check if IP addresses are public (global) or local (bogons).

## Get the script

```shell
$ git clone https://www.github.com/ksaver/bogons
$ cd bogons
$ chmod +x bogons.py
```

## Examples of use

### No arguments:

```shell
$ ./bogons.py
usage: bogons.py [-h] (-a ADDRESS | -f FILE) [--only-local | --only-public]
bogons.py: error: one of the arguments -a/--address -f/--file is required
```

### Getting help

```shell
$ ./bogons.py --help
usage: bogons.py [-h] (-a ADDRESS | -f FILE) [--only-local | --only-public]

Check if IP addresses are public or bogons.

options:
  -h, --help            show this help message and exit
  -a ADDRESS, --address ADDRESS
                        Single IP address to check.
  -f FILE, --file FILE  File containing a list of IP addresses to check.
  --only-local          Show only local IP addresses.
  --only-public         Show only public IP addresses. 
```

### Query a sinlge IP address:

```shell
$ ./bogons.py -a 10.0.0.1
Bogon: 10.0.0.1
$
$ ./bogons.py -a 127.0.0.1
Bogon: 127.0.0.1
$
$ ./bogons.py -a 8.8.8.8
Public: 8.8.8.8
$
$ ./bogons.py -a 208.80.153.224
Public: 208.80.153.224
$
```

### Query multiple files from a file:

```shell
$ ./bogons.py -f ips.txt
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

### Showing only local IP addresses from a file

```shell
> ./bogons.py -f ips.txt --only-local
10.252.11.xxx
10.252.21.xx
172.20.22.xx
```

### Showing only local IP addresses from a file

```shell
> ./bogons.py -f ips.txt --only-public
199.187.193.xxx
201.149.59.x
52.115.223.xxx
94.130.13.x
52.46.154.xx
108.138.167.xx
18.160.156.xx
```

### Getting input from other commands

The `--file` can be used as well with the standard output from other commands:

- A single IP

```shell
$ echo '10.0.0.1' | ./bogons.py -f -
Bogon: 10.0.0.1
$
$ echo '208.80.153.224' | bogons.py -f -
Public: 208.80.153.224
```

- Multiple IPs, from standard input

```shell
$ cat ips.txt | ./bogons.py -f -
Bogon: 10.0.0.1
Bogon: 10.0.0.2
Bogon: 10.0.0.10
Bogon: 10.0.0.11
Bogon: 10.0.1.1
Bogon: 10.0.1.11
Public: 8.8.8.8
Public: 1.1.1.1
Public: 9.9.9.9
[...]
```

- Showing only bogons or public, from standard input

```shell
$ cat ips.txt | ./bogons.py -f - --only-local
10.0.0.1
10.0.0.2
10.0.0.3
[...]
$
$ cat ips.txt | ./bogons.py -f - --only-public
8.8.8.8
1.1.1.1
[...]
```

I hope you find it useful.
