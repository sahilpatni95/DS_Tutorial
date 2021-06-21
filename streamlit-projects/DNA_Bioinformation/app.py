# Import libraries

import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

# Page Title
image = Image.open('dna-logo.jpg')
st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count Web App
This app counts the nucleotide composition of query DNA!
***
""")

# Input Text Box
st.sidebar.header('Enter DNA sequence')
#st.header('Enter DNA sequence')

sequence_input = "GAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\n" \
                 "ATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\n" \
                 "TGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.sidebar.text_area("Sequence input", sequence_input, height=250)
#sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:] # Skips the sequence name (first line)
sequence = ''.join(sequence) # Concatenates list to string



# Prints the input DNA sequence
st.header('DNA Query')
sequence

# DNA nucleotide count
st.header('DNA Nucleotide Count')

# Print dictionary
st.subheader('Print dictionary')
def DNA_nucleotide_count(seq):
  d = dict([
            ('A',seq.count('A')),
            ('T',seq.count('T')),
            ('G',seq.count('G')),
            ('C',seq.count('C'))
            ])
  return d

X = DNA_nucleotide_count(sequence)

#X_label = list(X)
#X_values = list(X.values())

X

# Print text
st.subheader('Print text')
st.write('There are  ' + str(X['A']) + ' adenine (A)')
st.write('There are  ' + str(X['T']) + ' thymine (T)')
st.write('There are  ' + str(X['G']) + ' guanine (G)')
st.write('There are  ' + str(X['C']) + ' cytosine (C)')

# Display DataFrame
st.header('Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

# Display Bar Chart using Altair
st.header('Display Bar chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80)  # controls width of bar.
)
st.write(p)