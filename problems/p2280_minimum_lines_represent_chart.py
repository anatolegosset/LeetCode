class Solution(object):
    def minimumLines(self, stockPrices):
        """
        :type stockPrices: List[List[int]]
        :rtype: int
        """
        if len(stockPrices) == 1:
            return 0
        stockPrices.sort()
        x_prev, y_prev = stockPrices[1][0], stockPrices[1][1]
        dir_x_prev, dir_y_prev = x_prev - stockPrices[0][0], y_prev - stockPrices[0][1]
        nb_lines = 1
        for x_cur, y_cur in stockPrices[2:]:
            dir_x_cur, dir_y_cur = x_cur - x_prev, y_cur - y_prev
            if dir_x_cur * dir_y_prev != dir_x_prev * dir_y_cur:
                dir_x_prev, dir_y_prev = dir_x_cur, dir_y_cur
                nb_lines += 1
            x_prev, y_prev = x_cur, y_cur
        return nb_lines
