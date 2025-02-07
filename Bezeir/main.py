from numpy import array


class Bezier:
    def __init__(self, *points: tuple[array]):
        self._points = list(points)

    @staticmethod
    def __bezier(fromPoints, partition: float):
        if len(fromPoints) == 2:
            return (fromPoints[1] - fromPoints[0]) * partition + fromPoints[0]
        else:
            newPoints = [
                (pointPair[1] - pointPair[0]) * partition + pointPair[0]
                for pointPair in zip(fromPoints, fromPoints[1:])
            ]

            return Bezier.__bezier(newPoints, partition)

    def __call__(self, count: int):
        for i in range(count + 1):
            yield self.__bezier(self._points, i / count)


bez = Bezier(array([1, 1]), array([2, 3]), array([-1, 9]), array([6, 10]))

print(list(map(lambda x: (float(x[0]), float(x[1])), bez(20))))
