# Basics of Linux File Systems
Reading materials:
- https://www.tldp.org/LDP/intro-linux/html/sect_03_01.html
- https://www.linux.com/learn/intro-to-linux/2017/6/understanding-linux-links

## Type of files

How to know type of files:
```
$ ls -l
# example output
-rw-rw-r--. 1 bintang bintang 0 Mar  2 22:32 a
drwxrwxr-x. 2 bintang bintang 4096 Mar  2 22:32 folder
```
The first character in `-rw-rw-r--.`, for example, is the type of the file.

Types of files:

- `-`: regular file
- Directories (d)
- Links (l)
- Socket (s)
- Special files (c): such as device in `/dev`
- Named pipes (p): act more or less like sockets, but without socket semantics
- block device (b)

## inode

inode is a number (or id) containing information about the actual data of a file such as owner and group owner of the file, file type, last modified, time of creation, filesize, number of links to this file, and address defining the actual location of the file. *It does not contain file name*.

How to know inode of a file:
```bash
$ ls -i file
or
$ stat file
```

To see use of inodes in partition:

```bash
df -i
```

## Links

Sources:

- https://stackoverflow.com/a/29786294/10522825
- https://unix.stackexchange.com/a/147515
- https://unix.stackexchange.com/a/50188

There are 2 types: hard link and soft link (symbolic link).

How to create:

- hard link: `ln file_ori_name hard_link_name`
- soft link: `ln -s file_ori_name hard_link_name`

Let's say we have a file.txt. In the inode, there is a *reference counter* which counts how many link references it has.

```bash
> ls -li file.txt
960528 -rw-rw-r--. 1 bintang bintang 8 Jun 28 18:49 file.txt
  ^                ^
inode            reference counter
```

Then we create a hard link.

```bash
> ln file.txt hard
> ls -l
960528 -rw-rw-r--. 2 bintang bintang     8 Jun 28 18:49 hard
960528 -rw-rw-r--. 2 bintang bintang     8 Jun 28 18:49 file.txt
  ^                ^
same inode        reference counter
```

Then we create a soft link

```bash
> ln -s file.txt soft
> ls -l
960528 -rw-rw-r--. 2 bintang bintang     8 Jun 28 18:49 hard
960528 -rw-rw-r--. 2 bintang bintang     8 Jun 28 18:49 file.txt
919502 lrwxrwxrwx. 1 bintang bintang     8 Jun 28 18:58 soft -> file.txt
  ^                ^
different inode   reference counter
```

The diagram looks like this:

![link](https://i.stack.imgur.com/ka2ab.jpg)

Source: https://stackoverflow.com/a/29786294/10522825

When the file is removed, the `hard` still has its value. The `soft` is broken. This is because the soft link points to the file. So when the file is deleted, the link is broken. Hard link has the same inode as the original file. When you do update to the original file, the hard link will also be updated. The bits of the file will be removed from the disk when the reference counter in the inode is 0. So if we delete the original file, it just decrements the reference counter in the struct inode. As long as the reference counter is > 0, the file still exists on the disk. That's why the bits of file still exists on disk.

Refer to the [troubleshooting guide](troubleshooting_guide.md) for troubleshooting disk full because of inodes.

# Other notes

## /proc

Reading material: https://www.linux.com/news/discover-possibilities-proc-directory 

`/proc` directory holds all the details about the Linux system such as processes and configuration parameters.

Inside this proc, there are:
- `/proc/PID`: this holds information of that PID. For example, `/proc/PID/cmdline` stores the command used to invoke this process PID, etc.
- `/proc/cpuinfo`
- `/proc/meminfo`
- etc.

## System calls when working with data

Reading material: http://profile.iiita.ac.in/bibhas.ghoshal/lab_files/System%20calls%20for%20files%20and%20directories%20in%20Linux.html

They are in C. For convenience, only the first system call I write with full name and arguments. Refer to the above link to get more details.
1. Open or create file: `open(const char *path, int flags, ...)`
2. Create file (like `touch`): `create(path, mode)`
3. Read: `ssize_t read(fd, buf, noct)`
4. etc