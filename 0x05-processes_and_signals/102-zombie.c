#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
 * infinite_while - "Infinte loop of sleeps"
 * Return: 0
 **/

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Entry point
 * Return: Nothing
 */

int main(void)
{
	int i;
	pid_t pid;

	for (i = 1; i <= 5; i++)
	{
		pid = fork();
		if (pid < 0)
			fprintf(stderr, "Unsuccesful child creation process");
		if (pid == 0)
		{
			printf("Zombie process created, PID:  %d\n", getpid());
			return (0);
		}
	}
	infinite_while();
	return (0);
}
