#!/usr/bin/env bash

# Function to extract information from log entries
extract_info() {
    # Regular expression to match the required fields
    local regex='\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]'
    [[ $1 =~ $regex ]] && echo "${BASH_REMATCH[1]},${BASH_REMATCH[2]},${BASH_REMATCH[3]}"
}

# Check if the script was given the correct number of arguments
if [[ $# -ne 1 ]]; then
    echo "Usage: $0 '<log entry>'"
    exit 1
fi

# Call the function with the provided log entry
extract_info "$1"
