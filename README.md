pyncho
======

pyncho v1: a screaming comes across the sky

A Python port of the blogging software poncho: http://pha.hk/wiki/poncho

Also contains a port of the markup language marxup: http://pha.hk/wiki/marxup
(either of version 1.5 or 0.6.5 depending on who you ask, marxup is more
fragmented than Android)

Usage
-----

```bash
pyncho prepare                      # set up your blog
pyncho post about                   # make an about page
pyncho generate                     # generate the HTML
pyncho post i ate a banana          # post your first post!!
pyncho generate                     # generate HTML again
pyncho post i ate another banana    # post more posts
pyncho post that was my last banana
pyncho generate                     # remember to generate HTML
```

Rules
-----

* You shouldn't post more than once a day. If you do, pyncho is unable to
  guarantee the posting order. This is a feature to restrict EXCESSIVE
  BLOGGING.

* You can't post several posts with the same name. It's not allowed!

* `pyncho generate` will skip posts that haven't been updated since the last
  time. If you want to force them to update you can delete the .html file in
  `output_path` first. You can also just `touch` the post files.

Available hooks
---------------

Must be +x and reside in .pyncho/hooks:

* before-info
* after-info
* before-post
* after-post
* before-generate
* after-generate
