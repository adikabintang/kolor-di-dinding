# Parsing log values

For example, we have a log with this format:

```bash
process_name - ID - message
```

Example log:

```bash
nginx - 12 - opo kue krungu
sshd - 31 - jeritan hatiku
```

To get all the lines with ID >= 30, we can use `awk`:

```bash
awk 'BEGIN {FS=" - "} {if ($2 >=30) print $2;}' process.log
```

Read [awk notes](../../../os/linux_command.md#awk) for more info.

# Parsing timestamp in log

Sources"

- https://www.digitalocean.com/community/tutorials/the-basics-of-using-the-sed-stream-editor-to-manipulate-text-in-linux
- https://askubuntu.com/a/1215011
 
Log sample:

```bash
Jun 19 11:19:16 ah masa sih tjoy
Jun 19 11:19:23 apaan tuh? kuis dangdut
Jun 19 12:37:03 yaah basah deh
Jun 19 12:37:54 ya! kopi suusunya nikmat dan mantaaap
Jun 19 12:39:32 tongli
Jun 19 12:40:09 sozis
```

1. if we want on a particular minute, we can use `grep`

```bash
grep "Jun 19 12:37" log.txt
```

Output:

```bash
Jun 19 12:37:03 yaah basah deh
Jun 19 12:37:54 ya! kopi suusunya nikmat dan mantaaap
```

2. If we want from a particular minute/hour onwards, we can use `sed`

```bash
sed -n "/Jun 19 12:37/,$p" log.txt
```

Output:

```bash
Jun 19 12:37:03 yaah basah deh
Jun 19 12:37:54 ya! kopi suusunya nikmat dan mantaaap
Jun 19 12:39:32 tongli
Jun 19 12:40:09 sozis
```

The `-n` to print only if the pattern is found (sed by default will print all lines in the file). The `$` means "til the end", just like what `$` means in regex. `p` is the print command.

Refer to the [DigitalOcean](https://www.digitalocean.com/community/tutorials/the-basics-of-using-the-sed-stream-editor-to-manipulate-text-in-linux) for more info.

# Parsing email

Sample text:

```txt
my_foo@gmai.com dolor men kancut sit amet
lorem ipsum oioi@yahoo.com
au ah ini apaan coba ada email darisaya@kth.se tau2nya ga jelas
emang email bisa ada angkanya ya kayak gini123@gmail.com bisa lah coy
di line ini ada dua email, yaitu email1.hah@gamil.com dan email.tjoy@aalto.fi
contoh ada gini @gmail.com ga valid nih, ini juga ngga men@
apalagi ini @kancut
ini email ga valid yah email+oi@gmail.com
```

For example:

Only `A-Z`, `a-z`, `0-9`, `_`, and `.` are allowed for user name.

- To capture the username: `[0-9a-zA-Z_\.]+`
- To capture the domain name: [a-z]+\.[a-z]+
- And the username should be a full word (we don't want to get `email+oi@gmail.com`): `(^|\s)`
- Combined: grep -E "(^|\s)[0-9a-zA-Z_\.]+@[a-z]+\.[a-z]+" sample_text_email.txt
- If you want to print only the match, use `-o`: grep -oE
- Wanna count? Use `-o` then count with `wc -l`: `grep -oE "pattern" | wc -l`

# Parsing IP address

Log example:

```text
67.164.164.165 - - [24/Jul/2017:00:34:11 +0000] “GET /info.php HTTP/1.1” 200 1543 “-” “Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36”
67.164.164.165 - - [24/Jul/2017:00:34:13 +0000] “GET /favicon.ico HTTP/1.1” 404 15 “http://104.236.9.232/info.php” “Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36”
67.164.164.165 - - [24/Jul/2017:00:34:14 +0000] “GET /info.php HTTP/1.1” 200 1543 “-” “Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36”
67.164.164.165 - - [24/Jul/2017:00:34:15 +0000] “GET /info.php HTTP/1.1” 200 1543 “-” “Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36”
```

- Match the IP address: `[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}` (this...is not exactly right though)
- Count the number of IP addresses with uniq (must be sorted (reversed) first): `grep ... | sort -r | uniq -c`
- Wanna put the most frequent one? Use `sed -n "1p"`

Example: `grep -oE "([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})" nginx_access_sample.log | sort -r | uniq -c | sed -n "1p"`

Correct IP address regex:

```
(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9])\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9])\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9])\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9])
```