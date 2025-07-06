#include <unistd.h>

// Very much over-documented but i want to be able to understand it later

int main() {
  char command[255]; // Create 255 byte long object "command"
  write(1, "# ", 2); // Print "# " to fd 1 (stdout)
  int count = read(0, command, 255); // Read up to 255 bytes (command) from fd 0(stdin)
  // /bin/ls\n -> /bin/ls\0 - convert read bytes to end with null terminator rather than newline
  command[count - 1] = 0; // Essentially just replace the end of that part of memory with a 0 instead of n
  execve(command, 0, 0); // Using 0s is a stupid idea, as it means no arguments or environment vars can be passed to the program. It does the job though
}
