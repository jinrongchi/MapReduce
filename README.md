# MapReduce
 Simple MapReduce working with Hadoop

## Part 1: 
- Input: Only one MR job for this part, the input is at least one document. By simple using command python mapper.py |sort| python reducer.py, mapper.py will automatically read all the files in ‘inputDirectory/’ directory.
- Output: The output will be the list of pairs, ((term, document identity), count), which states the frequency of a term in each document.

## Part 2:
- Input: Only one MR job for this part, the input is at least one document. 
- Output: The output will be the list of pairs, ((term1 term2), count), where (term1 term2) is a bigram. This counts the frequency of bigrams across the documents.

## Part 3:
- Input: Only one MR job for this part, the input is at least one document. 
- Output: The output will be an integer that represents the number of bigrams which only present in single document.

## Part 4:
( python mapper1.py |sort| python reducer1.py && python mapper2.py |sort| python reducer2.py ) | python mapper3.py |sort| python reducer3.py 
- MR1: Computing Term Frequency (TF)
  - Input: At least one document. 
  - Output: document identity, token TF
- MR2: Computing Inverse Document Frequency (IDF)
  - Input: At least one document. 
  - Output: document identity, token IDF
- MR3: Computing TF-IDF
  - Input: Output of MR1 and MR2
  - Output: (document identity, token), TF, IDF, TF-IDF)
