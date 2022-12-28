# MiniShoppingServer

**POST:** localhost:`port`/api/user - dùng khi đăng nhập hoặc login
```
{
    "email": "a"
}
```
**Response:** 
```
{
    "message": "success",
    "data": {
        "balance": 0.0,
        "hash": "ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb"
    }
}
```

**GET:** localhost:`port`/api/product?type=category&query=haha - lấy sản phẩm theo category

**Response:** 
```
{
    "products": [
        1, 2, 3, 4, 5, ...
    ]
}
```

**GET:** localhost:`port`/api/product?type=search&query=voucher - lấy sản phẩm theo search

**Response:** 
```
{
    "products": [
        1, 2, 3, 4, 5, ...
    ]
}
```

**POST:** localhost:`port`/api/favorite - thêm sản phẩm yêu thích
```
{
    "hash": "3e23e8160039594a33894f6564e1b1348bbd7a0088d42c4acb73eeaed59c009d",
    "product": <product_id>
}
```

**Response:** 
```
{
    "message": "success"
}
```

**GET:** localhost:`port`>/api/favorite/`hash` - lấy sản phẩm yêu thích theo hash

**Response:** 
```
{
    "products": [
        1, 2, 3, 4, 5, ...
    ]
}
```

**GET:** localhost:`port`/api/voucher/HAHA - lấy discount theo code

**Response:** 
```
{
    "discount": 30.0
}
```
