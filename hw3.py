def get_fixed_price(price, n):
    sale=100-price
    money=n*100/sale
    return int(money)

sale=int(input("할인율은? "))
A=int(input("A상품의 할인된 가격은? "))
B=int(input("Bx상품의 할인된 가격은? "))
print("A상품의 정가는", get_fixed_price(sale, A), "원")
print("B상품의 정가는", get_fixed_price(sale, B), "원")