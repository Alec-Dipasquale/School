#Hw 7 Problem 3

	.data
		#declare 3 arrays and a space
		ArrayA:	.word 2,3
		ArrayB: .word 4,5
		ArrayC: .word 0,0
		space: .asciiz " "
	.text
	.globl main
	
main:
	#store array memory location
	la	$t0, ArrayA
	la	$t1, ArrayB
	la	$t2, ArrayC
	
	#load first value from arrays
	lw	$t3, 0($t0)
	lw	$t4, 0($t1)
	
	#get sum
	add	$t5, $t3, $t4
	
	#store first value in array c
	sw	$t5, 0($t2)

	#load second value from arrays
	lw	$t3, 4($t0)
	lw	$t4, 4($t1)
	
	#get sum
	add	$t5, $t3, $t4
	
	#store second value in array c
	sw	$t5, 4($t2)
	
	#load both c values
	lw	$t6, 0($t2)
	lw	$t7, 4($t2)
	
	#print first c value
	move	$a0, $t6
	li	$v0, 1
	syscall
	
	#print space between 1st and 2nd c values
	la	$a0, space
	li	$v0, 4
	syscall
	
	#print second c value
	move	$a0, $t7
	li	$v0, 1
	syscall
	
	#end program
	li	$v0, 10
	syscall
	


