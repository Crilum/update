# update-app-script
Updates apps from `Apt`, `Pi-Apps`, and the `Snap Store`.




# Install
Clone the repository:

- `git clone https://github.com/Crilum/update-app-script/`

Copy the Update Script to `/bin/`:

- `cd update-app-script && sudo cp update /bin/`

Make it executable:

- `sudo chmod +x /bin/update`

Remove the cloned repository (This is optional):

- `rm /path/to/repo/directory/update-app-script`



# Uninstall
Just remove the script:

`sudo rm /bin/update`

and you're done!



## Tip
If you have another script in `/bin` named `update`, just rename the update script, and continue. (Just remember to change the name of the script in the install/uninstall scripts too!)
