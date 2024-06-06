# Inter-process communication
In this chapter you will learn the concepts provided by operating system to allow processes
and threads to communicate with each other and to coordinate their work.

## Types of communication
The OS provides mechanisms allowing processes and threads to communicate with each other which is called inter-process communicate

The most popular types of IPCs:
    - shared memory
    - message passing

### Shared memory IPC
    store data
    |-----v     |-------v
Task #1 <-----------> Task #2
             ^
        unprotected memory
                                `User space`
#### Advantages
- The fastest way to achive inter-process communication

#### Disadvantages
- Not the safest communication between the tasks.
- OS no longer provides the interfaces and protection of the shared memory.
- Does not scale beyond one machine, will have the problems in large distributed systems

### Message passing IPC
In this way, each task is identified by a unique name, and tasks interact with each other by sending
and receiving messages to and from named tasks.
OS establishes a communication channel and provides proper system calls for tasks to pass messages through this channel.

There are a lot of technologies to implement the message passing approach; we will cover some of the msot common 
ones in modern operating systems pipes, sockets, and message queues - in the sectiosn below.

#### Pipes
The simplest form of IPC.
Synchronized way of transferring information from one task to another. |------> NOT <----->

There are two types of pipe:
- unnamed: used by related tasks
    + child-parent
    + sibling processes
    + threads in the same process
- named: disappear after the tasks finish using them


