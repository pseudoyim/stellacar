'''
Allows user to input (via CLI) a series of commands to have the car execute when run.
'''
from wheels import wheel


def commands():

	series = []
	series_for_wheels_to_execute = []

	counter = 1

	accepting_commands = True

	while accepting_commands:

		print ''
		print '----------------------------Command # {}--------------------------'.format(counter)

		direction = raw_input('Enter direction [(F)orward, (B)ackward, (L)eft-pivot, (R)ight-pivot]: ').lower()

		time = raw_input('Enter duration in seconds: ')

		pair = (direction, time)

		series.append(pair)

		print 'Current list of commands to execute: ', series

		print '------------------------------------------------------------------'

		done = raw_input('Do you want to enter another command? [(Y)es, (N)o]').lower()

		if done == 'y':
			counter += 1
			continue

		elif done == 'n':
			accepting_commands = False

			print 'Here are the commands you\'ve asked me to perform: ', series

		# Translate series for wheel function.
		for pair in series:
			translated_pair = translate_commands_to_wheel(pair)
			series_for_wheels_to_execute.append(translated_pair)

		# Execute translated commands.
		for each in series_for_wheels_to_execute:
			wheel(each[0], each[1])

		print 'All done!'



def translate_commands_to_wheel(pair):

	if pair[0] == 'f':
		wheels_dir = ('lf','rf')

	elif pair[0] == 'b':
		wheels_dir = ('lr','rr')

	elif pair[0] == 'r':
		wheels_dir = ('lf', 'rr')

	elif pair[0] == 'l':
		wheels_dir = ('lr', 'rf')

	# Return the tuble of (wheels & dirs) and the duration.
	return wheels_dir, pair[1]



if __name__ == '__main__':
	
	print ''
	print '****************************** Hi, Stella! *****************************'
	print 'Please enter the list of commands you would like me to perform.'

	commands()