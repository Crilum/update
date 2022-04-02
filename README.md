![logo](https://github.com/Crilum/update/blob/main/Imgs/update_simple-100x100.png)
[![update2deb](https://github.com/Crilum/update/actions/workflows/update2deb.yml/badge.svg?branch=main)](https://github.com/Crilum/update/actions/workflows/update2deb.yml)
# update
update is a small script that updates apps from [`Apt`](https://en.wikipedia.org/wiki/APT_(software)),  [`Pi-Apps`](https://github.com/Botspot/pi-apps),     [`Flatpak`](https://www.flatpak.org/), [`Homebrew`](https://brew.sh), [`NPM`](https://npmjs.com), and the [`Snap Store`](https://snapcraft.io/), a.k.a. [`snapd`](https://snapcraft.io).




# Install
```
curl "https://raw.githubusercontent.com/Crilum/update/main/install" | sudo bash
```


 <details> 
 <summary><b>If you want to install manually</b> | click to expand</summary>

<h3>There are two different ways to download the script, the first one is easier, but you can use the second one if you want.</h3>

 <h4>Method 1. Use `wget` and download `update` directly, and copy the script to `/usr/local/bin/`:</h4>
    
 
1. Make sure `wget` is installed:
     
   ```
   sudo apt install wget
   ```  
 
2. Download `update` with `wget`:
   
   ```
   wget "https://raw.githubusercontent.com/Crilum/update/main/update"
   ```  
 
3. Move `update` to `/usr/local/bin/`:
  
   ``` 
   sudo mv update /usr/local/bin/update
   ```
 
4. Make `update` executable:
   
   ``` 
   sudo chmod +x /usr/local/bin/update
   ``` 
 ##
 
<h4> Method 2. Use `git clone` and copy the script to `/usr/local/bin/`:</h4>
     
1. Clone the repository:
  
   ```
   git clone https://github.com/Crilum/update/
   ```
  
2. Or, if you have GitHub CLI:
  
   ```
   gh repo clone Crilum/update/
   ```

3. Copy the Update Script to `/usr/local/bin/`:
  
   ```
   cd update && sudo cp update /usr/local/bin/update
   ```

4. Make it executable:
  
   ```
   sudo chmod +x /usr/local/bin/update
   ```

5. Remove the cloned repository (This is optional):

     ```
     rm /path/to/update
     ```

</details>

# Uninstall
Just remove the script:

```
sudo rm /usr/bin/update
```

and you're done!


# Usage
You can use `update` like this:
```
update - Updates apps installed with Apt.
update all - Updates apps on all supported systems.
update pi-apps - Updates apps installed with pi-apps.
update npm - Updates all npm packages.
update snaps - Updates apps installed with the snap store and snapd.
update flatpak - Updates Flatpak build instances.
update homebrew - Updates apps installed with Homebrew.
update pacman - Updates apps installed with pacman.
update self-update - Updates the update script
update help - Displays a help.
```

# What if I don't have some of these package managers and/or app stores?
Well, that's fine. 

- If you have a Debian/Ubuntu based distro (apt), just use the `update` command alone.

##

### To Install any of the other package managers and/or app stores:

  ### Pi-Apps
  
  You can install Pi-Apps like this:
 
  ```
  wget -qO- https://raw.githubusercontent.com/Botspot/pi-apps/master/install | bash
  ```
  Note: Pi-Apps is intended for use on the Raspberry Pi, (Which has an ARM processor), running Raspberry Pi OS, Debian, or TwisterOS. 
  Most to all of the apps won't work on non-arm processors.

  ### snapd
  
  Install snapd like this on Debian based distros:

  ```
  sudo apt install snapd
  ```
  
  Note: The Snap Store in Ubuntu is just a GUI for `snapd`, so the update script will also update apps from there too. `snapd` is installed by default in Ubuntu.


  ### Flatpak
  Install Flatpak like this on Debian based distros:
  ```
  sudo apt install flatpak
  ```

  ### Homebrew
  
  Install Homebrew like this:
  
  ```
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  ```
  
  ### Install NPM
  
  Install NPM like this on Debian based distros:
  
  ```
  sudo apt install npm
  ```
  Note: NPM will usually only be useful for developers and software builders, so it may not be a good idea to use NPM unless you understand what you're doing.

##

## Todo

- [x] Make a Releases tesing system, so when I release an update GitHub Actions tests installation.
- [ ] Create `Contributing.md`.
- [ ] Create pull request templates.
- [ ] Create a editable configuration for `all` argument
- [ ] Create a more reliable way to check for updates that doesn't depend on a variable in the script, or modify `update2deb` to edit the script and set the right version.
