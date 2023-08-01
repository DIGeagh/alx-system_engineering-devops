#!/usr/bin/env ruby

# Check if the script is called with an argument
if ARGV.empty?
  puts "Usage: #{$0} <string>"
  exit 1
end

# Get the first argument passed to the script
input_string = ARGV[0]

# Define the regular expression to match capital letters
regex = /[A-Z]/

# Use the `scan` method of the regular expression to find all matches in the input string
matches = input_string.scan(regex)

# Join the matched letters into a single string
result = matches.join('')

# Output the result
puts result
