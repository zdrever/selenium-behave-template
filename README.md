#### A template for end to end testing with Selenium and Behave

## Selenium

Is a framework for automating browser interactions. More information can be found [here](https://www.seleniumhq.org/)

## Behave

Is a framework for BDD (Behaviour-Driven Development). It is a common language syntax which can be used to define steps for end to end tests. It's documentation can be found [here](https://behave.readthedocs.io/en/latest/)

## Getting Started

Fork the repo. Clone and navigate into the repository and run `pip3 install -r requirements.txt`.

If you are new to selenium, you must setup your webdrivers. It is best to use a package manager to manage webdrivers. Chrome is a ubiquitous browser, therefore we will walk through some steps to setup a chrome testing environment. You must have chrome downloaded and installed, and will also need to get a version of the chromedriver.

For Mac users, simply run:

`brew install chromedriver`

Windows;

`choco install chromedriver`

Ubuntu/Debian:

`apt install chromium-chromedriver`

Note: installing using `apt` can lead to versioning issues between chrome and chromedriver as the chromedriver package sometimes lags and leads to compatability issues. You can also manage chrome driver yourself by installing via the proprietary binary found [here](https://sites.google.com/a/chromium.org/chromedriver/downloads)

Ensure that the chromedriver has been added to your path by your package manager.

At this point, issuing the command `behave` should run a simple test case which runs a google search using the chrome browser.

## General Architecture

This template is built using the Page-Object-Model (POM). This is a simple architectural pattern where each webpage is modelled by an object.

`environment.py` contains [environmental controls](https://behave.readthedocs.io/en/latest/tutorial.html#environmental-controls) for the behave framework.

There are four directories contained in this project: context, features, steps and pages:

#### context

Settings and driver instantiation. This project uses a singleton pattern to represent a webdriver.

#### features

Contains `.feature` files. These are text files conforming to [gherkin syntax](https://behave.readthedocs.io/en/latest/philosophy.html#the-gherkin-language).

#### steps

Contains files with test methods which are bound to steps in the `.feature` files.

#### pages

Contains all page objects, as well as locators for finding elements on the webpages.
