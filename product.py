# 상품

class Product:

    next_id = 1 # 클래스 변수

    # 새 상품의 초기 정보 저장
    def __init__(self, name, price, stock):
        self.id = Product.next_id
        Product.next_id += 1 # 다음 상품번호 1씩 증가
        self.name = name
        self.price = price
        self.stock = stock

    def is_sold_out(self):  # 불리언 타입 변수 앞에 관례적으로 is 씀(부정형 쓰지 않는다)
        return self.stock == 0

    def __str__(self):
        stock_text = "품절" if self.is_sold_out() else f"재고 {self.stock}개"
        return f"{self.id} {self.name:<10} {self.price:>8,} {stock_text}" # 테스트하면서 값 검증할 때 쓰기 좋음


#----------------------------tese code----------------------------------


if __name__ == "__main__":

    products = [
        Product("무선 이어폰", 80_000, 3), 
        Product("텀블러", 15_000, 10),
        Product("보조배터리", 32_000, 5),
        Product("마우스패드", 9_000, 0),
        Product("USB허브", 18_000, 4)
    ]

    for p in products:
        print(p)

