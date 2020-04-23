Desired phone number pattern: `(xxx) xxx-xxxx` or `xxx-xxx-xxxx`

Example input:

```
987-123-4567
123 456 7890
(123) 456-7890
```

Output:

```
987-123-4567
(123) 456-7890
```

```bash
grep -E "^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$|^[0-9]{3}-[0-9]{3}-[0-9]{4}$" file.txt
```

The regex is splitted into two:

First,

To match the `(xxx) xxx-xxxx`:

```
^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$
```

- `^\(`: matches `(` at first char
- `[0-9]`: matches any number
- `[0-9]{3}`: matches 3 numbers
- etc.

Then, use `or` condition with `|`.

Finally, the second pattern:

```
^[0-9]{3}-[0-9]{3}-[0-9]{4}$
```
