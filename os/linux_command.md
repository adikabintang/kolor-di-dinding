# Contents
- [file](#file)
- [find](#find)
- [locate](#locate)
- [grep](#grep)
- [du](#du)
- [df](#df)
- [sort](#sort)
- [wc](#wc)
- [uptime](#uptime)
- [whatis](#whatis)
- [tee](#tee)
- [sed](#sed)
- [awk](#awk)
- [read](#read)
- [cut](#cut)
- [tr](#tr)
- [uniq](#uniq)
- [xargs](#xargs)
- [traceroute](#traceroute)
- [dig](#dig)
- [telnet](#telnet)
- [netstat](#netstat)
- [nmap](#nmap)
- [Loops](#Loops)
- [Conditional](#Conditional)
- [Arithmethic](#Arithmethic)
- [Array](#Array)
- [Get](#Get)
- [to](#to)

# Really Basics
## file
`file` find out type of files.
example
```bash
$ file test.xt
> test.txt: ASCII text
```

## find
find files. Example:
```
find -type f -name main.c      ( f for files, d for dir )
```

## locate
like files, but not search in the filesystem. it looks to updatedb. pros: faster than `find`. cons: not as consistent as `find`, especially when there is a change in the filesystem.
example:
```
locate main.c (will look every file containing main.c, like `grep main.c`)
```

## grep
https://www.thegeekstuff.com/2009/03/15-practical-unix-grep-command-examples/ 

Examples:
```bash
$ cat demo_file
THIS LINE IS THE 1ST UPPER CASE LINE IN THIS FILE.
this line is the 1st lower case line in this file.
This Line Has All Its First Character Of The Word With Upper Case.

Two lines above this line is empty.
And this is the last line.
```

```bash
$ grep "this" demo_file
this line is the 1st lower case line in this file.
Two lines above this line is empty.
And this is the last line.
```

```bash
# we make two files first
$ cp demo_file demo_file1
$ grep "this" demo_*
demo_file:this line is the 1st lower case line in this file.
demo_file:Two lines above this line is empty.
demo_file:And this is the last line.
demo_file1:this line is the 1st lower case line in this file.
demo_file1:Two lines above this line is empty.
demo_file1:And this is the last line.
```

```bash
# case insensitive search, using -i
$ grep -i "the" defmo_file
```

```bash
# match regex
$ grep "lines.*empty" demo_file
Two lines above this line is empty.
```

```bash
# match exact string, not substring using -w (like ^word$)
$ grep -w "word" file
```

## id
Checks users and group. Example:
```bash
$ id
uid=1000(bintang) gid=1000(bintang) groups=1000(bintang),10(wheel),971(docker),974(wireshark) context=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023
```

## chmod
Usual mode, refer here: http://permissions-calculator.org/info/ 

Special mode:
**setuid**: executable file with the setuid bit can be executed with the privileges of the file's owner. `chmod 4xxx file` or `chmod u+s`.

**setgid**: executable file with the setgid can be executed with the privileges of the file's group. `chmod 2xxx file` or `chmod g+s file`.

**sticky bit**: when a directory's sticky bit is set, the filesystem treats the files in such directories in a special way so that *only the file owner's, dir owner's, or root can rename/delet the file*. Example: `/tmp` folder. `chmod 1xxx file`.

## du
check file/dir size.
example:
```
$ du -h file.txt (-h to make it readable like 4.0K, 46M, etc)
$ du -h foldername (will print the size recursively)
$ du -h foldername -d 0 (-d for depth, 0 will print the size of foldername only)
$ du -h foldername -d 1 (will print -d 0 and the recursive of depth 1)
```
## df
- show disk usage
- find out which partition a directory is on. Command: `df -h /path/to/dir`
## sort
example
```bash
$ cat file.txt
b
c
a

$ sort file.txt
a
b
c

$ sort -r file.txt
c
b
a
```

For sorting numbers:
```bash
$ sort -n file.txt
1
1.5
2
5
```

## wc
word count
line counting
byte counting

## uptime
tells how long the system has been running.

## whatis
display one-line manual page description of a command. example
```
$ whatis whatis
whatis (1)           - display one-line manual page descriptions

$ whatis tee
tee (1)              - read from standard input and write to standard output and files
tee (1p)             - duplicate standard input
tee (2)              - duplicating pipe content
```

## tee
Read from standard input and write to standard output and files. For example, if we use `ping google.com > file.txt`,  the output will be in file.txt but not in stdout. But with tee, we can get both to stdout and file.txt. Example:
```
$ ping google.com | tee file.txt

or we can even output to multiple files

$ ping google.com | tee file.txt another.txt
```

## sed
sed: stream editor for filtering and transforming text. 

Example 1 replacing string, [link](https://unix.stackexchange.com/questions/159367/using-sed-to-find-and-replace):
```
sed -i -e 's/before/after/g' hello.txt
```

## awk
pattern scanning and processing language. huh?

Example 1, printing column of a text [link](https://www.tutorialspoint.com/awk/awk_basic_examples.htm):
```
$ cat file.txt
1) Amit     Physics   80
2) Rahul    Maths     90

$ awk '{print $1}' file.txt
1)
2)

$ awk '{print $2 " " $4}' file.txt
Amit 80
Rahul 90

# print line which has more than 18 chars
$ awk 'length($0) > 18' file.txt
```

## read
read input.

Example:
```bash
read varname
echo "Hello $varname"
```

## cut
https://www.thegeekstuff.com/2013/06/cut-command-examples/

`cut -c2 test.txt`  print (like `cat`) but only the 2nd character from each line of the test.txt.

`cut -c1-3 test.txt` print character 1 to 3 (like `asu`, 3 character from the first character) from each line of the test.txt.

`cut -c3- test.txt` print from the 3rd character.

`cut -c-8 test.txt` print from the first to the 8th character from each line of the test.txt.

`cut -c2,7 test.txt`  print the 2nd and 7th characters from each line of the test.txt.

`cut -c- test.txt` same as `cat test.txt`.

`cut -d':' -f1 /etc/passwd`   -d is delimiter, -f is the field. in this case, the output would be something like:
```
root
bin
sync
nginx
```

## tr
https://www.geeksforgeeks.org/tr-command-in-unix-linux-with-examples/

tr stands for translage. tr is for translating and deleting characters.

Syntax:
```
tr [OPTION] SET1 [SET2]

OPTION:
-c: complements the set of characters in string
-d: delete characters in the first set from the output
-s: replaces repeated characters listed in the SET1 with single occurence
-t: truncates SET1
```

Example 1: how to convert lower case to upper case
```bash
echo "Budj" | tr "[a-z]" "[A-Z]"
```

Example 2: translate white-space to tabs
```bash
echo "dewa budjana" | tr "[:space:]" '\t'
```

Example 3: tranlate braces to parenthesis
```bash
echo "{dewa} budjana" | tr '{}' '()'
or
tr '{}' '()' file.txt
```

Example 4: delete specified char using -d
```bash
echo "hyang giri" | tr -d 'g' # otuput: hyan iri
echo "dafuq 123" | tr -d "[:digit:]" # output: dafuq
```

Example 5: complement the sets using -c options
```bash
echo "dafuq 123" | tr -cd "[:digit:]" # output: 123
```

## uniq
`uniq` = unique.

Examples:
```bash
$ cat file.txt
wanjir
wanjir
kancut men
kancut

$ uniq file.txt
wanjir
kancut men
kancut

$ uniq -c file.txt # it counts the number of repetitions
2 wanjir
1 kancut men
1 kancut

$ uniq -D file.txt # print only duplicate lines
wanjir
wanjir
```

## xargs
...

# Basic Networking
## traceroute
print the route packets trace to network host.
Example:
```
$ traceroute google.com
```

## dig
DNS lookup utility. Example:
```
$ dig geekflare.com
```

## telnet
user interface to the TELNET protocol. used to check if the connection is ok. example:
```
telnet geekflare 443
```

## netstat
Print network connections, routing tables, interface statistics, masquerade connections, and multicast memberships.

Review network connection and open sockets.

Examples:
```bash
# display routing table
netstate -r

# display network services
netstate -i

# continuous monitorign
netstat -c

# see tcp connections
netstat -t

# see udp conn
netstate -u

# see state LISTENING
netstate -L

# practical use
netstate -tulpn # p: display programe name, n: numeric
```

## lsof
lsof lists the open files associated with an application. Example:
```bash
lsof -i tcp:80
```

## nmap
check opened ports. port scanner.

# Loop, Conditional, etc
## Loops
Example 1:
```bash
for i in {1..4}
do
    echo "$i"
done

# output:
# 1
# 2
# 3
# 4
```

Example 2:
```bash
for i in {0..4..2}
do 
    echo "$i"
done

# output
# 0
# 2
# 4
```

Example 3:
```bash
for file in server.cpp plain.zip
do
	wc $file
done

# output:
# 19  49 484 server.cpp
# 143900   815790 44879792 plain.zip
```

## Conditional
Example 1:
```bash
var="kancut"
if [ "$var" = "abc" ]; then
    echo "true"
else
    echo "false"
fi
```

Example 2:
```bash
x=0
y=1
if [ "$x" -eq "$y" ]; then
    echo "x is equal to y"
elif [ "$x" -gt "$y" ]; then
    echo "x is greater than y"
elif [ "$x" -lt "$y" ]; then
    echo "x is less than y"
fi

if [ "$x" -ne "$y" ]; then
    echo "x is not equal to y"
fi
```

Example 3:
```bash
name="jeff beck"
# check if it's an empty string
if [ -z "$name" ]; then
    echo "name is an empty string"
fi

# check if the length is not zero
if [ "$name" ]; then
    echo "name's length is NOT zero"
fi
```

Example 4:
```bash
file_1="server.cpp"
file_2="one.cpp"
dir_1="cpp"
dir_2="catch2"

if [ -f "$file_1" ]; then
	echo "$file_1 exists"
fi

if [ -f "$file_2" ]; then
    echo "$file_2 exists"
fi

if [ -d "$dir_1" ]; then
    echo "$dir_1 exists"
fi

if [ -d "$dir_2" ]; then
    echo "$dir_2 exists"
fi
```

`-f` and `-d` do not work recursively (i.e. they do not look inside other directories).

For other than `-f` and `-d`,  see: http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_07_01.html 

## Arithmethic Operations
Example:
```bash
x=2
y=9
echo `expr "$x" + "$y"`
echo `expr "$x" - "$y"`
echo `expr "$x" \* "$y"`
echo `expr "$x" / "$y"`

i=0
#increment
((i=i+1))
```

## Array
Examples: https://www.thegeekstuff.com/2010/06/bash-array-tutorial/

Example 1:
```bash
unix[0]='Debian'
unix[1]='Fedora'

echo ${unix[1]} # output: Fedora
```

Example 2: `declare -a` declares an array
```bash
declare -a unix=('Debian' 'Fedora')

# print all elements
echo ${unix[*]}

# print the length of the array
echo ${#unix[*]}

# print the length of the element located at index 1
echo ${#unix[1]}

# print subset
Unix=('Debian' 'Red hat' 'Ubuntu' 'Suse' 'Fedora' 'UTS' 'OpenLinux');
echo ${Unix[@]:3:2} # output: Suse Fedora
```

## Get return status of last executed command
Syntax: `?`

Example:
```bash
ls # assume ls runs successfully 
echo $? # print 0 (return value of success status)
```

## to uppercase and to lowercase
Example:
```bash
var="aLaY"
echo ${var,,} # to lowercase
echo ${var^^} # to uppercase
```

## 2>&1
https://stackoverflow.com/questions/818255/in-the-shell-what-does-21-mean

https://www.brianstorti.com/understanding-shell-script-idiom-redirect/ 

File descriptor 1 is the `stdout`.

File descriptor 2 is the `stderr`.

`2>&1` means "redirect the `stderr` to the same place we are redirectering the `stdout`".

Example:
```bash
$ ./main.out > output.txt 2>&1 # this will save stderr and stdout output to output.txt, but nothing appears on screen

$ ./main.out 2>&1 | tee output.txt # this will save stderr and stdout to output.txt, they also appear on screen
```