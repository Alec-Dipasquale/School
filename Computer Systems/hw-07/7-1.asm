#Hw 7 Problem 1

	.data
	.text
	.globl main
	
main:
	#memory location
	la	$s0, 0xFFFF0010
	
	li	$t1, 1
	li	$t2, 2
	li	$t3, 3
	li	$t7, 0
	
	#Store to memory location FFFF0010 w/ 3 memory locations used (0,4,8)
	sw	$t1, 0($s0)
	sw	$t2, 4($s0)	
	sw	$t3, 8($s0)
	
	#load from memory FFFF0010 +4 +4 +4
	lw	$t4, 0($s0)
	lw	$t5, 4($s0)
	lw	$t6, 8($s0)
	
	#get sum of 3 integers
	add	$t7, $t4, $t5
	add	$t7, $t7, $t6
	
	#store sum to FFFF001C
	sw	$t7, 12($s0)
	
	#load sum from FFFF001C
	lw	$t8, 12($s0)
	
	#end program
	li $v0, 10
	syscall
	