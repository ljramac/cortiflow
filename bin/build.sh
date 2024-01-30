#!/usr/bin/env sh
. ./bin/_.sh

npx env-cmd -f ./env/$env.env react-scripts build
