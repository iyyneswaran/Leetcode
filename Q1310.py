class Solution:
    def build_prefix_xor(self, arr: list[int], length: int) -> list[int]:
        prefix_xor = [0] * (length + 1)
        for i, num in enumerate(arr):
            prefix_xor[i + 1] = prefix_xor[i] ^ num

        return prefix_xor

    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        length = len(arr)
        prefix_xor = self.build_prefix_xor(arr, length)
        answer = [0] * len(queries)
        for i, query in enumerate(queries):
            l_ptr = query[0]
            r_ptr = query[1]
            answer[i] = prefix_xor[r_ptr + 1] ^ prefix_xor[l_ptr]

        return answer