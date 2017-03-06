#!/bin/bash

git clone https://github.com/melta/testapp.git
cd testapp
vagrant up
xdg-open http://localhost:9999/words/
