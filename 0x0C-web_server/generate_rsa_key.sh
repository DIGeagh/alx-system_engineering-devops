#!/bin/bash

# Check if the user provided an argument for the key file name
if [ $# -eq 0 ]; then
  echo "Usage: $0 <key_filename>"
  exit 1
fi

# Get the key file name from the command line argument
key_filename="$1"

# Check if the key file already exists
if [ -f "$key_filename" ]; then
  echo "Key file '$key_filename' already exists. Please choose a different name."
  exit 1
fi

# Generate the RSA key pair (2048 bits is a common choice, but you can adjust it)
ssh-keygen -t rsa -b 2048 -f "$key_filename"

# Check if the key generation was successful
if [ $? -eq 0 ]; then
  echo "RSA key pair successfully created."
else
  echo "Error generating RSA key pair."
fi
