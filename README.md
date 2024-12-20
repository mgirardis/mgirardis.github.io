# How to add a publication (in my modified site)
1. include it in the bib file that's referenced within `markdown_generator/PubsFromBib.ipynb` and run this script (publications should contain year, month and abstract, other than the usual bibtex tags)
2. update the TOC by running `./build_toc_for_page.ipynb` set for `publications`

# How to add a talk (in my modified site)
1. duplicate a talk file inside the `./_talks` folder and modify it accordingly (make sure to make a `location` tag in the header with the city name where the talk was given)
2. update the talk map by running the `./talkmap.ipynb` script to generate the maps with cities where the talks were given
3. update the TOC by running `./build_toc_for_page.ipynb` set for `talks`

# How to add a teaching event
1. duplicate a file inside `./_teaching` directory and modify it accordingly
2. need to verify whether the CSS styling is compatible (TO-DO)

# How to add a highlight
1. highlights are blog post (like news in a site); so duplicate one of the files in `./_highlights` and modify it accordingly
2. need to verify whether the CSS styling is compatible (TO-DO)

# How to add a new top menu item
1. modify `./_data/navigation.yml` to include a page
2. add the proper settings to `./_config.yml` (e.g., the `collections` settings and the `defaults` settings)
3. I believe that the `path` tag in the `defaults` config must match the `./_FOLDER` where the pages to be listed in the new page corresponding to the new menu item will be placed. 
4. I also believe that the `path` tag in the `defaults` must match with the filename (either `.md` or `.html`) of the page the menu link will refer to in the folder `./_pages`
5. The page added in `./_pages` will have the liquid variable `site.FOLDER` where `FOLDER` is the name of the folder created in step 2. This variable contains all the _posts_, each of which is an `md` or `html` file in `./_FOLDER`

# How to add people
1. duplicate a file inside `./_people` directory and modify it accordingly
3. if a new category of people is needed (other than PI, students, collabs), then include it in the sort order `people-order` in `./_config.yml`

# Original README below this point

A Github Pages template for academic websites. This was forked (then detached) by [Stuart Geiger](https://github.com/staeiou) from the [Minimal Mistakes Jekyll Theme](https://mmistakes.github.io/minimal-mistakes/), which is © 2016 Michael Rose and released under the MIT License. See LICENSE.md.

I think I've got things running smoothly and fixed some major bugs, but feel free to file issues or make pull requests if you want to improve the generic template / theme.

### Note: if you are using this repo and now get a notification about a security vulnerability, delete the Gemfile.lock file. 

# Instructions

1. Register a GitHub account if you don't have one and confirm your e-mail (required!)
1. Fork [this repository](https://github.com/academicpages/academicpages.github.io) by clicking the "fork" button in the top right. 
1. Go to the repository's settings (rightmost item in the tabs that start with "Code", should be below "Unwatch"). Rename the repository "[your GitHub username].github.io", which will also be your website's URL.
1. Set site-wide configuration and create content & metadata (see below -- also see [this set of diffs](http://archive.is/3TPas) showing what files were changed to set up [an example site](https://getorg-testacct.github.io) for a user with the username "getorg-testacct")
1. Upload any files (like PDFs, .zip files, etc.) to the files/ directory. They will appear at https://[your GitHub username].github.io/files/example.pdf.  
1. Check status by going to the repository settings, in the "GitHub pages" section
1. (Optional) Use the Jupyter notebooks or python scripts in the `markdown_generator` folder to generate markdown files for publications and talks from a TSV file.

See more info at https://academicpages.github.io/

## To run locally (not on GitHub Pages, to serve on your own computer)

1. Clone the repository and made updates as detailed above
1. Make sure you have ruby-dev, bundler, and nodejs installed: `sudo apt install ruby-dev ruby-bundler nodejs`
1. Run `bundle clean` to clean up the directory (no need to run `--force`)
1. Run `bundle install` to install ruby dependencies. If you get errors, delete Gemfile.lock and try again.
1. Run `bundle exec jekyll liveserve` to generate the HTML and serve it from `localhost:4000` the local server will automatically rebuild and refresh the pages on change.

# Changelog -- bugfixes and enhancements

There is one logistical issue with a ready-to-fork template theme like academic pages that makes it a little tricky to get bug fixes and updates to the core theme. If you fork this repository, customize it, then pull again, you'll probably get merge conflicts. If you want to save your various .yml configuration files and markdown files, you can delete the repository and fork it again. Or you can manually patch. 

To support this, all changes to the underlying code appear as a closed issue with the tag 'code change' -- get the list [here](https://github.com/academicpages/academicpages.github.io/issues?q=is%3Aclosed%20is%3Aissue%20label%3A%22code%20change%22%20). Each issue thread includes a comment linking to the single commit or a diff across multiple commits, so those with forked repositories can easily identify what they need to patch.
