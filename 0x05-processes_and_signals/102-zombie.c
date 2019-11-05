#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
 * main - Entry point
 * Return: Nothing
 */

int main(void)
{
	int i;
	pid_t pid;

	pid = fork();

	for (i = 1; i <= 5; i++)
	{
		if (pid < 0)
		{
			perror("Unsuccesful to create child process");
			exit(1);
		}
		else if (pid == 0)
		{
			dprintf(1, "Zombie process created, PID:  %d\n", getpid());
			return(0);
		}
		else
			printf("Refers to the PPID");
	}
	to_infinity();
	return (0);
}

/**
 * to_infinity - "Infinte loop of sleeps"
 * Return: Nothing
 **/

int to_infinity(void)
{
	while (1)
		sleep (1);

	return (0);
}
