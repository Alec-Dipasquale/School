#Homework 5 Problem 3
#This program prints out the result of x^3 + y^3 + z^3
#where x,y and z are predefined to 3, 4 and 5 respectively

	.data
	.text
	.globl main
main:
	#stores int values representing x, y , z and a temp as $t4
	li $t0, 3
	li $t1, 4
	li $t2, 5
	li $t4, 0
	
	#cubes $t0 using $t4 as temp storage
	mul 	$t4, $t0, $t0
	mul 	$t0, $t4, $t0
	
	#cubes $t1 using $t4 as temp storage
	mul 	$t4, $t1, $t1
	mul 	$t1, $t4, $t1
	
	#cubes $t2 using $t4 as temp storage
	mul 	$t4, $t2, $t2
	mul 	$t2, $t4, $t2
	
	#adds $t1 to $t2 and stoers it in $t1
	add	$t1, $t1, $t2
	
	#adds $t0 to $t1 and stoers it in $t0
	add	$t0, $t0, $t1
	
	
	#quits program
	li	$v0, 10
	syscall
