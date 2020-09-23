# Parsing syslog

Source: 
- https://www.youtube.com/watch?v=dv328WQlUQg
- https://www.youtube.com/watch?v=sFe4c6KBn9s
- next: https://youtu.be/3P3x09ZrT0E?t=1789

Syslog sample:

```
2015 Apr 2 14:25:06 switch1 %ETHPORT-5-IF_DOWN_INTERFACE_REMOVED: Interface Ethernet5/1 is down (Interface removed)
2015 May 18 12:43:15 switch2 %ETHPORT-5-IF_DOWN_LINK_FAILURE: Interface Ethernet1/4 is down (Link failure)
```

We can group each line as:

```
{2015 Apr 2} {14:25:06} {switch1} {%ETHPORT-5-IF_DOWN_INTERFACE_REMOVED}: {Interface Ethernet5/1 is down (Interface removed)}
```

Or:

```
Datestamp timestamp device error_code: error_message
```

```python
import re

DATE_RE = r'^(\d{4}\s+\w+\s+\d+)'
TIMESTAMP_RE = r'(\d{2}:\d{2}:\d{2})'
DEVICE_RE = r'\s+'
DEVICE_RE = r'\S+'
ERROR_CODE = r'%(\S+)'
ERROR_MESSAGE_RE = r'(.*)'
ERROR_CODE_RE = r'%(\S+)'
DEVICE_RE = r'(\S+)'
COLUMN_DELIMITER_RE = r'\s+'
SYSLOG_RE = (DATE_RE + COLUMN_DELIMITER_RE + TIMESTAMP_RE + COLUMN_DELIMITER_RE \
    + DEVICE_RE + COLUMN_DELIMITER_RE + ERROR_CODE_RE + COLUMN_DELIMITER_RE + \
    ERROR_MESSAGE_RE)

for line in log_lines:
    m = re.match(SYSLOG_RE, line)
    if m:
        print(m.groups())
```