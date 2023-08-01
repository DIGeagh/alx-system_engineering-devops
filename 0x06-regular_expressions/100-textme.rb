#!/usr/bin/env ruby

# Check if the script is called with an argument
if ARGV.empty?
  puts "Usage: #{$0} <log_file>"
  exit 1
end

# Get the first argument passed to the script (log file path)
log_file = ARGV[0]

# Define the regular expression to extract sender, receiver, and flags
regex = /\[from:(?<sender>[^\]]+)\] \[to:(?<receiver>[^\]]+)\] \[flags:(?<flags>[^\]]+)\]/

# Read the log file and extract the required information
File.open(log_file, 'r') do |file|
  file.each_line do |line|
    match_data = line.match(regex)
    if match_data
      sender = match_data[:sender]
      receiver = match_data[:receiver]
      flags = match_data[:flags]
      puts "#{sender},#{receiver},#{flags}"
    end
  end
end
