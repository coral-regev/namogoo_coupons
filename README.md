# Namogoo Home Assignment

### Requirements
Docker installed on your local machine

### Run the following from terminal:
`cd` into project directory (eg. `cd ~/Downloads/namogoo_coupons/namogoo`)

`docker-compose up`

### API Documentation
#### Get Coupon:
GET /coupons/GetCoupon/?domain=inerview.com&coupon_value=3 HTTP/1.1
Host: localhost:8000

`curl --location --request GET 'http://localhost:8000/coupons/GetCoupon/?domain=inerview.com&coupon_value=3'`

#### Return Coupon
POST /coupons/ReturnCoupon/ HTTP/1.1
Host: localhost:8000
Content-Type: application/json
Content-Length: 96

{"domain": "inerview.com", "coupon_value": 8, "coupons_list": ["itHEOENN2G2", "HCeAIln8fSdFkX"]}

`curl --location --request POST 'http://localhost:8000/coupons/ReturnCoupon/' \
--header 'Content-Type: application/json' \
--data-raw '{"domain": "inerview.com", "coupon_value": 8, "coupons_list": ["itHEOENN2G2", "HCeAIln8fSdFkX"]}'`
