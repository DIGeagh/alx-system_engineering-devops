#!/usr/bin/env ruby

# Check if the script is called with an argument
if ARGV.empty?
  puts "Usage: #{$0} <string>"
  exit 1
end

# Get the first argument passed to the script
input_string = ARGV[0]

# Define the regular expression to match the pattern
regex = /^\d{10}$/

# Use the `match` method of the regular expression to find the match in the input string
match_result = input_string.match(regex)

# Output the matched string (or an empty string if no match is found)
puts match_result ? match_result[0] : ""
