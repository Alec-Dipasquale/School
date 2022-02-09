#Homework 6 Problem 1 a
	
	
	.data
	.text
	.globl main
main:	
	
	li	$t1, 0	#sum
	li	$t2, 1	#a
	
	loop:
		#Exit the loop $t2 = 5
		beq	$t2, 5, exit
		#adds a($t2) to sum($t1)
		add	$t1, $t1, $t2
		#adds  + 1 to sum
		addi	$t1, $t1, 1
		#Increment loop
		addi	$t2, $t2, 1
		j	loop
	
		
	#Script for exiting loop
	#prints sum and then exits program	
	exit:
		move	$a0,$t1
		li	$v0, 1
		syscall
		li	$v0, 10
		syscall
