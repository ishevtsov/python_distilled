from functools import reduce

nums = [1, 2, 3, 4, 5]

total = reduce(lambda x, y: x + y, nums)
print(f'Total: {total}')

product = reduce(lambda x, y: x * y, nums, 1)
print(f'Product: {product}')

pairs = reduce(lambda x, y: (x, y), nums, None)
print(f'Pairs: {pairs}')