# The way we've solved this

1. After logging into the **level06** user, we can see two new files in home directory: executable named `level06` and PHP file `level06.php`. Checking the first file did not give us much, so let's check out the second.
2. The second file is a small PHP program, which makes some substitutions on file content of the file passed into the program as the first argument. We're specifically interested in the `$a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a);` operation, because it's vulnerable to the bash command injection. As we can see, our bash command should wrapped into something like [x ${`<our command>`}].
3. Let's exploit that by making script `letskekphp` with the next content [x ${`getflag`})] in our beloved `/tmp` folder. Now we should heck the `level06` file by sending there path of our script like that: `./level06 /tmp/letskekphp`. As a result we get the token from the **level07** user in the notice message of PHP: `wiok45aaoguiboiki2tuin6ub`.
