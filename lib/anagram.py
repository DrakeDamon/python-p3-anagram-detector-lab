class Anagram:
  def __init__(self, word):
    self.word = word 

  def match(self, word_list):
    matches = []  # Empty list to store matches
    sorted_self_word = sorted(self.word)  # Sort the initialized word

    for word in word_list:  # Loop through each word in word_list
        if sorted(word) == sorted_self_word:  # Check if the sorted word matches the sorted initialized word
            matches.append(word)  # If it matches, append to matches

    return matches  # Return the matches list after the loop completes
