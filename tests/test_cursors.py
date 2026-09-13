from src import discover


def test_advance_circular_wraps():
    st: dict = {"cursors": {}}
    discover._advance_circular(st, "k", 8, 5, 10)
    assert st["cursors"]["k"] == 3
    discover._advance_circular(st, "k2", 0, 0, 0)
    assert st["cursors"]["k2"] == 0


def test_next_rotation_bounded():
    st: dict = {"cursors": {"osm_idx": 25}}
    cur = discover._next_rotation(st, "osm_idx", 10)
    assert cur == 5
    assert st["cursors"]["osm_idx"] == 6
    # Next call advances by one, still bounded.
    cur2 = discover._next_rotation(st, "osm_idx", 10)
    assert cur2 == 6
    assert st["cursors"]["osm_idx"] == 7
