.data
prompt1: .asciiz "Enter first integer: "
prompt2: .asciiz "Enter second integer: "
prompt3: .asciiz "Enter third integer: "
message: .asciiz "The sum of the three integers is: "

.text
#prompt the user to enter first integer
li $v0,4
la $a0, prompt1
syscall

#Get the first integer
li $v0,5
syscall

#Store the result in $t0
move $t0,$v0

#prompt the user to enter second integer
li $v0,4
la $a0, prompt2
syscall

#Get the second integer
li $v0,5
syscall

#Store the result in $t1
move $t1,$v0

#prompt the user to enter third integer
li $v0,4
la $a0, prompt3
syscall

#Get the third integer
li $v0,5
syscall

#Store the result in $t2
move $t2,$v0

#Adding three integers and keeping $t3
add $t1,$t1,$t0
add $t3,$t1,$t2

#Display message
li $v0,4
la $a0,message
syscall

#Print the sum
li $v0,1
move $a0,$t3
syscall