import subprocess
import sys

def execute_command(command):
    # Split the command into subprocess arguments
    command_args = command.split()

    # Check for IO redirection operators
    input_file = None
    output_file = None

    if '<' in command_args:
        input_index = command_args.index('<')
        input_file = command_args[input_index + 1]
        command_args = command_args[:input_index]
    if '>' in command_args:
        output_index = command_args.index('>')
        output_file = command_args[output_index + 1]
        command_args = command_args[:output_index]

    try:
        # Execute the command
        if input_file:
            with open(input_file, 'r') as f:
                result = subprocess.run(command_args, stdin=f, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            result = subprocess.run(command_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # If output redirection is specified, write the output to the file
        if output_file:
            with open(output_file, 'w') as f:
                f.write(result.stdout.decode())
        else:
            # Print the command output to the console
            print(result.stdout.decode())
        
        # Print error output if there's an error
        if result.stderr:
            print(result.stderr.decode(), file=sys.stderr)

    except FileNotFoundError:
        print("Command not found")

def main():
    while True:
        # Get user input
        user_input = input("$ ")

        # Exit shell if user enters 'exit'
        if user_input == 'exit':
            break

        # Execute the command
        execute_command(user_input)

if __name__ == "__main__":
    main()