Here: https://www.educative.io/courses/grokking-the-system-design-interview/m2ygV4E81AR

# How to use the system

Like tinyurl.

# Requirements

See https://www.educative.io/courses/grokking-the-system-design-interview/m2ygV4E81AR

# Capacity estimation and constraints

See https://www.educative.io/courses/grokking-the-system-design-interview/m2ygV4E81AR

# Database design

See https://www.educative.io/courses/grokking-the-system-design-interview/m2ygV4E81AR

# Algorithm

## 1st option: use hash

If we want to hash the url with a certain algorithm such as MD5 and encode it with Base64:

```
res = base64_encode(md5(url))
```

The length of `res` is more than 21 characters. Why?

- `MD5` yields 128-bit output.
- base64 has [a-z, A-Z, 0-9, +, /], which are 64 combinations or 6 bit
- 128 bit hash value, encoded with base64 is `128 / 6 = 21.3`

Then, store it in key-value store. Key: `res`, val: actual URL.

Return `res` to user: `mytinyurl.com/($res)`

When user hits `mytinyurl.com/($res)`, backend will search in the key-value store with key `res`, server returns HTTP `302 Redirect` with actual url read from data store.

But what if we want a shorter `res`? Cutting the `res` will likely cause collisions.

## 2nd option: use a pre-generated unique key

With the 1st option, `res` is 21-22 character or something. What if we want 6 characters only?

1. Make a table of unique 6-char keys, call it `db-key`. If we use base64 encoding, 6 chars means `64 ^ 6` keys (~68.7 billion) keys.
2. When there is a request to shorten URL:
   1. Take one key from `db-key`
   2. Put `{key: actual url}` in another table, call it `url_db`
   3. Remove `key` from `db-key`

The rest of the operation follows the 1st option's way.
