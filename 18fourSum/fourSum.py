class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()        
        dictionary = {key:{*group} for key, group in itertools.groupby(sorted((_ for _ in itertools.product(range(len(nums)), repeat = 2) if operator.lt(*_)), key = lambda _: sum(map(nums.__getitem__, _))), lambda _: sum(map(nums.__getitem__, _)))}
        result = {frozenset(dictionary.get(key, ())):{*group} for key, group in itertools.groupby(sorted((_ for _ in itertools.product(range(len(nums)), repeat = 2) if operator.lt(*_) and _[0] != 0 and _[0] != 1), key = lambda _: target - sum(map(nums.__getitem__, _))), lambda _: target - sum(map(nums.__getitem__, _)))}
        result = {*map(lambda _: tuple(map(nums.__getitem__, _)), (tuple(itertools.chain(*_)) for _ in itertools.chain(*itertools.starmap(itertools.product, result.items())) if _[0][1] < _[1][0]))}
        return [[*_] for _ in result]
