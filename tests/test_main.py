from src.main import add


def test_add_success_int():
    assert add(1, 2, 3) == 6


def test_add_success_float():
    assert add(1.5, 2.5, 3.0) == 7.0


def test_add_success_default_c():
    assert add(4, 5) == 9


def test_type_check_string():
    assert add("1", 2, 3) == -1


def test_type_check_none():
    assert add(None, 2, 3) == -1


def test_type_check_bool():
    # bool は Python では int のサブクラスだが、
    # この仕様で bool を数値として扱うなら 3、
    # 扱わないなら add 側で bool 除外ロジックを追加して -1 にする
    assert add(True, 1, 1) == 3


def test_boundary_lower_ok():
    assert add(0, 0, 0) == 0


def test_boundary_upper_ok():
    assert add(10, 10, 10) == 30


def test_boundary_a_below():
    assert add(-0.1, 1, 1) == -2


def test_boundary_b_above():
    assert add(1, 10.1, 1) == -2


def test_boundary_c_above():
    assert add(1, 1, 11) == -2
