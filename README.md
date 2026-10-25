# Case Study: E-commerce Product Sorting using Divide and Conquer

## Objective
Demonstrate sorting an e-commerce product catalogue by price, rating, or name using **Merge Sort**, a Divide and Conquer algorithm.

## Requirements
- Python 3.8 or newer
- No third-party packages

## Run
```bash
python ecommerce_sort.py
python ecommerce_sort.py --by price
python ecommerce_sort.py --by rating --order desc
python ecommerce_sort.py --by name --order desc
```
Edit `sample_products()` in the Python file to change the example catalogue.

## Algorithm: Divide and Conquer
1. **Divide:** Split the list into two halves.
2. **Conquer:** Recursively sort each half.
3. **Combine:** Merge the sorted halves into one sorted list.

The `--by` option chooses the field and `--order` chooses ascending or descending order.

## Complexity
For `n` products, Merge Sort takes **O(n log n)** time in best, average, and worst cases and uses **O(n)** auxiliary space.

## E-commerce use
Sorting helps customers compare prices and ratings or browse products alphabetically. A production system may additionally use database indexes, pagination, inventory, discounts, and tie-breaking rules.
