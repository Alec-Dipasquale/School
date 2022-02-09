#Homework 5 Problem 1
#This program prints out the sum of 3 input integers.
	#Create the strings for prompts
	.data
	prompt1: .asciiz	"First Number: "
	prompt2: .asciiz	"Second Number: "
	prompt3: .asciiz	"Thrid Number: "
	
	.text
	.globl main
main:
	#Prints first prompt
	la	$a0, prompt1
	li	$v0, 4
	syscall
	
	#Get first input:
	li	$v0, 5
	syscall
	
	#Store first input:
	move $t0, $v0
	
	#Prints second prompt
	la	$a0, prompt2
	li	$v0, 4
	syscall
	
	#Get second input:
	li	$v0, 5
	syscall
	
	#Store second input:
	move $t1, $v0
	
	#Prints third prompt
	la	$a0, prompt3
	li	$v0, 4
	syscall
	
	#Get third input:
	li	$v0, 5
	syscall
	
	#Store third input:
	move $t2, $v0
	
	#Get the sum and store it in $t0
	add $t0, $t0, $t1
	add $t0, $t0, $t2
		
	#Print final output
	move $a0, $t0
	li $v0, 1
	syscall
	
	#End program
	li	$v0, 10
	syscall
	
