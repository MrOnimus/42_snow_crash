# The way we've solved this

1. After logging into the **level03** user, we can observe file named `level03` in the home directory of the user. That file is executable, so we launch it, and get the response "Exploit me".
2. We parse this file with the `strings` tool, which gets us all the readable strings observed in this file. We're interested in finding "Exploit me", so let's launch it like that: `strings level03 | grep "Exploit me"`. As a result of this command we get string "/usr/bin/env echo Exploit me". Obviously, we need to exploit /usr/bin/env at the next step.
3. We can check the owner of this file using command `ls -l ~/level03`, and find out, that user **flag03** owns this file. Knowing that, coupled with the fact the `level03` script uses echo command we can conclude, that we can perform privilege escalation by substitution of the `echo` program.
4. Let's substitute the program `echo` by creating a program of the same name in directory /tmp, in which we have write permissions. The program `echo` will contain only `/bin/getflag` invocation.
5. After that we definitely need to add new `echo` program to the $PATH, to make it available for the other system programs. We can do that by executing `export PATH=/tmp:$PATH`.
6. So, finally, let's start the **level03** program in home directory of our user. This time it will give us the token from the **level04** user: `qi0maab88jeaj46qoumi7maus`.
