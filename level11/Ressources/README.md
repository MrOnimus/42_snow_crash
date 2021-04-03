# The way we've solved this

1. After logging into the **level11** user, we can see one binary file, named `level11.lua`. Obviously, that's a Lua script. If we open it, we'll see, that it's a server, written on the Lua language. This server listens to the new connections on the local network address 127.0.0.1, port 5151. This is socket-typed connection, so just "curling" it won't help us very much.
2. So, what can we do with it? Let's try to connect to it using netcat tool `nc`, which we've used already in the previous task. This time we'll use it to establish socket connection: `nc 127.0.0.1 5151`. After execution of that command in our CLI we'll see, that server asks us for the password.
3. Now, if we take another look at the script, than we'll notice, that if response will travel to the server without errors, the other function, custom hash function, will be invoked. In that function specifically we can see invocation of other process `io.popen`. So let's expose it!
4. This time, after server asks us for the password, we'll answer it with the command: "`getflag` > /tmp/flag". After that our flag will be in the `/tmp/flag` file: `fa6v5ateaw21peobuub8ipe6s`.
