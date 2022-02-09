
	.data
	#Declare matrix
	A:
		row1:	.word 11,22,0
		row2:	.word 0,33,44
		row3:	.word 0,0,55
	.text
	.globl mainABC:

.space 9

TextA:

.asciiz    "Matrix A:\r\n"

TextB:

.asciiz    "Matrix B:\r\n"

TextC:

.asciiz    "Matrix C:\r\n"

TextD:

.asciiz    "Matrix D:\r\n"

crlf:

.asciiz    "\r\n"

Tab:

.asciiz "\t"

.text

la   $a0, Data

la   $a1, Scratch

addi $a2, $0, 0

jal MakeDet

addi $a0, $a1, 0

la   $a1, TextD

jal PrintDet

la   $a0, Data

la   $a1, Scratch

addi $a2, $0, 1

jal MakeDet

addi $a0, $a1, 0

la   $a1, TextA

jal PrintDet

la   $a0, Data

la   $a1, Scratch

addi $a2, $0, 2

jal MakeDet

addi $a0, $a1, 0

la   $a1, TextB

jal PrintDet

la   $a0, Data

la   $a1, Scratch

addi $a2, $0, 3

jal MakeDet

addi $a0, $a1, 0

la   $a1, TextC

jal PrintDet

addi $v0, $0, 10

syscall

PrintDet:

# $a0 - address of array

# $a1 - address of label to print

# $t0 - i

# $t1 - j

# $t2 - loop Limit (same for i and j)

# $t3 - $a0 to manipulate

addi $sp, $sp, -8

sw   $a0, 0($sp)

sw   $a1, 4($sp)

addi $t0, $0, 0

addi $t1, $0, 0

addi $t2, $0, 3

addi $t3, $a0, 0

addi $a0, $a1, 0

addi $v0, $0, 4

syscall

PrintLoop:

lw   $a0, 0($t3)

addi $v0, $0, 1

syscall

la   $a0, Tab

addi $v0, $0, 4

syscall

addi $t0, $t0, 1

addi $t3, $t3, 4

bne $t0, $t2, PrintLoop

addi $t0, $0, 0

addi $t1, $t1, 1

la $a0, crlf

addi $v0, $0, 4

syscall

bne $t1, $t2, PrintLoop

syscall

lw   $a1, 4($sp)

lw   $a0, 0($sp)

addi $sp, $sp, 8

jr $ra

MakeDet:

# $a0 - original 3 x 4 data array

# $a1 - address of resulting array

# $a2 - Column (0-3)

# $s0 - i counter

# $s1 - j counter