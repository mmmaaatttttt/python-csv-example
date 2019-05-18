import csv


def count_rows(csv_file_path, phrase_to_match):
    """ Counts the number of rows in which phrase_to_match occurs,
    as well as the total number of times phrase_to_match appears.

    Example:
    >>> count_rows("sample.csv", "Matt")
    {'rows_with_word': 4, 'total_matches': 7}"""

    counts = {"rows_with_word": 0, "total_matches": 0}
    with open("sample.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:  # iterate through all the CSV rows
            notes = row[2]  # notes are in the third column
            if phrase_to_match in notes:
                # add one to the row count
                counts["rows_with_word"] += 1
                # count the number of additional phrase matches
                counts["total_matches"] += notes.count(phrase_to_match)

    return counts


print(count_rows("sample.csv", "Matt"))
# should display {'total_matches': 7, 'rows_with_word': 4}