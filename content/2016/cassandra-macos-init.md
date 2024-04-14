---
date: '2016-11-03'
title: How-to initialize Cassandra in macOS?
category: English
tags: CLI, database, macOS, noSQL, Cassandra, Apple, macOS 10.12 Sierra, Homebrew, Java
---

A little note on how I setup and bootstrap a local Cassandra clusters on macOS
machines for development.

Instructions below were tested on macOS Sierra, and aim to spawn a 3-nodes
2.1.x cluster.

Install [`ccm`](https://github.com/pcmanus/ccm) and its dependencies:

```shell-session
$ brew install ant
$ brew cask install java
$ pip install --upgrade ccm
```

Just in case we messed up a previous installation, let's clean things up:

```shell-session
$ ccm switch test21
$ ccm stop test21
$ killall java
$ ccm remove
$ rm -rf "${HOME}/.ccm/test21"
```

Create a new 3-nodes cluster named `test21` with the latest Cassandra release
of the 2.1.x series:

```shell-session
$ ccm create test21 -v 2.1 -n 3
```

Here is an example on how we can alter the common configuration of all nodes of
the cluster. In this case to bump all timeouts ten times:

```shell-session
$ tee -a ~/.ccm/test21/cluster.conf <<-EOF
config_options: {
    read_request_timeout_in_ms: 50000,
    range_request_timeout_in_ms: 100000,
    write_request_timeout_in_ms: 20000,
    request_timeout_in_ms: 100000,
    tombstone_failure_threshold: 10000000}
EOF
$ ccm updateconf
```

Also had to sometimes increase Java's heap size, like to accommodate large data
imports:

```shell-session
$ export CCM_MAX_HEAP_SIZE="12G"
$ export CCM_HEAP_NEWSIZE="2400M"
```

Before starting the server, we need to create missing local network interfaces,
one for each node:

```shell-session
$ sudo ifconfig lo0 alias 127.0.0.1 up
$ sudo ifconfig lo0 alias 127.0.0.2 up
$ sudo ifconfig lo0 alias 127.0.0.3 up
```

We can now start the cluster:

```shell-session
$ ccm start test21
```

To get the state of the cluster:

```shell-session
$ ccm status
Cluster: 'test21'
-----------------
node1: UP
node3: UP
node2: UP
```

Or a much more detailed status:

```shell-session
$ ccm status -v
Cluster: 'test21'
-----------------
node1: UP
       auto_bootstrap=False
       thrift=('127.0.0.1', 9160)
       binary=('127.0.0.1', 9042)
       storage=('127.0.0.1', 7000)
       jmx_port=7100
       remote_debug_port=0
       byteman_port=0
       initial_token=-9223372036854775808
       pid=81379

node3: UP
       auto_bootstrap=False
       thrift=('127.0.0.3', 9160)
       binary=('127.0.0.3', 9042)
       storage=('127.0.0.3', 7000)
       jmx_port=7300
       remote_debug_port=0
       byteman_port=0
       initial_token=3074457345618258602
       pid=81381

node2: UP
       auto_bootstrap=False
       thrift=('127.0.0.2', 9160)
       binary=('127.0.0.2', 9042)
       storage=('127.0.0.2', 7000)
       jmx_port=7200
       remote_debug_port=0
       byteman_port=0
       initial_token=-3074457345618258603
       pid=81380
```

To get the detailed data ownership status, you need to get through a node and
point to an existing column family:

```shell-session
$ ccm node1 status my_column_family

Datacenter: datacenter1
=======================
Status=Up/Down
|/ State=Normal/Leaving/Joining/Moving
--  Address    Load     Tokens  Owns (effective)  Host ID                               Rack
UN  127.0.0.1  6.08 GB  1       100.0%            25e0440b-3ac9-490e-b0b0-260e96395f15  rack1
UN  127.0.0.2  6.22 GB  1       100.0%            848edc79-db1c-49bf-bdd8-3768b588460f  rack1
UN  127.0.0.3  6.14 GB  1       100.0%            75acd6c7-61c5-4ae7-9008-63d6426d1468  rack1
```

For debugging, a node's log is available through `ccm`:

```shell-session
$ ccm node1 showlog
```

And you can directly query through that node:

```shell-session
$ TZ=UTC cqlsh --cqlversion=3.2.1 127.0.0.1
Connected to test21 at 127.0.0.1:9042.
[cqlsh 5.0.1 | Cassandra 2.1.12 | CQL spec 3.2.1 | Native protocol v3]
Use HELP for help.
cqlsh> CONSISTENCY QUORUM;
Consistency level set to QUORUM.
cqlsh>
```

Finally, to restore a bunch of table snapshots from your production cluster:

```shell-session
$ TABLES="table1 table2 table3"
$ DUMP_FOLDER="${HOME}/dump/2016-09-12/"
$ for host_folder in $(ls "${DUMP_FOLDER}"); do
>     for table in ${TABLES}; do
>         SSTABLE_FOLDER="${DUMP_FOLDER}/${host_folder}/my_column_family/${table}";
>         echo "Importing: ${SSTABLE_FOLDER} ...";
>         ccm bulkload "${SSTABLE_FOLDER}";
>     done
> done
```

Forcing a repair on each table after a massive import can't be bad:

```shell-session
$ for table in ${TABLES}; do
>     ccm node1 nodetool repair my_column_family ${table};
> done
```
