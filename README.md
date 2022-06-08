![logo](https://github.com/Crilum/update/blob/main/images/update_simple-100x100.png)
[![update2deb](https://github.com/Crilum/update/actions/workflows/update2deb.yml/badge.svg?branch=main)](https://github.com/Crilum/update/actions/workflows/update2deb.yml)
# update
update is a small script that updates apps from [`Apt`](https://en.wikipedia.org/wiki/APT_(software)),  [`Pi-Apps`](https://github.com/Botspot/pi-apps),     [`Flatpak`](https://www.flatpak.org/), [`Homebrew`](https://brew.sh), [`NPM`](https://npmjs.com), and the [`Snap Store`](https://snapcraft.io/), a.k.a. [`snapd`](https://snapcraft.io).




# Install

```
curl "https://raw.githubusercontent.com/Crilum/update/main/install" | bash
```

This should work for most systems (Apt-based distros (not Alpine Linux, yet..), DNF-based distros, most other Linux distros, and MacOS). If it doesn't work on your system, [create an issue](https://github.com/Crilum/update/issues/new) (or even better, a PR), and I'll try to help. 

 <details> 
 <summary><b>If you want to install manually</b> | click to expand</summary>

<h3>There are two different ways to download the script, the first one is easier, but you can use the second one if you want.</h3>

 <h4>Method 1. Use `wget` and download `update` directly, and copy the script to `/usr/local/bin/`:</h4>
    
 
1. Make sure `wget` is installed:
     
   ```
   sudo apt install wget
   ```  
 
2. Download the latest version of `update` with `wget`:
   
   ```
   version="$(curl -s https://api.github.com/repos/Crilum/update/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")')"
   wget "https://github.com/Crilum/update/raw/v${version}/update"
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
     
1. Clone the latest release of the repository:
  
   ```
   version="$(curl -s https://api.github.com/repos/Crilum/update/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")')"
   git clone https://github.com/Crilum/update/ -b $version
   ```
  
2. Or, if you have GitHub CLI:
  
   ```
   version="$(curl -s https://api.github.com/repos/Crilum/update/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")')"
   gh repo clone Crilum/update -- -b $version
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
     rm -rf update/
     ```

</details>

# Uninstall

### Just uninstall the package:

#### Apt based distros:

```
sudo apt remove update
```

#### DNF based distros:

I'm not sure exactly what the command for removing the Alien package is, but it might look something like this:
```
sudo alien -r update
```

### Or, if your system doesn't have an update package:

#### Other linux:
```
sudo rm -f /usr/bin/update /usr/bin/up
```
#### MacOS:

```
sudo rm -f /usr/local/bin/update /usr/local/bin/up
```

and you're done!


# Usage
You can use `update` like this:

These are the main options/arguments for update:
```
update apt · -a · --apt [packages]         Updates apt packages
update all · -A · --all                    Updates apps on all installed package managers and/or app stores that are supported - Note: This option does not update NPM packages because this can cause trouble.
update pi-apps · -p · --pi-apps            Updates Pi-Apps, and apps installed with Pi-Apps
update npm · -n · --npm                    Updates all npm packages
update snaps · -s · --snaps [snaps]        Updates snaps with snapd
update flatpak · -f · --flatpak [packages] Updates flatpak apps
update homebrew · -H · --homebrew          Updates Homebrew apps
update pacman · -c · --pacman [packages]   Updates pacman apps
update dnf · -d · --dnf                    Updates dnf packages
update self-update · -u · --self-update    Updates the update script
update help · -h · --help                  Displays this help
update version · -v · --version            Prints version
```
Flags for update:
```
      --no-grep-args                       If this flag is specified, update won't remove arguments that are also packages from the update package list, i.e. 'apt'
```


## Todo
- [X] make a unified install script.
- [x] Make a Releases tesing system, so when I release an update GitHub Actions tests installation.
- [ ] Create `Contributing.md`.
- [ ] Create pull request templates.
- [ ] Create a editable configuration for `all` argument
- [ ] Create a more reliable way to check for updates that doesn't depend on a variable in the script, or modify `update2deb` to edit the script and set the right version.
