#!/bin/sh

read -p "Commit description: " desc
git add . && \
git commit -m "$desc"