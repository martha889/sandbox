import read_index
import text_processing
import math


def tf_idf_weight(term, document):  # Use the mapped document number
    try:
        # term_frequency -> document id -> count of term in that document
        tf = read_index.term_frequency[str(document)][term]
    except KeyError:  # If the document doesn't contain the term
        tf = 0

    return (math.log(1 + tf)) * math.log(read_index.document_number / read_index.document_frequency[term])


answer = 1

while answer:
    query = input("Enter your query: ")
    query_tokens_list = text_processing.text_processing(text_processing.tokenize(query))

    query_tokens_dict = {}  # Store count of terms; used in cosine similarity numerator term

    for token in query_tokens_list:
        if token not in query_tokens_dict:
            query_tokens_dict[token] = 1
        else:
            query_tokens_dict[token] += 1

    print("Term list:", query_tokens_list)

    best_match = 0
    best_document_number = -1

    output_list = []

    for i in range(read_index.document_number+1):
        weight = 0
        query_denominator = 0
        doc_denominator = 0

        for token in query_tokens_dict:
            query_weight = math.log(1+query_tokens_dict[token]) * math.log(read_index.document_number / read_index.document_frequency[token])
            doc_weight = tf_idf_weight(token, i)

            query_denominator += query_weight ** 2
            doc_denominator += doc_weight ** 2
            weight += query_weight * doc_weight  # cosine similarity numerator

        try:
            weight = weight / (math.sqrt(query_denominator) * math.sqrt(doc_denominator))
        except ZeroDivisionError:
            weight = 0

        if weight > best_match:
            output_list.append([weight, read_index.document_map[str(i)]])
            best_match = weight
            best_document_number = i

    output_list.reverse()  # Best match always appended to the end. So, reverse to get the top documents.

    try:
        print("Best Weight:", best_match, "Document Path:", read_index.document_map[str(best_document_number)])
        print()
        print("Top 5 documents", output_list[:5] if len(output_list) >= 5 else output_list)

    except Exception as e:
        print(e)

    answer = int(input("Continue? (1 for Yes, 0 for No): "))


