from collections.abc import Iterable, Hashable, Iterator

from main.sorted_frozen_set_dtypes import SupportsRichComparisonT, SupportsRichComparison


class SortedFrozenSet:
    def __init__(self, items: Iterable[SupportsRichComparisonT] | None = None) -> None:
        self._items: list[SupportsRichComparisonT] = sorted(set(items)) if items is not None else []

    def __contains__(self, item: Hashable) -> bool:
        return item in self._items

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> Iterator[SupportsRichComparison]:
        return iter(self._items)
