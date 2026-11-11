from product import Product  # product 모듈로부터 Product 클래스 가져와 사용

class Cart:
    # 인스턴스화될 때 장바구니 생성
    def __init__(self):
        self.items = {} # 딕셔너리 형식으로 상품 담기 {상품:수량}, # 속성값이 딕셔너리일 수도 있으!
        # 내가 한 것처럼 인스턴스.qty 속성이 아니라 카트 딕셔너리 키값으로!!! 사실 이게 맞지ㅠ

    # 장바구니에 상품 추가
    def add(self, product, qty):
        # 품절 상품은 담을 수 없다
        if product.is_sold_out(): # ()빼먹지 말자 제발
            print("품절된 상품입니다.")
            return  # return 뒤에 아무것도 안써도 되는ㄱ거였나..?
        
        # 이미 장바구니에 담겨있는 수량 확인
        in_cart_qty = self.items.get(product, 0)
        
        # 더 담을 수 있는 수량 확인
        extra_qty = product.stock - in_cart_qty
        if qty > extra_qty:
            print(f"재고가 부족합니다. (담을 수 있는 수량 : {extra_qty})")
            return

        # 추가
        # 딕셔너리 key값이 있는지 확인할 수 있는 get 메서드 활용!!
        # get - 상품 추가한 적없어서 키값 못찾아도 에러나지 x 없으면 우선 qty 기본 0으로 항목 만들고 +qty
        # 기존에 추가한 상품은 get했을때 기존 qty가 뜨고 다시 추가 수량 +qty 
        self.items[product] = self.items.get(product, 0) + qty
        print(f"{product.name} {qty}개를 담았습니다.")

    # 장바구니에서 상품 제거
    def remove(self, product, qty):
        # 기존에 없는 상품은 뺄 수 없다
        if product not in self.items: # self.items는 딕셔너리 자료형, not in쓰면 그 키가 없다면
            print("장바구니에 해당 상품이 없습니다.")
            return

        # 담은 수량 이상 뺴면 상품을 통째로 삭제
        if qty >= self.items[product]: # self.items[product] = product 객체가 키인 qty 수량값
            del self.items[product] # remove랑 뭐가 달라??
            print(f"{product.name}을 장바구니에서 모두 뺐습니다.")

        else: # 여기서는 왜 else? 위에서 그냥 return 하면 안됨??
            self.items[product] -= qty
            print(f"{product.name} {qty}개를 뺐습니다.")

    # 장바구니 비었는지 확인
    def is_empty(self):
        return len(self.items) == 0

    # 상품 합계 계산
    def subtotal(self):
        return sum(p.price * q for p, q in self.items.items()) # ⭐⭐⭐ 이런 구문!!! 학습!!!

    # 배송비 계산
    def shipping(self):
        if self.is_empty(): return 0 # 장바구니 비어있으면 배송비 0
        return 0 if self.subtotal() >=30_000 else 3_000 # ⭐⭐⭐

    # 결제 금액 계산
    def total(self):
        return self.subtotal() + self.shipping()

    # 장바구니 내용 출력
    def show(self):
        line = "-" * 40 # 줄 긋기를 line 변수롤 만들 수 있음
        print(line)

        if self.is_empty():
            print("장바구니 비어있습니다.")

        for p,q in self.items.items(): # p = product 객체
            # 제품명(왼쪽정렬)  x 수량 = 총 금액(세자리수 ,)
            print(f"{p.name:<10} x {q:<3} = {p.price*q:>,}원")

        print(line)
        print(f"{'상품 합계':<10} {self.subtotal():>15,}원") # 문자열 title 정렬
        print(f"{'배송비':<10} {self.shipping():>15,}원")
        print(f"{'결제 금액':<10} {self.total():>15,}원")
        print(line)

    #결제 후 재고 수정
    def checkout(self):
        if self.is_empty(): return # 장바구니 비어있는 경우 아무것도 x
        self.show() # 결제 영수증 역할

        # 재고 감소 처리
        for p,q in self.items.items(): #p = product, q= quantity, qty
            p.stock -= q

        # 장바구니 비우기
        self.items.clear() #clear로 딕셔너리 지우기 -> 딕셔너리 메서드

        # 결제 성공여부(여기서는 코드 생략) 확인 후
        print("결제가 완료되었습니다. 감사합니다.")

      
#----------------------------------------------------------------- 테스트 코드


tumbler = Product("텀블러", 15000, 10) # 제품 생성
earphone = Product("이어폰", 89000, 3) # 제품 생성

cart = Cart() # 카트 인스턴스 생성
cart.add(tumbler, 3)
cart.add(earphone, 2)
cart.checkout()

print(tumbler)
print(earphone)

# for p, q in cart.items.items(): # cart.items 속성(상품(객체):개수 딕셔너리)를 items로 키 밸류값 가지고 나와서 봄
#     # cart.items의 키값인 p가 어떻게 객체? 위에서 제품 생성한 tumbler 가 Product 클래스로 만든 객체임!!
#     print(f"{p.id} : {p.name} X {q}")

# print("남은 종류:", len(cart.items)) # len을 인스턴스 속성에도 쓸 수 있군!