# The way we've solved this

1. After logging into the **level04** user, we can observe Perl script file named `level04.pl` in the home directory of the user. If we cat it, we will see it's program code. In the top part of the file we can see comment "localhost:4747". Maybe that's a local address, on which this script is running.
2. Let's check ports on that local machine being used using command `netstat -tuln`. We can see, that something listens to the 4747 port. Maybe that's our script.
3. This script is waiting for one argument named `x`, which will be echoed further. We can alter this behaviour by passing not simple string, but pipe and the command we want to. Let's try with the command `getflag` we've interest in. To do that we should somehow send needed argument x to this program. Let's do this by using curl utility: `curl "localhost:4747?x=|getflag"`. It will get us the response with the token from the **level05** user: `ne2searoevaevoem4ov4ar8ap`.
