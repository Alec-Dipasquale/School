#Hw 7 problem 6

	.data
		#declaring the 3 matrices and enter
		a:	.word	5, 3, 4,	1, 5, 3,	2, 1, 5
		x:	.word	1,2,3
		y:	.word	0,0,0
		enter:	.asciiz "\n"
	.text
	.globl	main
main:
	#initialize counter for loop
	li	$t5, 0
	li	$t1, 0
	loop:
		beq	$t5, 36, exit1
		#initialize counter for loop2 and result y(x) value
		li	$t4, 0
		li	$t9, 0 
		loop2:
			beq	$t4, 12, exit2
			#load values from arrays
			lw	$t8, a($t5)
			lw	$t7, x($t4)
			
			#multiply and add values to final result y(x) value
			mul	$t6, $t7, $t8
			add	$t9, $t9, $t6
			
			#increment by 4
			addi	$t4, $t4, 4
			addi	$t5, $t5, 4
			j	loop2
		exit2:
			#Saveto y array memory
			sw	$t9, y($t1)
			#load from memory
			lw	$t9, y($t1)
			addi	$t1, $t1, 4
			
			#PRINT
			move	$a0, $t9
			li	$v0, 1
			syscall
			la	$a0, enter
			li	$v0, 4
			syscall
			
			#jump to original loop
			j	loop
	exit1:
		#end program
		li	$v0, 10
		syscall
	
