# The way we've solved this

1. After logging into the **level12** user, we can see one binary file, named `level12.pl`. Again, obviously, that's a Perl script. After short examination of the given script we'll get the sense, what happens in it. The program we need to heck is listening on the 4646 port of the 127.0.0.1 address. We'll exploit execution of egrep command on `/tmp/xd` with pattern, which lays in the passed variable. There are some permutations takes place with the given arguments, so will pass our code as an executable file.
2. Let's create this file in our beloved directory `/tmp`, named `HECK`, and give all the permissions to it. The file will contain almost standard code for this project: `getflag >/tmp/flag`.
3. Now, let's pass this executable using curl to this script using next command "curl localhost:4646?x='`/*/HECK`'". After that we can check `/tmp/flag` file for the presence of the next flag: `g1qKMiRpXf53AWhDaU7FEkczr`.
