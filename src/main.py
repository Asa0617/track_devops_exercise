def add(a, b, c=0):
    # 型チェック（int または float のみ許可）
    if not all(isinstance(x, (int, float)) for x in (a, b, c)):
        return -1

    # 境界値チェック（0〜10 の範囲内）
    if not all(0 <= x <= 10 for x in (a, b, c)):
        return -2

    # 条件を満たす場合は合計を返す
    return a + b + c
