# Folder module_5/problem2.asm

	.text
	.globl main
main:
	li	$t0, 1
	addi	$t5, $t0, 2
	addi	$t5, $t5, 3
	addi	$t5, $t5, 4
	addi	$t5, $t5, 5
	li $v0, 10
	syscall
