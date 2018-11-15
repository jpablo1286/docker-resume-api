# resume api

curl --header "Content-Type: application/json" \
  --header "X-Apikey: Token" \
  --request PUT \
  --data '{"name": "Juan Pablo Rivera Velasco", "currentPosition": "Site Reliability Engeneer", "summary": "My Summary"}' \
  http://localhost:8000/summary/
