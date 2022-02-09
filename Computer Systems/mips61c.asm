#Homework 6 problem 1 c
#Sum of sums of (a+b+c+1) 
#where 	a = 1 to 2,
#	b = 1 to 2,
#	c = 1 to 2

	.data
	.text
	.globl main
	
main:
	li	$t0, 1	#a
	li	$t1, 1	#b
	li	$t2, 1	#c
	li	$t3, 0	#sum
	
	#loop 1 for incrementing a and resetting b
	loop1:
		beq	$t0, 3, exit1
		li	$t1, 1
		#loop2 for incrementing b and resetting c
		loop2:
			beq	$t1, 3, exit2
			li	$t2, 1
			#loop3 for incrementing c and adding a,b, and c to sum
			loop3:
				beq	$t2, 3, exit3
				add	$t3, $t3, $t2
				add	$t3, $t3, $t1
				add	$t3, $t3, $t0
				addi	$t3, $t3, 1
				addi	$t2, $t2, 1
				j	loop3
			#increments b
			exit3:
				addi	$t1, $t1, 1
				j	loop2
		#increments a
		exit2:
			addi	$t0, $t0, 1
			j	loop1
	#prints final sum and exits program
	exit1:
		move	$a0, $t3
		li	$v0, 1
		syscall
		
		li	$v0, 10
		syscall
		