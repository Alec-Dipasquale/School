# Folder L1/1.asm

	.text
	.globl main
main:
	li	$t0, 2
	li	$t1, 3
	add	$t5, $t1, $t0
	li $v0, 10
	syscall