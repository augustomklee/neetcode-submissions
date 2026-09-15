class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
     s1Freq = {}
     for c in s1:
          if c in s1Freq:
               s1Freq[c] += 1
          else:
               s1Freq[c] = 1

     for d in s1Freq:
          print(f'{d}:{s1Freq}')
     # Sliding window s2
     for i in range(len(s2) - len(s1) + 1):
          freq = {}
          for c in s2[i:i + len(s1)]:
               if c in freq:
                    freq[c] += 1
               else:
                    freq[c] = 1
          for d in freq:
               print(f'{d}:{freq[d]}')
          if freq == s1Freq:
               return True
     return False