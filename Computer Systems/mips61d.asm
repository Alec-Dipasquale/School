#Homework 6 problem 1 d
#Sum of sums of (a+b+c+d+1) 
#where 	a = 1 to 2,
#	b = 1 to 2,
#	c = 1 to 2,
#	d = 1 to 2

	.data
	.text
	.globl main
	
main:
	li	$t0, 1	#a
	li	$t1, 1	#b
	li	$t2, 1	#c
	li	$t3, 1	#d
	li	$t4, 0	#sum
	
	#loop 1 for incrementing a and resetting b
	loop1:
		beq	$t0, 3, exit1
		li	$t1, 1
		#loop2 for incrementing b and resetting c
		loop2:
			beq	$t1, 3, exit2
			li	$t2, 1
			#loop3 for incrementing c and resetting d
			loop3:
				beq	$t2, 3, exit3
				li	$t3, 1
				loop4:
					beq	$t3, 3, exit4
					add	$t4, $t4, $t3
					add	$t4, $t4, $t2
					add	$t4, $t4, $t1
					add	$t4, $t4, $t0
					addi	$t4, $t4, 1
					addi	$t3, $t3, 1
					j	loop4
				#increment c
				exit4:
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
		move	$a0, $t4
		li	$v0, 1
		syscall
		
		li	$v0, 10
		syscall
		