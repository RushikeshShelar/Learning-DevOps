#!/bin/bash

MY_LIST=(one two three four five)
for item in ${MY_LIST[@]}; do
	echo -n $item | wc -c; done
