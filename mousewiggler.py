'''

Notes

TO DO
-Change the sleep timer back to 15 when done with testing.

'''
import pyautogui, time, random

# welcome message and explanation of program
print('Welcome to Mouse Wiggler by GrizzledLabs\n')
print('This program prevents computer sleeping')
print('...by wiggling your mouse every 15 seconds\n')
print('After entering desired time in minutes you will')
print('...have 10 seconds before Mouse Wiggler begins.')

# replay setup
replay = 'Y'
while replay == 'Y':

	# sets up second counter
	iteration = 0

	# user input for length of program run in minutes
	runtime = input('\nRun mouse wiggle for how many minutes?\n\n')

	# enforces numbers only with digit check and while loop
	numcheck = runtime.isdigit()
	while numcheck == False:
		runtime = input('\nINVALID RESPONSE\nRun mouse wiggle for how many minutes?\n\n')
		numcheck = runtime.isdigit()

	# takes minutes and multiplies by 4 as program runs in 15 second chunks
	runtimeINT = int(runtime)
	actualrun = runtimeINT * 4

	# 5 second prewiggle warning and countdown
	print('\nStarting in...')
	x = 11
	while x != 1:
		x = x-1
		print(x)
		time.sleep(1)
	print('\nProgram started\n')

	# engine of the program
	for i in range(actualrun):
		# sleeper until next run in seconds
		time.sleep(15)
		# for double zero move checker
		doublezero = False
		# iteration counter in seconds
		iteration = iteration + 15
		# creates random numbers to move by
		randx = random.randint(-4,4)
		randy = random.randint(-4,4)
		# double zero checker to protect against timeout
		if randx == 0 and randy == 0:
			doublezero = 'double zero avoided'
			pyautogui.moveRel(-1, -1, duration=0.25)
			pyautogui.moveRel(1, 1, duration=0.25)
		# mouse mover	
		pyautogui.moveRel(randx, randy, duration=0.25)
		# print messages
		if doublezero == False:
			print(f'{iteration} seconds   {randx}, {randy}')
		else:
			print(f'{iteration} seconds   {randx}, {randy}, {doublezero}')

# replay checker
replay = input('Program over.\nRun again?  Y/N:   ').upper()
while replay not in ('Y', 'N'):
	replay = input('INVALID RESPONSE\nRun again?  Y/N:   ').upper()