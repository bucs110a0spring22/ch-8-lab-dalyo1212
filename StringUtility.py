class StringUtility:
  def __init__(self, string):
    self.string = string
    
  def __str__(self):
    return self.string

  def vowels(self):
    count = 0
    for char in self.string:
      if char.lower() in "aeiou":
        count +=1
    if count >= 5:
      return "many"
    return count

    
  def bothEnds(self):
    word = "Hello"
    first_two_letters = word[:2]
    reverse = word[-2:]
    print(first_two_letters, reverse)
    if len(self.string) <= 2:
      return ''
    
  def fixStart(self):
    if len(self.string) <= 1:
      return self.string
    else:
      new_word = self.string[0] + self.string[1:].replace(self.string[0], "*")
    return new_word
  
  
  def asciiSum(self):
    sum = 0
    for i in self.string:
      sum + ord(i)
    return sum
  
  def cipher(self):
    if not self.string:
      return ''

