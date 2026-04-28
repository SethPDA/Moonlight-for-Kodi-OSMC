# Moonlight-for-Kodi-OSMC
This Kodi addon is first and foremost created for **OSMC** Kodi(it might work on other Kodi too) that basically closes Kodi, runs **moonlight-qt** to let you stream your **Steam Deck** or **Steam Machine** games through **Sunshine**. 

When you exit **moonlight-qt**, it restarts Kodi.

# If you need help with moonlight-qt install, or steam deck stuff, don't contact me. There are plenty of info on the internet about this.

# How to use:

For Raspberry pi 4 and 5, use this guide:
https://github.com/moonlight-stream/moonlight-docs/wiki/Installing-Moonlight-Qt-on-Raspberry-Pi-4

After it is installed, SSH into your OSMC install and try running moonlight-qt from the terminal. It won't show anything on your TV just yet, but you will see if it's even trying to work or not.

If it does, then continue with the moonlight-qt connection setup to set up your connection to Sunshine on your device(Steam Deck or Steam Machine or whatever).

then the only thing left you need to do is to execute this command:

**sudo visudo**

and at the end of the file, add this line:

**osmc ALL=(ALL) NOPASSWD: /bin/systemctl stop mediacenter, /bin/systemctl start mediacenter, /usr/bin/systemd-run**

Save and exit the file.

This is there to make sure the command is executed by the correct sudo user.

Then just install the kodi addon as normal or you can manually copy it under /.kodi/addons/

Reboot kodi.

Configuration is simple, enter the name of the device you've set up previously, and the "program" you'll access. That can be the desktop or steam or whatever.

