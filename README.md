![logo](https://github.com/Crilum/update/blob/main/Imgs/update_simple-100x100.png)
# update
update is a small script thet updates apps from [`Apt`](https://en.wikipedia.org/wiki/APT_(software)),  [`Pi-Apps`](https://github.com/Botspot/pi-apps),     [`flatpak`](https://www.flatpak.org/), [`homebrew`](https://brew.sh), [`NPM`](https://npmjs.com), and the [`Snap Store`](https://snapcraft.io/), a.k.a. [`snapd`](https://snapcraft.io).




# Install
```
curl "https://raw.githubusercontent.com/Crilum/update/main/install" | sudo bash
```


 <details> 
 <summary><b>If you want to install manually</b> | click to expand</summary>

 <br>

 Clone the repository:
```
git clone https://github.com/Crilum/update/
```

Or, if you have GitHub CLI:
```
gh repo clone Crilum/update/
```

Copy the Update Script to `/usr/local/bin/`:
```
cd update && sudo cp update /usr/local/bin/update
```

Make it executable:
```
sudo chmod +x /usr/local/bin/update
```

Remove the cloned repository (This is optional):
```
rm /path/to/update
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
update homebrew - Updates apps installed with Homebrew.
update self-update - Updates the update script
update help - Displays a help.
```

# What if I don't have some of these package managers and/or app stores?
Well, that's fine. 

- If you have a Debian/Ubuntu based distro, just use the `update` command alone.

<hr>

### To Install any of the other package managers and/or app stores:

  ### Pi-Apps
  
  You can install Pi-Apps like this:
 
  ```
  wget -qO- https://raw.githubusercontent.com/Botspot/pi-apps/master/install | bash
  ```
  Note: Pi-Apps is intended for use on the Raspberry Pi (Which has an ARM processor), running Raspberry Pi OS, Debian (Before Bullseye) or TwisterOS. 
  Most to all of the apps won't work on x86 or x64 Intel or AMD processors. 

  ### snapd
  
  Install snapd like this:

  ```
  sudo apt install snapd
  ```
  
  Note: The Snap Store in Ubuntu is just a GUI for `snapd`, so the update script will also update apps from there too. `snapd` is installed by default in Ubuntu.


  ### Flatpak
  Install Flatpak like this:
  ```
  sudo apt install flatpak
  ```

<hr>

Note: I'm still working on this part of the readme, and I plan to add instructions for installing all package managers/app stores that you can use with update.
## Todo

- [x] Make a Releases tesing system, so when I release an update GitHub Actions tests installation.
- [ ] Create `Contributing.md`.
- [ ] Create pull request templates.
- [ ] Create a editable configuration for `all` argument
