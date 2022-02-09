# Folder module_5/problem1.asm

	.text
	.globl main
main:
	li	$t0, 1
	li	$t5, 0
	add	$t5, $t5, $t0
	li	$t0, 2
	add	$t5, $t5, $t0
	li	$t0, 3
	add	$t5, $t5, $t0
	li	$t0, 4
	add	$t5, $t5, $t0
	li	$t0, 5
	add	$t5, $t5, $t0
	li $v0, 10
	syscall
