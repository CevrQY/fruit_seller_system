from typing import List


def solution(costs: List[int], N: int, shipping: int, X: int):
    assert shipping > 0
    assert X > 0

    total_cost = 0
    for i in range(N):
        assert costs[i] > 0
        total_cost += costs[i]

    if total_cost == 0:
        return 0
    if total_cost >= X:
        return total_cost
    else:
        return total_cost + shipping


if __name__ == "__main__":
    result = solution([10, 10, 10], 3, 20, 15)
    print(result)

    result = solution([10, 15, -30], 3, 16, 100)
    print(result)

    result = solution([10, 15, 30], 3, 27, 55)
    print(result)

    result = solution([], 0, 27, 55)
    print(result)
