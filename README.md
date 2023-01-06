# MiniShoppingServer

**POST:** localhost:`port`/api/user - dùng khi đăng kí hoặc đăng nhập
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
    "product": <product_id>,
    "action": "add"/"remove"
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
    "discount": 30.0,
    "quantity": 1
}
```

**GET:** localhost:`port`/api/database - download database

**POST:** localhost:`port`/api/location - thêm/update địa chỉ người dùng 
```
{
    "email": "a",
    "location": {
        "lat": 0.0,
        "lng": 0.0
    }
}
```

**Response:** 
```
{
    "message": "success"
}
```

**GET:** localhost:`port`/api/location/`hash` - lấy địa chỉ người dùng theo hash

**Response:** 
```
{
    "location": {
        "lat": 0.0,
        "lng": 0.0
    }
}
```

**POST:** localhost:`port`/api/purchase - thanh toán
```
{
    "hash": "3e23e8160039594a33894f6564e1b1348bbd7a0088d42c4acb73eeaed59c009d",
    "products": [
        {
            "id": 1,
            "quantity": 1
        },
        {
            "id": 2,
            "quantity": 2
        }
    ],
    "voucher": "HAHA"
}
```

**Response:** 
```
{
    "balance": 0.0,
}
```