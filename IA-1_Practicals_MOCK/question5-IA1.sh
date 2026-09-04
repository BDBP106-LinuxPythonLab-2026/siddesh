#!/bin/bash

echo "enter your Argument1:"
read Argument1
echo "enter your Argument2:"
read Argument2
echo "enter your Argument3:"
read Argument3
echo "enter your Argument4:"
read Argument4

count=0
until [ $count -gt 4 ]
do
	$count=$count+1
	if [ $count -eq 4 ]; then
		echo "your Argument1 is : " $Argument1

		echo "your Argument2 is : " $Argument2

		echo "your Argument3 is : " $Argument3

		echo "your Argument4 is : " $Argument4
	fi
done
















