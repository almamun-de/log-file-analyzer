import re

def analyze_log_file(log_file, search_pattern, output_file):
    """
    Analyzes a log file, searching for lines that match a given pattern.
    Outputs matching lines to a file and prints a summary of the results.
    
    :param log_file: Path to the log file to be analyzed.
    :param search_pattern: The pattern to search for in the log file.
    :param output_file: File to write the matching log entries to.
    """
    pattern = re.compile(search_pattern)
    match_count = 0

    with open(log_file, 'r') as file, open(output_file, 'w') as output:
        for line in file:
            if pattern.search(line):
                output.write(line)
                match_count += 1

    print(f"Found {match_count} occurrences of pattern '{search_pattern}' in {log_file}.")
    print(f"Matching entries have been written to {output_file}.")

if __name__ == "__main__":
    log_file_path = input("Enter the path to the log file: ")
    pattern = input("Enter the pattern to search for (e.g., ERROR, 404, etc.): ")
    output_file_path = input("Enter the path for the output file: ")

