#Hw 7 Problem 4

	.data
		#declare 3 arrays and space
		m:	.word 1,2,3,4
		v:	.word 5,6
		r:	.word 0,0
		
		space:	.asciiz " "
	.text
	.globl	main
main:
	la	$t0, m
	la	$t1, v
	la	$t2, r
	
	#load (1,1) of matrix and 1 of array
	lw	$t3, 0($t0)
	lw	$t4, 0($t1)
	
	#multiply first 2 numbs
	mul	$t5, $t3, $t4
	
	#load second numbs to multiply
	lw	$t3, 4($t0)
	lw	$t4, 4($t1)
	
	#multiply second 2 numbs
	mul	$t3, $t3, $t4
	
	#add both multiplied numbs for first numb result in r vector
	add	$t5, $t5, $t3
	
	sw	$t5, 0($t2)
	
	#load (2,1) of matrix and 1 of array
	lw	$t3, 8($t0)
	lw	$t4, 0($t1)
	
	#multiply just loaded numbs
	mul	$t5, $t3, $t4
	
	#load (2,2) of matrix and 2 of array
	lw	$t3, 12($t0)
	lw	$t4, 4($t1)
	
	#multiply just loaded numbs
	mul	$t3, $t3, $t4
	
	#add both multiplied numbs for second numb result in r vector
	add	$t5, $t5, $t3
	
	#store in memory 2nd result of r vector
	sw	$t5, 4($t2)
	
	#Load and print both r results*********************
	lw	$t6, 0($t2)
	
	move 	$a0, $t6
	li	$v0, 1
	syscall
	
	la 	$a0, space
	li	$v0, 4
	syscall
	
	lw	$t6, 4($t2)
	
	move 	$a0, $t6
	li	$v0, 1
	syscall
	#**************************************************
	
	#end program
	li	$v0, 10
	syscall