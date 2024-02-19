def authorFreq(books_authors):
    author_count = {}
    for book, author in books_authors.items():
        if author in author_count:
            author_count[author] += 1
        else:
            author_count[author] = 1
    return author_count

# Example usage:
books_authors = {"book1": "James", "book2": "Ellie", "book3": "Samantha", "book4": "James","book5": "James", "book6": "Ellie", "book7": "Samantha", "book8": "James"}
result = authorFreq(books_authors)
print(result)  # Output will be {"James": 2, "Ellie": 1, "Samantha": 1}



def authorFreq(books_authors):
    author_count = {}
    for author in books_authors.values():
        if author in author_count:
            author_count[author] += 1
        else:
            author_count[author] = 1
    return author_count

# Example usage:
books_authors = {"book9": "James", "book10": "Ellie", "book11": "Samantha", "book12": "James"}
result = authorFreq(books_authors)
print(result)  # Output will be {"James": 2, "Ellie": 1, "Samantha": 1}
