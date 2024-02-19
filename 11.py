def authorFreq(books_authors):
    author_count = {}
    for author in books_authors.values():
        if author in author_count:
            author_count[author] += 1
        else:
            author_count[author] = 1
    return author_count




def prolificAuthors(books_authors):
    author_count = authorFreq(books_authors)
    max_books_written = max(author_count.values())
    prolific_authors = [author for author, count in author_count.items() if count == max_books_written]
    return prolific_authors

# Example usage:
books_authors = {"book1": "James", "book2": "Ellie", "book3": "Samantha", "book4": "James", "book5": "James"}
result = prolificAuthors(books_authors)
print(result)  # Output will be ["James"]
