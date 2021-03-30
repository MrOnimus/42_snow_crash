# The way we've solved this

1. After logging into the level02 user, we can observe file named level02.pcap in the home directory of the user. After checking what type of file it is we know, that it's Packet Capture data file type, which can be opened with Wireshark.
2. We've opened this file with the Wireshark, and among other frames of packets we've found a frame with suspicious string "_Password_".
3. Using tool Follow -> Follow TCP Stream we observed full stream, in which the string "_Password_" encountered.
4. Opening that stream, we can see something, that appears to be password from the next level: `ft_wandr...NDRel.L0L`, but after we've tried to use it as a password from user **flag02**, we definitely can say it's not the password.
5. After opening that stream in HEX and checking for the ASCII codes of chars in that stream we may notice that what we thought were dots symbols are actually symbols of Backspace, and the last one of them is symbol of carriage return, or, to make it simple, Enter symbol. So, according to their functions, we delete all functional symbols, and get the actual password: `ft_waNDReL0L`.
6. Logging into user **flag02** we launch command `./getflag` to get the actual flag: `kooda2puivaav1idi4f57q8iq`.
