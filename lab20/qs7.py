paragraph = input("Enter a paragraph: ")

word_counts = {}
punctuation = ".,!?;:"

for word in paragraph.split(): # space split by default
  clean_word = word.strip(punctuation).lower()

  if clean_word:
    word_counts[clean_word] = word_counts.get(clean_word, 0) + 1

print("\nWord Frequencies (Alphabetical):")
for word, count in sorted(word_counts.items()):
  print(f"{word}: {count}")


if word_counts:
  max_count = max(word_counts.values())
  most_frequent = [
      word for word, count in word_counts.items() if count == max_count
  ]

  print(f"\nMost frequent word ({max_count} times): {', '.join(most_frequent)}")
