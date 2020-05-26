Read:

- https://en.wikipedia.org/wiki/Instruction_set_architecture
- https://stackoverflow.com/questions/14794460/how-does-the-arm-architecture-differ-from-x86


Instruction Set Architecture (ISA) is an abstract model of a computer, also referred as computer architecture. This abstraction is implemented as CPU.

Examples of ISA ar x86 and x64, arm blablabla

x86 has 16-bit instruction set. x64 has 32 bit instruction set.

ARM is a RISC architecture (reduced instruction set computing). x86 is a CISC (complex instruction set computing). That means x86 is capable of doing complex task with a single instruction while ARM must do multiple instruction to do the same task. ARM requires less transistors, and it is cheaper as well as less energy hungry. 

ISA defines supported data types, the registers, IO model, etc.

x86 diagram:

![x86pic](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/80186_arch.png/1024px-80186_arch.png)

Source: https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/80186_arch.png/1024px-80186_arch.png

3 types of system bus: control bus, address bus, data bus. see here: https://en.wikipedia.org/wiki/System_bus

PCIe is an expansion bus, it is fast. Used for GPU, ethernet, ssd, etc.

NVMe is the interface of the SSD. NVMe stands for Non Volatile Memory Express. It is connected to the PCIe.