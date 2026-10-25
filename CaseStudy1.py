"""E-commerce Product Sorting using Divide and Conquer (Merge Sort)."""
import argparse
from dataclasses import dataclass
from typing import Callable, List, TypeVar
T = TypeVar("T")

@dataclass
class Product:
    name: str
    price: float
    rating: float
    reviews: int
    def __str__(self):
        return f"{self.name:<24} | Price: ₹{self.price:>8.2f} | Rating: {self.rating:.1f}/5 | Reviews: {self.reviews}"

def merge_sort(items: List[T], key: Callable[[T], object], reverse: bool = False) -> List[T]:
    """Sort a copy of items with Merge Sort."""
    if len(items) <= 1:
        return items[:]
    mid = len(items) // 2
    left = merge_sort(items[:mid], key, reverse)
    right = merge_sort(items[mid:], key, reverse)
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        a, b = key(left[i]), key(right[j])
        take_left = a >= b if reverse else a <= b
        if take_left:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:]); result.extend(right[j:])
    return result

def sample_products():
    return [
        Product("Wireless Headphones", 2499, 4.4, 1250), Product("Smart Watch", 3999, 4.2, 870),
        Product("USB-C Charger", 799, 4.6, 2100), Product("Laptop Backpack", 1299, 4.3, 640),
        Product("Bluetooth Speaker", 1799, 4.5, 980), Product("Mechanical Keyboard", 3299, 4.7, 520),
        Product("Phone Case", 299, 4.1, 3100), Product("Webcam", 2199, 4.0, 430)]

def main():
    parser = argparse.ArgumentParser(description="Sort sample products using Merge Sort.")
    parser.add_argument("--by", choices=("price", "rating", "name"), default="price")
    parser.add_argument("--order", choices=("asc", "desc"), default="asc")
    args = parser.parse_args()
    key_funcs = {"price": lambda p: p.price, "rating": lambda p: p.rating, "name": lambda p: p.name.casefold()}
    products = merge_sort(sample_products(), key_funcs[args.by], args.order == "desc")
    print(f"E-COMMERCE PRODUCT SORTING — DIVIDE AND CONQUER\nSorted by: {args.by.title()} ({args.order})")
    print("-" * 92)
    for product in products: print(product)

if __name__ == "__main__": main()
