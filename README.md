# lubuntu-wallpaper-slideshow
Quick program to allow wallpaper slideshows on Lubuntu, or any distro with PCManFM desktop management.

Wallpapers are selected randomly from a given directory. The time between wallpapers is set with a simple cron job.

The image directory can be set by editing the script. By default wallpapers are pulled from `~/Pictures/Wallpapers/Use`.

Add the following line to your cron list using `crontab -e`
```
*/15 * * * * /path/to/script
```
Where the number is the number of minutes between runs.

Currently, I have this installed in `~/.bin`, but it could equally go in
`/usr/local/bin`.
