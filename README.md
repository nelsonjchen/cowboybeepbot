# cowboybeepbot

This is a python script to run at an interval to set the UCSB subreddit's theme
depending upon the elevation of the sun. It also handles updating the sidebar
so the sidebar can be put under Git.

It is designed to run on Heroku. There is no error checking in this because the
Python reddit library in this does not throw exceptions upon errors in these
parts; we will have to wait on upstream for that.

For now, this script is running periodicially every ten minutes on Heroku. It's
a great place to host small scripts.

To keep it simple for hosting on Heroku, this is only the
python-uploading-at-an-interval portion.  Only place verified production CSS
and markdown files in here. If it doesn't pass the cssfilter in reddit, the
upload will silently fail. It must also be ensured that images have beep
uploaded. Verification and image upload are done by hand, for now. Also, note
that image uploading is only put in effect once the CSS is updated because
reddit does a find and replace only upon updating the CSS. 
