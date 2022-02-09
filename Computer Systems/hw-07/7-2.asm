#Hw 7 Problem 2

	.data
		#Declare array w/ values
		Array:	.word 2,3,4
	.text
	.globl main

main:
	#store array memory location
	la	$t0, Array
	
	#load each value from array
	lw	$t1, 0($t0)
	lw	$t2, 4($t0)
	lw	$t3, 8($t0)
	
	#get sum
	add	$t4, $t1, $t2
	add	$t4, $t4, $t3
	
	#print sum
	move $a0, $t4
	li	$v0, 1
	syscall
		
	#end program
	li	$v0, 10
	syscall