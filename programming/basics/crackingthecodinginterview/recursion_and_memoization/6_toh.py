class Tower:
    def __init__(self):
        self.stack = []
    
    def __repr__(self):
        return str(self.stack)

    def add(self, val: int):
        self.stack.append(val)
    
    def move_top_disk_to(self, dest):
        val = self.stack.pop()
        dest.add(val)
    
    def move_disks(self, n_disk, dest, buffer):
        if n_disk == 0:
            return 

        if n_disk == 1:
            self.move_top_disk_to(dest)
            return
        
        self.move_disks(n_disk - 1, buffer, dest)
        self.move_top_disk_to(dest)
        buffer.move_disks(n_disk - 1, dest, self)

if __name__ == "__main__":
    t_a = Tower()
    t_b = Tower()
    t_c = Tower()
    t_a.add(3)
    t_a.add(2)
    t_a.add(1)
    print(t_c)
    t_a.move_disks(len(t_a.stack), t_c, t_b)
    print(t_c)
