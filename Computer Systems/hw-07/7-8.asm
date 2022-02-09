#Hw 7 Problem 8


	.data
	#Declare matrix
		b:	.word	0,1,5,	1,0,4,	5,4,0
	.text
	.globl	main
main:
	#initialize final determinant
	li	$t0, 0
	la,	$t9, b
	#***************************
	lw	$t1, 0($t9)# get (1,1)
	
	lw	$t2, 16($t9)# get (2,2)
	lw	$t3, 32($t9)# get (3,3)
	
	mul	$t2, $t2, $t3
	
	lw	$t4, 20($t9)# get (3,2)
	lw	$t5, 28($t9)# get (3,2)
	
	mul	$t4, $t4, $t5
	
	sub	$t2, $t2, $t4
	
	mul	$t1, $t1, $t2
	
	add	$t0, $t0, $t1
	#*****************************
	lw	$t1, 4($t9)# get (1,2)
	
	lw	$t2, 12($t9)# get (2,1)
	lw	$t3, 32($t9)# get (3,3)
	
	mul	$t2, $t2, $t3
	
	lw	$t4, 20($t9)# get (2,3)
	lw	$t5, 24($t9)# get (3,1)
	
	mul	$t4, $t4, $t5
	
	sub	$t2, $t2, $t4
	
	mul	$t1, $t1, $t2
	
	sub	$t0, $t0, $t1
	#****************************
	lw	$t1, 8($t9)# get (1,3)
	
	lw	$t2, 12($t9)# get (2,1)
	lw	$t3, 28($t9)# get (3,2)
	
	mul	$t2, $t2, $t3
	
	lw	$t4, 16($t9)# get (2,2)
	lw	$t5, 24($t9)# get (3,1)
	
	mul	$t4, $t4, $t5
	
	sub	$t2, $t2, $t4
	
	mul	$t1, $t1, $t2
	
	add	$t0, $t0, $t1
	
	
	
	
	#PRINT
	move	$a0, $t0
	li	$v0, 1
	syscall
	
	#end program
	li	$v0, 10
	syscall
	
