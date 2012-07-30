# cowboybeepbot

This is a python script to run at an interval of about every 10 minutes to set
the UCSB subreddit's theme depending upon the elevation of the sun. It also
handles updating the sidebar so the content of the sidebar can be put under
`git`.

The script is designed to run nearly anywhere as long as the python packages
`astral` and `praw` are there. Additinally, some sort of mechanism to run
commands on an interval should be present and `cron` is the usual go-to tool
for this. No error checking in the script because the Python reddit library in
this does not throw exceptions upon errors in the stylesheet updating code.

For now, this script is running periodicially every ten minutes on Heroku as it
is a great place to host small Unix scripts. Ensure the `REDDIT_USER`,
`REDDIT_PASS`, and `REDDIT_SUBREDDIT` variables are set in Heroku before
proceeding. Once set, `heroku run bash` and `python cowboy.py` to ensure it
works manually. There is no `cron` functionality in Heroku so use their
scheduler addon to run `python cowboy.rb` every 10 minutes. This is granular
enough for what is being done.

To keep it simple for hosting on Heroku, this is only the
python-uploading-at-an-interval portion since I don't want to try and deploy
a hybrid ruby and python project. _Only place verified production CSS files in
the master branch in the stylesheets and markdown folders, respectively_. If it
doesn't pass the cssfilter in reddit, the upload will silently fail. You must
also ensure that images have been uploaded beforehand.  Verification and image
upload are done by hand, for now. Also, note that the new images are only put
in effect once the CSS is updated because reddit does a find and replace on
image references only upon updating the CSS.  This means the images must have
already been uploaded to the subreddit or else it will also silently fail. You
can verify the target reddit has been prepped per images by using the
`cowboystyle` tools or upload the stylesheet manually to check for errors for
now..

There are almost no requirements for the sidebar uploading section as it's hard
to make invalid markdown. However, the ordering of elements in the sidebar may
be integral to the CSS working but this may not always be the case. Just keep
in mind to make sure the post submit links still exist. 

Anyway, this is a small and simple tool. I'm trying to abstain from softcoding
this to keep things simple and easy to debug.
