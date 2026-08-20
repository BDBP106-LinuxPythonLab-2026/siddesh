#!/bin/bash
echo "enter your filename : "
read filename
if [ -e $filename ] ; then
	echo "Your file is exist"
	if [ -s $filename ] ; then 
		echo "Your file is not empty : " $filename
	else 
		echo "your file is empty : " $filename
	fi	

else
	echo "your file is not exist"
fi


if [ -e $filename ] ; then
	if [ -f $filename ] ; then 
		echo "Your file is Regular file : " $filename
	else 
		echo "your file is not a Regular file : " $filename
	fi	
fi	

