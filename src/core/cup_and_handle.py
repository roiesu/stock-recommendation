from decimal import Decimal
from typing import List

def detect_cup_and_handle(prices: List[Decimal], tolerance: float = 0.03) -> bool:
    if len(prices) < 10:
        return False  # Not enough data

    # 1. Find the lowest point (cup bottom)
    min_idx = prices.index(min(prices))

    if min_idx == 0 or min_idx == len(prices) - 1:
        return False  # Cup cannot start or end with the lowest point

    # 2. Identify the left and right peaks
    left_peak = max(prices[:min_idx])
    right_peak = max(prices[min_idx+1:])

    # 3. Compare peaks: must be similar within tolerance
    peak_diff = abs(left_peak - right_peak) / left_peak
    if peak_diff > Decimal(str(tolerance)):
        return False

    # 4. Ensure there's a real cup shape
    cup_depth = left_peak - prices[min_idx]
    if cup_depth < left_peak * Decimal("0.05"):  # cup must dip at least 5%
        return False

    # 5. Handle check: shallow pullback after right peak
    right_peak_idx = prices[min_idx+1:].index(right_peak) + min_idx + 1
    if right_peak_idx >= len(prices) - 2:
        return False

    handle_prices = prices[right_peak_idx+1:]
    handle_bottom = min(handle_prices)
    handle_depth = right_peak - handle_bottom

    if handle_depth > cup_depth * Decimal("0.5"):
        return False

    return True
