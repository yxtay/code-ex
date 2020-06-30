import pytest

from src.roads_and_libraries import roads_and_libraries, roads_and_libraries_ds

cases = [
    (3, 2, 1, [[1, 2], [3, 1], [2, 3]], 4),
    (6, 2, 5, [[1, 3], [3, 4], [2, 4], [1, 2], [2, 3], [5, 6]], 12),
]


@pytest.mark.parametrize("n, c_lib, c_road, cities, expected", cases)
def test_roads_and_libraries(n, c_lib, c_road, cities, expected):
    result = roads_and_libraries(n, c_lib, c_road, cities)
    assert result == expected


@pytest.mark.parametrize("n, c_lib, c_road, cities, expected", cases)
def test_roads_and_libraries_ds(n, c_lib, c_road, cities, expected):
    result = roads_and_libraries_ds(n, c_lib, c_road, cities)
    assert result == expected
