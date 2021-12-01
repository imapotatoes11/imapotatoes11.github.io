#https://edabit.com/challenge/76ibd8jZxvhAwDskb
def tallest_skyscraper(n):
    for i in range(len(n)):
        if 1 in n[i]:
            return abs(i-len(n))

print(tallest_skyscraper([
  [0, 0, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 0],
  [1, 1, 1, 1]
]))