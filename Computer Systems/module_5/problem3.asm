# Folder module_5/problem3.asm

	.text
	.globl main
main:
	li	$t0, 1
	addi	$t0, $t0, 2
	addi	$t0, $t0, 3
	addi	$t0, $t0, 4
	addi	$t0, $t0, 5
	li 	$v0, 10
	syscall
