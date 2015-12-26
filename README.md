# lubuntu-wallpaper-slideshow
Quick program to allow wallpaper slideshows on Lubuntu

Not much more to it than that at the moment. Simple bash script to run in the background, and chose images at random.
Images are loaded to the desktop by pcmanfm. Script is run by a cron job.

Add the following line to your cron list using `crontab -e`

```
*/15 * * * * /path/to/script
```
Where the number is the number of minutes between runs.

Currently, I have this installed in `~/.bin`, but it could equally go in
`/usr/local/bin`.
