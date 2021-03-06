import read_index
import boolean_operators
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()

answer = 1

while answer:  # Infinite loop for entering query multiple times
    print()
    query = input("Enter your query (use '+', '*', '~' for OR, AND, NOT respectively): ").lower()
    query_tokenized = []

    start = 0
    i = 0

    while i < len(query):
        if query[i] == '*' or query[i] == '+':
            query_tokenized.append(query[start:i])
            query_tokenized.append(query[i])
            start = i + 1
        elif i == len(query) - 1:
            query_tokenized.append((query[start:]))
            break
        i += 1

    print("Recognized Tokens:", query_tokenized)  # Print the tokenized query (words and operators separated)

    try:
        result = boolean_operators.operator_not(read_index.postings_dict[query_tokenized[0]]) if query_tokenized[0][0] == '~' else read_index.postings_dict[query_tokenized[0]]
        operator = None

        for token in query_tokenized:
            if token == '*' or token == '+':
                operator = token
            else:
                if operator is None:
                    pass
                else:
                    if token[0] == '~':
                        if operator == '*':
                            result = boolean_operators.operator_and(result, boolean_operators.operator_not(read_index.postings_dict[token[1:]]))
                        elif operator == '+':
                            result = boolean_operators.operator_or(result, boolean_operators.operator_not(read_index.postings_dict[token[1:]]))
                    else:
                        if operator == '*':
                            result = boolean_operators.operator_and(result, read_index.postings_dict[token])
                        elif operator == '+':
                            result = boolean_operators.operator_or(result, read_index.postings_dict[token])

        print("Document numbers:", result, end='\n\n')
        result_names = []

        for doc_number in result:
            result_names.append(read_index.document_map[str(doc_number)])  # Append document names (or path)

        print("Document Names:", result_names)
        answer = int(input("Enter 1 to continue or enter 0 to quit: "))

    except KeyError as e:
        print("Not found:", e, end='\n\n')


