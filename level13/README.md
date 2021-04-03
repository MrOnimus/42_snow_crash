# The way we've solved this

1. After logging into the **level13** user, we can see one binary file, named `level13`. We execute it, and it responses us, that it will be executed fully only under user with UID 4242.
2. So, just let's create user with that UID using one of `adduser` or `useradd` commands. Being signed under that user we can freely execute that script and get the next flag: `2A31L79asukciNyi8uppkEuSx`.
