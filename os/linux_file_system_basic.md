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

## Type of file: link
Link is like a shortcut. There are two kinds of links:
- Hard link
- Soft link/symbolic link

With hard link, we can:
- link to files, but not directories
- cannot link to a file on different disk or volume
- when the original file is removed, the link will still be ok and usable.
How to create a hard link:
```bash
ln /path/to/source path/to/dest
```

With soft/symlink, we can:
- link to files and directories
- when the original file is removed, the link **will be broken** and not usable.
How to create a symlink:
```bash
ln -s /path/to/src /path/to/dst
```

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
2. Create file (like `touch`): `creat(path, mode)`
3. Read: `ssize_t read(fd, buf, noct)`
4. etc