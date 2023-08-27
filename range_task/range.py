class Range:
    def __init__(self, start, end):
        self.__start = start
        self.__end = end

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, start):
        self.__start = start

    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, end):
        self.__end = end

    def get_length(self):
        return self.__end - self.__start

    def is_inside(self, number):
        return self.__start <= number <= self.__end

    def get_intersections(self, other_range):
        if self.__end <= other_range.start or other_range.end <= self.__start:
            return None

        return Range(max(self.__start, other_range.start), min(self.__end, other_range.end))

    def get_unions(self, other_range):
        if self.__end < other_range.start or other_range.end < self.__start:
            return [Range(self.__start, self.__end), Range(other_range.start, other_range.end)]

        return [Range(min(self.__start, other_range.start), max(self.__end, other_range.end))]

    """Почему решение с созданием списка не подходящее? Оно выглядит более лаконично"""
    # def get_differences(self, other_range):
    #     result = []
    #
    #     if self.__start < other_range.start:
    #         result.append(Range(self.__start, min(self.__end, other_range.start)))
    #
    #     if self.__end > other_range.end:
    #         result.append(Range(max(self.__start, other_range.end), self.__end))
    #
    #     return result

    def get_differences(self, other_range):
        if self.__start < other_range.start and self.__end < other_range.end:
            return [Range(self.__start, min(self.__end, other_range.start))]

        if self.__end > other_range.end and self.__start > other_range.start:
            return [Range(max(self.__start, other_range.end), self.__end)]

        if self.__start < other_range.start and self.__end > other_range.end:
            return [Range(self.__start, min(self.__end, other_range.start)),
                    Range(max(self.__start, other_range.end), self.__end)]

        return []

    def __repr__(self):
        return f"({ self.__start }; {self.__end})"
