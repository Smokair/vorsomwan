APIKEY="cisco|SCG7KxNDa1d93AV2mpd6uEkKZhCfE01gZt-uK65cBok"
BOOK=11111111
DELETE_URL="http://library.demo.local/api/v1/books/$BOOK"
echo $DELETE_URL
curl -X DELETE $DELETE_URL -H "accept: application/json" \
-H "X-API-KEY: $APIKEY" -H "Content-Type: applicatino/json"