# The way we've solved this

1. After logging into the **level07** user, we can see one new binary file, named `level07`. According to our tradition, let's check this file with the strings utility: `strings level07`. While scrolling through all the meaningful lines in this binary, we've stumbled upon one interesting line: `/bin/echo %s`, and one line above `LOGNAME`. We have the variable with the same name in list of our environment variables.
2. Let's try to exploit that by substituting the content of `LOGNAME` environment variable with our command `getflag`. Of course, it should be invoked as a command, instead it will be echoed as a normal string.
3. Now let's try to start our executable `level07` again. Finally, we've got our flag, and access to the user **level08**: `fiumuikeil55xe9cu4dood66h`.
