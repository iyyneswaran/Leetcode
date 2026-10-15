class Solution:
    def build_diff_arr(self, bookings: list[list[int]], n: int) -> list[int]:
        diff_arr = [0] * (n + 2)
        for first, last, seats in bookings:
            diff_arr[first] += seats
            diff_arr[last + 1] -= seats

        return diff_arr

    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        diff_arr = self.build_diff_arr(bookings, n)
        total_seats = 0
        answer = []
        for i in range(1, n + 1):
            total_seats += diff_arr[i]
            answer.append(total_seats)

        return answer