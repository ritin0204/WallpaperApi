#!/bin/bash

# Number of parallel requests
num_requests=4

# API endpoint URL
url="http://127.0.0.1:8000/api/wallpapers/goku/?limit=3/"

# Function to send the request
send_request() {
  response=$(curl -s -X GET "$url")
  echo "Response: $response"
}

# Loop to send parallel requests
for ((i=1; i<=num_requests; i++)); do
  send_request & echo "Request sent: $i"
done

# Wait for all requests to finish
wait
