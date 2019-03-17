constantSize_bits = 8

fi = open ("input.txt", "r")
code = []

for line in fi: #fi.readline().rstrip().split('\t')
	line  = line.rstrip().split('\t')
	code.append(line)



#---------------------------------------- labels
# guardar posiciones
labels = {}
def create_variable (label, pos):
	labels.update({
		label: pos
	})

pos_rom = 0
for line in code:
	label = line[0]
	if len(label) > 0: 
		create_variable(label, pos_rom)
	pos_rom += 1


#---------------------------------------- operands
# guardar variables
variables = {}
def create_variable (name, pos):
	variables.update({
		name: pos
	})

# guardar constante
constants = {}
def create_constant (name, pos, value):
	constants.update({
		name : {
			"position" : pos,
			"value" : value
		}
	})



def is_operand_in_line (line):
	return len(line) == 3

third_column = set([line_with_operand[2] for line_with_operand in filter(is_operand_in_line, (line for line in code))])
operands = set(filter(lambda e : e not in labels, third_column ))

pos_ram = 0
for operand in operands:
	if operand.isdigit():
		create_constant(operand, pos_ram, int(operand))
	else:
		create_variable(operand, pos_ram)
	pos_ram += 1

encoding = {
	'loada' 	: '0', 
	'storea' 	: '1', 
	'adda' 		: '2', 
	'suba' 		: '3',
	'ina' 		: '400', 
	'outa' 		: '500',
	'jpos' 		: '6', 
	'jneg' 		: '7', 
	'jz' 		: '8', 
	'jnz' 		: '9', 
	'jmp' 		: 'A',
	'halt' 		: 'B00'
}

print (constants)
print(variables)


def is_program_instruction(instruction):
	return instruction in ('jpos', 'jneg', 'jz', 'jnz', 'jmp')

def is_data_instruction(instruction):
	return instruction in ('loada', 'storea', 'adda', 'suba')

def is_io_instruction(instruction):
	return instruction in ('ina', 'outa', 'halt')

converted_rom = "signal ROM : rom_mem_type:=(\n"
pc = 0

def convertToProperPostition(pos):
	return  hex(pos)[2:].zfill(2).upper()

for line in code:
	instruction = line[1].lower()
	content = encoding[instruction]
	if is_program_instruction(instruction):
		label = line[2]
		content += convertToProperPostition(labels[label])
	elif is_data_instruction(instruction):
		operand = line[2]
		if operand.isdigit():
			content += convertToProperPostition(constants[operand]["position"])
		else:
			content += convertToProperPostition(variables[operand])

	converted_rom += "{} => X\"{}\",\n".format(pc, content)
	pc += 1

converted_rom += "others => x\"000\");"

print (converted_rom)
print ("//")

def convertToProperValue(value, constantSize_bits):
	size = 1 if constantSize_bits == 4 else 2
	return  hex(value)[2:].zfill(size).upper()

converted_ram = "signal RAM : ram_mem_type:=(\n"
for constant in constants:
	value = convertToProperValue(constants[constant]["value"], constantSize_bits)
	converted_ram += "{} => X\"{}\",\n".format(constants[constant]["position"], value)


converted_ram += "others => X\"{}\");".format(convertToProperValue(0, constantSize_bits))
print (converted_ram)
