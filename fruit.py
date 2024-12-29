from typing import Dict


class Fruit:
    def __init__(self, name, price, unit=2, discount=1.0):
        self.name: str = name                                   # 水果名
        self.price: float = price                               # 水果单价
        self.unit: int = unit                                   # 计量单位
        self.discount: float = discount                         # 水果折扣
        self.count: Dict[str, int] = {'good': 0, 'bad': 0}      # 水果数量

    def update_count(self, good_count, bad_count):
        self.count['good'] += good_count
        self.count['bad'] += bad_count

    def reset(self):
        self.count = {'good': 0, 'bad': 0}

    def get_price(self, weight=1.0, count=0):
        """计算水果价格，返回折后价格、减价金额"""
        if self.unit in [0, 1]:
            original_cost = weight * self.price
        else:
            if self.unit != 2:
                self.unit = 2
                raise Warning('未知计量单位，已使用默认单位（元/个）')
            original_cost = count * self.price

        after_discount = original_cost * self.discount
        return after_discount, original_cost - after_discount
