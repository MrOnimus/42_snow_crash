# The way we've solved this

1. After logging into the **level14** user, we can see nothing. Like, you know, absolutely nothing, not to count three ordinary files, which doesn't have anything interesting for us.
2. So, why not try to kek the most interesting thing in this project? Shouldn't we? Of course we should. Let's kek by creating user, identical to the **flag14** user on our machine, and execute `getflag` there.
3. First of all, we need to know the group for all of the **flag** users. We can do it by logging under any **flag** user from the previous tasks we have access for with the command `groups`.
4. Secondly we need to get all info about user **flag14** we possibly can have. Most of it we can fetch from the `/etc/passwd` file.
5. Now, let's recreate **flag14** user using all that information, and the commands `groupadd`, `useradd`, `passwd`, `su`, and their flags. After all that operations we can execute the `./getflag` script again. This time it will get us the flag, which can be used either for accessing the **flag14** user or proving, that we've solved this level: `7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ`.
