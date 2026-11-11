# 쿠폰 클래스


class Coupon:
    def __init__(self, name): # name = 쿠폰이름
        self.name = name

    # 할인금액 반환 메서드
    def discount_amount(self, total):
        return 0 # 부모 클래스에서는 할인값x 자식 클래스에서 오버라이딩


# 10% 할인 쿠폰
class PercentDiscount(Coupon):
    # 할인율과 최대 할인율 적용
    def __init__(self, rate=0.1, max_discount=5_000):
        super().__init__("10% 할인 쿠폰") #쿠폰 이름 넣기
        self.rate = rate
        self.max_discount = max_discount

    def discount_amount(self, total):
        pass # 할인율 받아오기
        # return 
    

# 정액 할인 쿠폰
class FixedDiscount(Coupon):
    def __init__(self, amount, min_total):
        super().__init__(f"{min_total}이상 {amount}원 할인 쿠폰") # 부모 클래스 단계 매개변수만 생각하고 넣기
        self.amount = amount
        self.min_total = min_total

    def discount_amount(self, total):
            pass # 할인율 받아오기
            # return