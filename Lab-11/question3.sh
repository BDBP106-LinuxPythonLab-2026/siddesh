#!/bin/bash


echo "enter your string : "
read str


if [ -z $str ] ; then
	echo "your string is empty "

elif [ -n $str ] ; then 
	echo "your string is not empty"
fi	
