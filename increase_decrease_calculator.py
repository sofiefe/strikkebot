# This will be the script for calculating increases and decreases in the round for a knitting project
# Based on https://hobbyhygge.com/nb/strikkekalkulator

# This script will have some main functions:
# The first function takes two inputs; current amount of stiches, and wanted amount of stiches
# It will return the correct frequency to increase/decrease
# Second function wil print a step-by-step interactive guide to help keeping track of the decreases

# Some test-cases:
# Ex 1
# currentStiches = 200
# wantedStiches = 190
# Strikk 18 masker, så 2 sammen. Gjør dette 10 ganger.

# Ex 2
# currentStiches = 190
# wantedStiches = 200
# Strikk 19 masker, øk med 1 maske. Gjør dette 10 ganger.

# Ex 3
# currentStiches = 300
# wantedStiches = 321
# Du vil øke 21 masker. Dette må gjøres:

# Strikk 14 masker, øk med 1 maske. × 15
# Strikk 15 masker, øk med 1 maske. × 6
# Følg stegene under for å få det helt jevnt.

# Gjør disse stegene 3 ganger:
# Strikk 14 masker, øk med 1 maske. Gjør dette 2 ganger.
# Strikk 15 masker, øk med 1 maske.
# Strikk 14 masker, øk med 1 maske.
# Gjør disse stegene 3 ganger:
# Strikk 14 masker, øk med 1 maske. Gjør dette 2 ganger.
# Strikk 15 masker, øk med 1 maske.
# Strikk 14 masker, øk med 1 maske. Gjør dette 2 ganger.

# Ex 4
# currentStiches = 300
# wantedStiches = 321
# Du vil felle 21 masker. Dette må gjøres:

# Strikk 13 masker, så 2 sammen. × 15
# Strikk 14 masker, så 2 sammen. × 6
# Følg stegene under for å få det helt jevnt.

# Gjør disse stegene 3 ganger:
# Strikk 13 masker, så 2 sammen. Gjør dette 2 ganger.
# Strikk 14 masker, så 2 sammen.
# Strikk 13 masker, så 2 sammen.
# Gjør disse stegene 3 ganger:
# Strikk 13 masker, så 2 sammen. Gjør dette 2 ganger.
# Strikk 14 masker, så 2 sammen.
# Strikk 13 masker, så 2 sammen. Gjør dette 2 ganger.

