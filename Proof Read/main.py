# You've just finished writing the last chapter for your novel when a virus suddenly infects
# your document. It has swapped the 'i's and 'e's in 'ei' words and capitalised random letters.
# Write a function which will:

# Remove the spelling errors in 'ei' words. (Examples of 'ei' words: their, caffeine, deceive, weight)

# Only capitalise the first letter of each sentence.
# Make sure the rest of the sentence is in lower case.
# Each sentence is separated by a full stop.

# He haD iEght ShOTs of CAffIEne. --> He had eight shots of caffeine.

def proofread(st):
    st = st.lower()
    st = st.replace("ie", "ei")
    stlist = st.split(". ")
    stlist = [item.capitalize() for item in stlist]
    st = ". ".join(stlist)
    return st
