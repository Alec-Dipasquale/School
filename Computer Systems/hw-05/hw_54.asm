#Homework 5 Problem 4
#This program places the determinant of a given matrix in $t0

	.data
	.text
	.globl main
	
main:
	#Store individual parts of matrix in registers
	li 	$t0, 4	#a/result register
	li 	$t1, 1	#b
	li 	$t2, 2	#c
	li 	$t3, 1	#d
	li 	$t4, 0	#e
	li 	$t5, 3	#f
	li 	$t6, 2	#g
	li 	$t7, 3	#h
	li 	$t8, 5	#i
	li 	$t9, 0	#temp
	
	#multiply aei and store it in $t9(temp)
	mul 	$t9, $t0, $t4
	mul 	$t9, $t9, $t8
	#multiply afh and store it in $t0(a)
	mul 	$t0, $t0, $t5
	mul 	$t0, $t0, $t7
	#subtract $t0(afh) from $t9(aei)
	sub 	$t0, $t9, $t0
	
	#multiply bfg and store it in $t9
	mul	$t9, $t1, $t5
	mul	$t9, $t9, $t6
	#Adds $t9(bfg) to $t0 and stores it in $t0
	add 	$t0, $t0, $t9
	
	#multiply cdh and store it in $t9
	mul	$t9, $t2, $t3
	mul	$t9, $t9, $t7
	#Adds $t9(cdh) to $t0 and stores it in $t0
	add 	$t0, $t0, $t9
	
	#multiply ceg and store it in $t9
	mul 	$t9, $t2, $t4
	mul 	$t9, $t9, $t6
	#subtract $t9(ceg) from $t0 and stores it in $t0
	sub 	$t0, $t0, $t9
	
	#multiply bdi and store it in $t9
	mul 	$t9, $t1, $t3
	mul 	$t9, $t9, $t8
	#subtract $t9(afh) from $t0 and stores it in $t0
	sub 	$t0, $t0, $t9

	#print result
	move 	$a0, $t0
	li 	$v0, 1
	syscall	
	
	#Ends a program
	li	$v0, 10
	syscall
