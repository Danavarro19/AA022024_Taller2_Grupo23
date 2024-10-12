class Heap:
    heap = []

    def __init__(self, arr):
        n = len(arr)
        self.heap = arr

        for i in range(n//2, -1, -1):
            self.heapify(self.heap, n, i)

    def heapify(self, arr, n, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i] > arr[left]:
            smallest = left

        if right < n and arr[smallest] > arr[right]:
            smallest = right

        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            self.heapify(arr, n, smallest)

    def insert(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 0 and self.heap[(i-1)//2] > self.heap[i]:
            self.heap[i], self.heap[(i-1)//2] = self.heap[(i-1)//2], self.heap[i]
            i = (i-1)//2

    def sort(self):
        n = len(self.heap)
        result = self.heap.copy()
        for i in range(n-1, 0, -1):
            result[i], result[0] = result[0], result[i]
            self.heapify(result, i, 0)

        return result

