#Homework 5 Problem 2
#This program prints out the result of x^2-n * y^2
#where x,n and y are predefined to 2, 5 and 3 respectively
	.data
	.text
	.globl main
main:
	#sets x to $t0, y to $t2, and n to $t1
	li	$t0, 2
	li	$t1, 5
	li	$t2, 3
	
	#squares $t0
	mul	$t0, $t0, $t0
	
	#squares $t2
	mul	$t2, $t2, $t2
	
	#multiplies $t1 and $t2 and stores it in $t1
	mul	$t1, $t1, $t2
	
	#Subtracts $t1 from $t0 and stores it in $t0
	sub	$t0, $t0, $t1
	
	#Prints final result
	move 	$a0, $t0
	li	$v0, 1
	syscall
	
	#exits program
	li 	$v0, 10
	syscall

