#!/usr/bin/env sh
env=$1

if [[ "$env" != "des" && "$env" != "pre" && "$env" != "pro" ]]; then
  env=$NODE_ENV
fi

