#!/bin/bash

curl -s https://www.puzzle-bridges.com/ > page

echo -n "task_string: "; cat page | grep -Po "var task = ['\"]\K[^ '\"]*"
echo -n "width: "; cat page | grep -Po "puzzleWidth: \K[^,]*"
echo -n "height: "; cat page | grep -Po "puzzleHeight: \K[^,]*"
