from collections import Counter


class ReconsturctDigits(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        # The count of each char in each number string.
        cnts = [
            Counter(_)
            for _ in [
                "zero",
                "one",
                "two",
                "three",
                "four",
                "five",
                "six",
                "seven",
                "eight",
                "nine",
            ]
        ]
        # The order for greedy method.
        order = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
        # The unique char in the order.
        unique_chars = ["z", "o", "w", "t","u", "f", "x","s", "g","n"]
        cnt = Counter(list(s))
        res = []
        for i in order:
            while cnt[unique_chars[i]]> 0:
                val_sub = cnts[i]
                cnt -= val_sub
                res.append(i)
        res.sort()
        return "".join(map(str, res))


if __name__ == "__main__":
    s = "wozneoer"
    print(ReconsturctDigits().originalDigits(s))