# Introductory Python Project: 
Data Structures, File I/O, String Processing

### Background
I made this project in Languages and Computation with 
Professor EricLarson at Seattle University.

#### Functions
1. **countPairs**
    - Recieves the name of the input file (string).
    - Reads the file and returns a dictionary that 
    has 2-letter pairs as keys and the frequencies as 
    values.
    - Assumes the input file exists and contains at 
    least one pair.
    - The pairs are not case-sensitive, but are stored
    in the dictionary in lowercase.
    - Anything that is not a letter is considered a 
    delimiter.
    - Ex: "E-mail r2d2 @ seattleu.edu"'s dictionary 
    would be 
    
    {'ma' : 1, 'ai' : 1, 'il' : 1, 'se' : 1, 'ea' : 1,
    'at' : 1, 'tt' : 1, 'tl' : 1, 'le' : 1, 'eu' : 1,
    'ed' : 1, 'du' : 1}

2. **getTopFivePairs**
    - Recieves dictionary returned from **countPairs**.
    - Creates and returns a list of tuples where the 
    first entry in the tuple is a 2-letter string and 
    the second is an integer.
    - The list contains the top 5 most frequent pairs 
    in order from most frequent to least frequent. 
    - If there is a tie, all pairs of that frequency 
    will be placed in alphabetical order.
    - If there are fewer than 5 pairs, the appropiate
    list will simply be returned.
    - Therefore, the list has the potential to be a 
    length of fewer and greater than 5.

3. **createFollowsDict**
    - Recieves dictionary returned from **countPairs** 
    and a single character.
    - Creates and returns a dictionary that has each 
    letter of the alphabet as a key and the frequency 
    of how often that letter follows the given 
    character.
    - If a letter never follows the given letter, a 
    dictionary entry of 0 will be present.

#### Other
- The driver uses list comprehension on a dictionary.
- Comments are present in the code for further technical
understanding.
