- systemd makes sure it stops services cleanly: kill all the children that the main process forks too. no zombie.
- every service in systemd is controlled by cgroup