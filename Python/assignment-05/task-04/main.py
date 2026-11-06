import shop_package.discount as disc
from shop_package.billing import calculate_total
import shop_package.billing as bill

print(disc.apply_discount(1000, 10))
print(disc.flat_discount(500))
print(calculate_total([100, 200, 300]))
print(bill.apply_tax(600))