"""Time Conversation Read an integer value, which is the duration in seconds of a certain event in a factory,
and inform it expressed in hours:minutes:seconds.

Input
The input file contains an integer N.

Output
Print the read time in the input file (seconds) converted in hours:minutes:seconds like the following example.
"""

seconds = int(input())
miniutes = seconds // 60
seconds %= 60
hour = miniutes // 60
miniutes %= 60
print(f"{hour}:{miniutes}:{seconds}")
