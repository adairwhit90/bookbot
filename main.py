import sys
from stats import get_words, character_stats

def main():
	if len(sys.argv) <2:
		print("Usage: python3 main.py <path_to_book>")
		sys.ext(1)
	path_to_file = sys.argv[1]
	text = get_words(path_to_file)
	words = text.split()
	num_words = len(words)
	book_text_all = list(text.lower())
	book_text = [char for char in book_text_all if char.isalpha()]

	print(f"Found {num_words} total words")
	
	sorted_char_stats = character_stats(book_text)

	for stat in sorted_char_stats:
        	print(f"{stat['character']}: {stat['count']}")
main()
