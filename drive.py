'''
Allows user to input (via CLI) a series of commands to have the car execute when run.
'''
import stellacar


def commands():

	series = []

	counter = 1

	accepting_commands = True

	while accepting_commands:

		print ''
		print '----------------------------Command # {}--------------------------'.format(counter)

		direction = raw_input('Enter direction [(F)orward, (B)ackward, (L)eft, (R)ight]: ').lower()

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

			print series
			return series


if __name__ == '__main__':
	
	print ''
	print '****************************** Hi, Stella! *****************************'
	print ''

	commands()