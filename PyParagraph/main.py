import re

# Read and analyze text files in current directory
def paranalysis(filename):
    print(filename)
    file=open(filename,"r")
    paragraph=file.read()
    # delimit to find sentences
    sentences=re.split("(?<=[.!?]) +", paragraph)
    sentcount=len(sentences)
    wordcount=0
    lettcount=0
    punctuation = ".,:!'()-"
    # delimit to find words
    for sent in sentences:
        # remove punctatuation from a sentence and store separately
        sentclean=sent
        for p in punctuation:
            sentclean=sentclean.replace(p,"")
        words=sentclean.split()
        wordcount += len(words)
        # delimit to count letters
        for word in words:
            lettcount += len(word)

    avg_lett=lettcount/wordcount
    avg_sent=wordcount/sentcount
    print('Paragraph Analysis')
    print('-----------------')
    print(f'Approximate Word Count: {wordcount}')
    print(f'Approximate Sentence Count: {sentcount}')
    print(f'Average Letter Count: {avg_lett:.1f}')
    print(f'Average Sentence Length Count: {avg_sent:.1f}')


# Call function for text files in the directory
paranalysis('paragraph_1.txt')
print('\n')
paranalysis('paragraph_2.txt')
