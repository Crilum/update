# update-app-script
Updates apps from [`Apt`](https://en.wikipedia.org/wiki/APT_(software)),  [`Pi-Apps`](https://github.com/Botspot/pi-apps),     [`flatpak`](https://www.flatpak.org/), and the [`Snap Store`](https://snapcraft.io/) ([`snapd`](https://snapcraft.io)).




# Install
```
curl "https://raw.githubusercontent.com/Crilum/update-app-script/main/install" | sudo bash
```

#### Manual install 
 <details> 

Clone the repository:
```
 git clone https://github.com/Crilum/update-app-script/
```

Or, if you have GitHub CLI:
```
gh repo clone Crilum/update-app-script
```

Copy the Update Script to `/usr/local/bin/`:
```
cd update-app-script && sudo cp update /usr/local/bin/update
```

Make it executable:
```
sudo chmod +x /usr/local/bin/update
```

Remove the cloned repository (This is optional):
```
rm /path/to/update-app-script
```

</details>
 
 


# Uninstall
Just remove the script:

```
sudo rm /usr/local/bin/update
```

and you're done!


# Usage
You can use `update` like this:
```
update - Updates apps installed with Apt.
update all - Updates apps on all supported systems.
update pi-apps - Updates apps installed with pi-apps.
update npm - Updates all npm apps.
update snaps - Updates apps installed with the snap store and snapd.
update flatpak - Update Flatpak build instances.
update self-update - Updates the update script
update help - Displays a help.
```

# What if I don't have Pi-Apps, snapd or Flatpak?
Well, that's fine. If you have a Debian/Ubuntu based distro, just use the `update` command alone.

But, if you want to install Pi-Apps, snapd, or Flatpak, you can do it like this:
### Pi-Apps

If you have a Raspberry Pi, I strongly reccomend Pi-Apps.

You can install Pi-Apps like this:
```
wget -qO- https://raw.githubusercontent.com/Botspot/pi-apps/master/install | bash
```
Note: Pi-Apps is intended for use on the Raspberry Pi (Which has an ARM processor), running Raspberry Pi OS, Debian (Before Bullseye) or TwisterOS. 
Most to all of the apps won't work on x86 or x64 Intel or AMD processors. 
### snapd
Snaps run an app in a container.
Install like this:
```
sudo apt install snapd
```

Note: The Snap Store in Ubuntu is just a GUI for `snapd`, so the update script will also update apps from there too. `snapd` is installed by default in Ubuntu.

### Flatpak
Install Flatpak like this:
```
sudo apt install flatpak
```
