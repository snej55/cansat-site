# React port of the website

We are in the progress of porting the website from plain HTML and JavaScript to a version made with React, to 
improve the extensibility and maintainability of our site. Follow the setup instructions to get started.

## Getting started:

These instructions require an installation of npm.

First clone the repo, and cd into the react port:
```
# clone the repo
mkdir cansat-site
cd cansat-site
git clone https://github.com/snej55/cansat-site.git .
# go into the react port
cd react-port
```

Next, install the node modules
```
# install from package.json
npm install
```

To start the site, just run:
```
# run start script
npm run start
```

Done!

The site should now be live at `localhost:3000`. Any changes you make to the code
should automatically update to the live site.