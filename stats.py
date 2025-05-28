def get_words(path_to_file):
        with open(path_to_file) as f:
                return f.read()

def character_count(book_text):
	character_dict = {}
	for character in book_text:
		character_dict[character] = character_dict.get(character, 0) + 1
	return character_dict

def character_stats(book_text):
    counts = character_count(book_text)

    # Convert to list of dicts
    stats_list = [{"character": char, "count": count} for char, count in counts.items()]

    # Use a regular function instead of lambda
    def sort_on_count(item):
        return item["count"]

    # Sort by count descending
    stats_list.sort(key=sort_on_count, reverse=True)

    return stats_list


def character_stats(book_text):
    counts = character_count(book_text)

    # Convert to list of dicts
    stats_list = [{"character": char, "count": count} for char, count in counts.items()]

    # Sort by count descending
    stats_list.sort(key=lambda x: x["count"], reverse=True)

    return stats_list
