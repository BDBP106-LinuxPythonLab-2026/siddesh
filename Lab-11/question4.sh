#!/bin/bash


#> < operator, the comparison worked successfull. The shell basically interpreted that it should create a file called Nagesh due to the presence of the > symbol, hence the unwanted result. so using "\>" front of operator compres without making a new file in the current dir



val1=Jayashree
val2=Nagesh

# if [ $val > $val2 ] ; then
if [ $val1 \> $val2 ] ; then
	echo "$val1 is greater than $val2"
else
	echo "$val1 is lesser than $val2"
fi	
	

