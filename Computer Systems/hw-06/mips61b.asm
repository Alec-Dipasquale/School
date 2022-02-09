#Homework 6 question 1 b
#Sum of sums of (a+b+1) 
#where 	a = 1 to 3,
#	b = 1 to 3

	.data
	.text
	.globl main

main:
	li 	$t0, 1	#a
	li	$t1, 1	#b
	li	$t2, 0	#sum
	
	#loop for incrementing a and adding it to function
	loop1:
		beq	$t0, 4, exit1
		li	$t1, 1	#reset b
		#loop within loop1 for incrementing b and adding it to function
		loop2:
			#exits b's loop after it hits 3
			beq	$t1, 4, exit2
			add	$t2, $t2, $t0
			add	$t2, $t2, $t1
			addi	$t2, $t2, 1
			addi	$t1, $t1, 1
			j	loop2
		#exit of b's loop that increments a and goes back to start of loop1
		exit2:
			addi	$t0, $t0, 1
			j	loop1
	#Final exit that prints final sum and exits program.
	exit1:
		move	$a0, $t2
		li	$v0, 1
		syscall
		
		li	$v0, 10
		syscall	