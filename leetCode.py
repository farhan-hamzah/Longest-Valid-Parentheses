class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Menyimpan indeks, dimulai dengan -1 sebagai anchor
        max_len = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)  # Simpan indeks kurung buka
            else:
                stack.pop()  # Pop pasangan terakhir
                if not stack:
                    stack.append(i)  # Set anchor baru
                else:
                    max_len = max(max_len, i - stack[-1])  # Hitung panjang valid

        return max_len
