# update-app-script
Updates apps from [`Apt`](https://en.wikipedia.org/wiki/APT_(software)),  [`Pi-Apps`](https://github.com/Botspot/pi-apps),     [`flatpak`](https://www.flatpak.org/), and the [`Snap Store`](https://snapcraft.io/) ([`snapd`](https://snapcraft.io)).




# Install
```
curl "https://raw.githubusercontent.com/Crilum/update-app-script/main/install" | sudo bash
```

 ### Manual install 
 <details> 

Clone the repository:
```
 git clone https://github.com/Crilum/update-app-script/
```

Or, if you have GitHub CLI:
```
gh repo clone Crilum/update-app-script
```

Copy the Update Script to `/bin/`:
```
cd update-app-script && sudo cp update /bin/
```

Make it executable:
```
sudo chmod +x /bin/update
```

Remove the cloned repository (This is optional):
```
rm /path/to/repo/directory/update-app-script
```

</details>
 
 


# Uninstall
Just remove the script:

`sudo rm /bin/update`

and you're done!


# Usage
You can use `update` like this:
```
update - updates apps installed with Apt.
update pi-apps - updates apps installed with pi-apps.
update snaps - updates apps installed with the snap store and snapd.
update flatpak - update Flatpak build instances.
update help - Displays a help.
```

# What if I don't have Pi-Apps, snapd or Flatpak?
Well, that's ok, if you have a Debian/Ubuntu based distro, just use the `update` command alone.

### Pi-Apps

If you have a Raspberry Pi, I strongly reccomend Pi-Apps.

You can install Pi-Apps like this:
```
wget -qO- https://raw.githubusercontent.com/Botspot/pi-apps/master/install | bash
```
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
