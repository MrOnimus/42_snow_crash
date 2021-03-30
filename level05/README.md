# The way we've solved this

1. After logging into the **level05** user, we will get the "You have a new mail" notification. So, let's check what's that.
2. After checking out, how can we read an email in this (article) [https://devanswers.co/you-have-mail-how-to-read-mail-in-ubuntu/] we considered trying `less /var/mail/level05` command. That gets us some strange string, very similar to the cron job: `*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05`, which definitely executes file /usr/sbin/openarenaserver. So let's check out, what's that.
3. After executing `cat /usr/sbin/openarenaserver` we got the body of this script, which basically executes each file in the `/opt/openarenaserver` directory with time limitations, and then removes it.
4. Let's exploit that by making script `letsgetthisflag` with the next content `/bin/getflag >/tmp/flag` in the `/opt/openarenaserver` folder. Now we should wait up to 2 minutes this cron job to happen.
5. After this very long minute or two we can finally get desired flag by executing `cat /tmp/flag`: `viuaaale9huek52boumoomioc`.
