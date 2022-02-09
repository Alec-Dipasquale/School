#Homework 6 problem 2
#Sum of products of a,b,c, and 2, where all
#variables are incremented individually to 5


	.data
	.text
	.globl main
	
main:
	li	$t0, 1	#a
	li	$t1, 1	#b
	li	$t2, 1	#c
	li	$t3, 1	#product
	li	$t4, 0	#SumofProducts
	li	$t5, 2	#constant
	
	#loop 1 for incrementing a and resetting b
	loop1:
		beq	$t0, 6, exit1
		li	$t1, 1
		#loop2 for incrementing b and resetting c
		loop2:
			beq	$t1, 6, exit2
			li	$t2, 1
			#loop3 for incrementing c and adding a,b, and c to sum
			loop3:
				beq	$t2, 6, exit3
				#product of a, b, c and 2
				mul	$t3, $t3, $t2
				mul	$t3, $t3, $t1
				mul	$t3, $t3, $t0
				mul	$t3, $t3, $t5
				#adds product to sum
				add	$t4, $t4, $t3
				#increments c
				addi	$t2, $t2, 1
				li	$t3, 1
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
		