#!/bin/bash

set -e

API_URL="http://localhost:8000"

echo "1. Registering client and getting access token..."
ACCESS_TOKEN=$(curl -s -X POST "$API_URL/api-clients" \
  -H "Content-Type: application/json" \
  -d '{"clientName": "Alice", "clientEmail": "alice@example.com"}' | \
  python3 -c "import sys, json; print(json.load(sys.stdin)['accessToken'])")

echo "Access token: $ACCESS_TOKEN"
echo

echo "2. Listing books..."
curl -s "$API_URL/books" | jq
echo

echo "3. Getting book with ID 1..."
curl -s "$API_URL/books/1" | jq
echo

echo "4. Listing orders (should be empty)..."
curl -s -H "Authorization: Bearer $ACCESS_TOKEN" "$API_URL/orders" | jq
echo

echo "5. Creating an order..."
ORDER_RESPONSE=$(curl -s -X POST "$API_URL/orders" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -d '{"bookId": 1, "customerName": "Alice"}')
ORDER_ID=$(echo "$ORDER_RESPONSE" | python3 -c "import sys, json; print(json.load(sys.stdin)['id'])")
echo "Order created: $ORDER_RESPONSE"
echo

echo "6. Getting order by ID..."
curl -s -H "Authorization: Bearer $ACCESS_TOKEN" "$API_URL/orders/$ORDER_ID" | jq
echo

echo "7. Health check..."
curl -s "$API_URL/status" | jq
echo 