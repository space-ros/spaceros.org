name: Deploy Website to Github Pages

on:
  push:
    branches: [ master ]

jobs:
  build_and_deploy:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
      with:
        submodules: true
    - name: Set up Python 3.10
      uses: actions/setup-python@v3
      with:
        python-version: "3.10"
    - name: Install dependencies
      run: |
        # Install Python and Pelican.
        python -m pip install --upgrade pip
        python -m pip install "pelican[markdown]"
        # Install Stork.
        cd /usr/bin/
        sudo wget https://files.stork-search.net/releases/v1.5.0/stork-ubuntu-20-04
        sudo chmod +x stork-ubuntu-20-04
        sudo ln -s stork-ubuntu-20-04 stork
    # Build the website for Production.
    - name: Build
      run: |
        cd site
        pelican content -s publishconf.py
    # Deploy the site built into the gh-pages branch.
    # You need to configure pages to be at gh-pages and serve the root folder.
    - name: Deploy
      uses: JamesIves/github-pages-deploy-action@v4
      with:
        folder: site/output
        branch: gh-pages
