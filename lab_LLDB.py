#! /usr/bin/env python3

### labLLDB plug-in ###
### bbb (Breakpoint By Base address) ###

import lldb
import string

imageBaseAddr = 0x0

def __lldb_init_module(debugger, internal_dict):
	
	version = "1.0.0"
	print("\n### lab-LLDB v" + version + " ###\n")
	
	debugger.HandleCommand('command script add -f lab_LLDB.bbb bbb -h "bbb: set Breakpoint By Base address (0x100000000)"')
	# TODO: print registers & register pointer data
	#		  - after running ni, si...
	#		  - after being stopped by bp

def executeLLDBCommand(debugger, command):
    res = lldb.SBCommandReturnObject()
    interpreter = debugger.GetCommandInterpreter()
    interpreter.HandleCommand(command, res)

    if res.HasResult():
    	response = True, res.GetOutput()
    else:
    	response = False, res.GetError()

    return response

# check bbb argument
def checkBbbArgument(arg):
	basicImageBase = 0x100000000

	if len(arg.split(" ")) != 1:
		return 0

	# remove "0x" for converting to int
	if arg.startswith("0x"):
		arg = arg[2:]

	# check if command is hex data. 
	if all(c in string.hexdigits for c in arg) == False:
		return 0

	breakAddr = int(arg, 16)

	if breakAddr > basicImageBase:
		breakAddr -= basicImageBase

	return breakAddr

# Breakpoint By Base address
def bbb(debugger, command, result, internal_dict):
	global imageBaseAddr

	# find main binary image base address (ASLR)
	if imageBaseAddr == 0:
		ret, result = executeLLDBCommand(debugger, "image list")
		if ret == False:
			print("lab-LLDB failed : image list")
			print(result)
			return

		for element in result.splitlines( )[0].split(" "):
			if element.startswith("0x"):
				imageBaseAddr = int(element[2:], 16)

	arg = checkBbbArgument(command)
	if arg == 0:
		print("usage bbb : bbb hex_address")
		return

	breakAddr = arg + imageBaseAddr

	ret, result = executeLLDBCommand(debugger, "b " + hex(breakAddr))
	print(result)