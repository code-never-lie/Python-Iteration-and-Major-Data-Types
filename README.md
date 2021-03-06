# Python-Iteration-and-Major-Data-Types
Program 1
Iteration and Major Data Types:
List, Tuple, Set, and Dict (and Open for files)
ICS-33: Intermediate Programming
Introduction	This programming assignment is designed to ensure that you know how to use combinations of Python's most important data types to model and compactly write/debug code that solves a wide variety of different programming problems. The kind of abstract thinking that goes into modeling solutions to these programming problems with these data types (and iteration over them) is critical to your development as computer scientists.
There are five parts to this assignment. In each you will be asked to write a module that contains a few functions and a script at the bottom, which ties these functions together to solve the problem.

You should download the program1 project folder and use it to create an Eclipse project. The project folder contains files for all the modules in which to write your functions and scripts; it also contains all the data files that you need to test/debug your modules; finally, it contains all the batch self-check files I will use when grading your programs. In your modules, you may import additional standard/courselib modules and you may write additional helper functions.

I recommend that you work on this assignment in pairs, and I recommend that you work with someone in your lab section (so that you have 4 hours each week of scheduled time together). These are just recommendations. Try to find someone who lives near you, with similar programming skills, and work habits/schedule: e.g., talk about whether you prefer to work mornings, nights, or weekends; what kind of commitment you will make to submit programs early.

Only one student should submit all parts of the the assignment, but both students' UCInetID and name should appear in a comment at the top of each submitted .py file. A special grading program reads this information. The format is a comment starting with Submitter and Partner (when working with a partner), followed by a colon, followed by the student's UCInetID (in all lower-case), followed by the student's name in parentheses (last name, comma, first name -capitalized appropriately). If you omit this information, or do not follow this exact form, it will require extra work for us to grade your program, so we will deduct points.

For example if Romeo Montague (whose UCInetID is romeo1) submitted a program that he worked on with his partner Juliet Capulet (whose UCInetID is jcapulet) the comment at the top of each .py file would appear as:

# Submitter: romeo1(Montague, Romeo)
# Partner  : jcapulet(Capulet, Juliet)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming
If you do not know what the terms cooperatively and/or rules for pair programming mean, please read about Pair Programming before starting this assignment. Please turn in each program as you finish it, so that I can more accurately assess the progress of the class as a whole during this assignment.
Print this document and carefully read it, marking any parts that contain important detailed information that you find (for review before you turn in the files). The code you write should be as elegant and compact as possible, using appropriate Python idioms. You should familiarize yourselves with the safe_open function in the goody module and all the functions in the prompt module, both of which you should have installed in your courselib folder as part of the Eclipse/Python installation. Recall how to use the sep and end parameters in the print function. Currently Pythons f-strings offer the easiest way to format strings; know how to use them.

Reread the section on Time Management from Programming Assignment 0 before starting this assignment.

IMPORTANT 1: Before starting this assignment, download the xref project folder which contains a small Python script xref.py that produces a cross-reference of all the words (converted to lower case) in a file (where words appear with spaces between them: see xrefin.txt for an example): the words are listed in alphabetic order followed by a set (i.e., no duplicates) of the line numbers it appears on (listed in increasing numeric order). Before solving the problems in this programming assignment, ensure you understand all the details of how this program works: look at features and functions like safe_open, defaultdict (and how it is used), enumerate, rstrip and lower, split and join, sorted, lambda, for loops with two (unpacked) indexes, the two comprehensions (in the call to max and join), and f-strings. These are the building blocks for many parts of this assignment; explore and experiment with this code to understand how all the parts work together to achieve the desired result. Run this code on more complicated data files.

IMPORTANT 2: This assignment has 5 parts: pairs should work on each part together, not split them up and do them separately. Parts 1-3 are going to be worth 12 points each; parts 4-5 are to be worth 7 points each. This skewing of points towards the simpler parts means students finishing the first 3 parts correctly will yield a 72% average; those finishing the first 4 parts correctly will have an 86% average; but to get an A on this assignment requires solving all parts correctly. I strongly recommend finishing the first part by the weekend, and then finishing another part every few days.

In the past, many students waited until the last few days and then tried to write all their solutions: that is a recipe for learning little and getting a poor grade (or worse, cheating and getting caught; remember that I'm going to be running MOSS on all the parts of this assignment, checking for very similar solutions). So, now I am grading only 2 parts submitted on the day before the due date or later (and only 1 part submitted on the due date). You can submit as many parts as you want earlier than the day before the due date. That is if you submit all 5 parts on the day before the due date, I will grade only 2 parts; if you submit all parts on the due date I will grade only 1 part. If you submit all 5 parts two days before the due date, I will grade all 5 parts and you will get two extra credit points. In the worst case, to have me grade all parts, you must submit 3 parts two days before the due date, 1 part the day before the due date, and 1 part on the due date. So, start early on this assignment and submit your work well before the due date.

IMPORTANT 3: I will mostly grade all these programs automatically, using the batch self-check files provided in the download. Use the driver program (explored in Programming Assignment #0) to run the batch-self check files in this assignment; debug any errors that they produce. But the TAs (with some automated tools) will also look at/run the code in some of your scripts: so the scripts need to follow exactly what is shown in the Sample Interactions part for each problem, including the wording of all prompts and messages. Therefore, I suggest testing your code first to match the scripts; when those results are correct, test it using the batch self-check files. Finally, if a submitted Python module contains even one syntax error or bad import, it will fail all its batch self-checks; ensure that you submit modules with no syntax or bad import errors (Python sometimes adds strange imports at the top of your file; ensure that all your imports are used and are reasonable). See Announcement #5 for details.

Problem #1: Reachability	
Problem Summary:
Write the required functions and script that prompts the user for the name of a file representing a graph; reads the file (storing the graph in a dictionary); prints the graph/dictionary in a special form; repeatedly prompts the user for a starting node name (rejecting those that are not keys in the graph); computes and prints all the node names that are reachable from it by following zero or more edges in the graph (e.g., a node is reachable from itself).
Input and Output:
Read a file of pairs of node names (representing edges) in a directed graph, building a dictionary whose key is a str source node name and whose associated value is a set of str destination node names that are each reachable directly from the source node name key. We annotate this dictionary as {str:{str}}.
In the file, two nodes names appear on each line: first the source node name, then the destination node name, with these node names (which may be entire words, not just single characters) separated by one semicolon character. For example, the input file graph1.txt contains the following lines (which could appear in this order, or any other order, and still produce the same dictionary).

  c;f
  b;d
  a;c
  c;e
  d;g
  a;b
  e;d
  f;g
  f;d
which represent the graph


Print the graph, one source node name per line followed by the set of all the destination node names that the source can immediately reach. The graph above would print as

  Graph: str (one source node) -> [str] (sorted list of destination nodes)
    a -> ['b', 'c']
    b -> ['d']
    c -> ['e', 'f']
    d -> ['g']
    e -> ['d']
    f -> ['d', 'g']
Note that the source node names must be sorted alphabetically; the set of desintation node names associated with each source must appear in a list whose values are also sorted alphabetically: it makes no sense to talk about sorted sets. Note that because node g is not a source node (it is only a destination node), it does not appear first on any line (and appears only in the sets for source nodes d and f).

There are multiple data files for this program: graph1.txt (shown above), graph2.txt and graph3.txt; test/debug your program on the first file; when you are done, test it on the remaining files. Draw the graph represented by each file to ensure that your code correctly prints it and computes the node names reachable from any source node (which you can do by eyeballing the graphs: they are small).

Repeatedly prompt the user for a starting node name in the graph (until the user enters terminate) and compute and print all the node names that are reachable from it by following edges in the graph. Reject any node name that is not a key in the graph. An example interaction (processing the graph above) might be

  Specify one start node (or terminate): e
  From the start node e, reachable nodes = {'g', 'e', 'd'}

  Specify one start node (or terminate): x
    Entry Error: 'x';  Illegal: not a source node
    Please enter a legal String

  Specify one start node (or terminate): a
  From the start node a, reachable nodes = {'g', 'f', 'e', 'd', 'c', 'b', 'a'}

  Specify one start node (or terminate): terminate
Functions and Script:
Write the following functions and script. I am providing line counts for these function bodies not as requirements, but to indicate the lengths of well-written Pythonic code.
read_graph has an open (file) parameter; it returns the dictionary representing the graph (body is 5 lines).
graph_as_str has a dictionary parameter (representing the graph); it returns a multi-line string (each line is ended by '\n'), which when printed shows the contents of the graph in the appropriate textual form (body is 4 lines; can you do it in 1?).
reachable has a dictionary parameter (representing the graph), a str start node in the graph (technically a key in the dictionary), and a bool controling tracing (whose default value is False); it returns a set of all the nodes reachable from it by following edges in the graph. Hint: I used the get dictionary function, which allows a second argument that specifies what to do if the first argument (key) is not in the dictionary, because this function should not mutate the dictionary (body is 9 lines).
Write a script at the bottom of this module (in if __name__ == '__main__':) that prompts the user to enter the file storing the graph and start node (rejecting any string that is not a source node in the graph) or the word terminate; calls these functions with the entered information to solve the problem, and print the appropriate information: the graph and the set containing all the node labels (body is 9 lines).
Here is the basic algorithm for computing reachability; it is simple to explain and not (very) complicated to implement. But, you have to understand these instructions and carefully translate them into Python. You should hand-simulate this algorithm using the graph above, and verify that it produces the results you expect, before coding the algorithm in Python. You might be tempted to use recursion, but please don't: unless recursion is done very carefully, reachable will run forever on graphs that contain cycles: one of the input files is a graph that contains cycles.
To compute all the reachable nodes in a graph, create a set (initially empty) of reached nodes and a list (initially containing the parameter start node) of nodes that we are going to explore (to find nodes they can reach).
While the exploring list still has nodes, remove the first one (recall the pop method for lists) and put it into the reached set; for all its associated destination nodes that are not already in the reached set, put them in the exploring list.
When the exploring list becomes empty (can you argue that this always will happen -there is no infinite looping), return the reached set.
Read these instructions carefully, a few times. Hand simulate these instructions to ensure that you understand the reachability algorithm; use the data above, which is automatically traced in the example below. Do not attempt to write any Python code to solve this problem until you understand this algorithm and can apply it to the data specified above. Eventually you will write your Python code to produce such a trace conditionally.

Here is a trace (see the 3rd parameter to the reachable function described below, which activiates the trace) for graph specified above starting at the node a. The order of values in the sets are arbitrary; I have written these data structures on multiple lines for formating purposes.

  reached set    = set()
  exploring list = ['a']
  moving node a from the exploring list into the reached set
  after adding all nodes reachable directly from a but not already in reached, exploring = ['c', 'b'] 

  reached set    = {'a'}
  exploring list = ['c', 'b']
  moving node c from the exploring list into the reached set
  after adding all nodes reachable directly from c but not already in reached, exploring = ['b', 'f', 'e'] 

  reached set    = {'a', 'c'}
  exploring list = ['b', 'f', 'e']
  moving node b from the exploring list into the reached set
  after adding all nodes reachable directly from b but not already in reached, exploring = ['f', 'e', 'd'] 

  reached set    = {'a', 'c', 'b'}
  exploring list = ['f', 'e', 'd']
  moving node f from the exploring list into the reached set
  after adding all nodes reachable directly from f but not already in reached, exploring = ['e', 'd', 'g', 'd'] 

  reached set    = {'a', 'c', 'f', 'b'}
  exploring list = ['e', 'd', 'g', 'd']
  moving node e from the exploring list into the reached set
  after adding all nodes reachable directly from e but not already in reached, exploring = ['d', 'g', 'd', 'd'] 

  reached set    = {'f', 'b', 'a', 'c', 'e'}
  exploring list = ['d', 'g', 'd', 'd']
  moving node d from the exploring list into the reached set
  after adding all nodes reachable directly from d but not already in reached, exploring = ['g', 'd', 'd', 'g'] 

  reached set    = {'f', 'b', 'a', 'c', 'e', 'd'}
  exploring list = ['g', 'd', 'd', 'g']
  moving node g from the exploring list into the reached set
  after adding all nodes reachable directly from g but not already in reached, exploring = ['d', 'd', 'g'] 

  reached set    = {'f', 'b', 'a', 'g', 'c', 'e', 'd'}
  exploring list = ['d', 'd', 'g']
  moving node d from the exploring list into the reached set
  after adding all nodes reachable directly from d but not already in reached, exploring = ['d', 'g'] 

  reached set    = {'f', 'b', 'a', 'g', 'c', 'e', 'd'}
  exploring list = ['d', 'g']
  moving node d from the exploring list into the reached set
  after adding all nodes reachable directly from d but not already in reached, exploring = ['g'] 

  reached set    = {'f', 'b', 'a', 'g', 'c', 'e', 'd'}
  exploring list = ['g']
  moving node g from the exploring list into the reached set
  after adding all nodes reachable directly from g but not already in reached, exploring = []
Sample Interaction:
The program, as specified, will have the following interaction: user-typed information appears in italics. Your output should "match" this one (sets will match if they have the same contents, independent of their order). You should also check that it works for other starting nodes, and a variety of starting nodes in the other graphs.
  Specify the file name representing the graph: graph1.txt

  Graph: str (one source node) -> [str] (sorted list of destination nodes)
    a -> ['b', 'c']
    b -> ['d']
    c -> ['e', 'f']
    d -> ['g']
    e -> ['d']
    f -> ['d', 'g']

  Specify one start node (or terminate): e
  Specify choice for tracing algorithm[True]: False
  From the start node e, reachable nodes = {'g', 'e', 'd'}

  Specify one start node (or terminate): x
    Entry Error: 'x';  Illegal: not a source node
    Please enter a legal String

  Specify one start node (or terminate): a
  Specify choice for tracing algorithm[True]: False
  From the start node a, reachable nodes = {'g', 'f', 'e', 'd', 'c', 'b', 'a'}

  Specify one start node (or terminate): terminate
Note that if the user specified True for tracing the algorithm, the program would also print the kinds of information shown above in the example of tracing.
Problem #2: Stable Marriage	
Problem Summary:
Write the required functions and script that prompts the user for the names of two files: a file representing the marriage preferences of a sequence of men, and a file representing the marriage preferences of a sequence of women; reads these files (storing this information in special data structures: dictionaries storing preference as lists); prints the dictionary/preferences of the men and women in a special form; runs the Gale/Shapley algorithm for finding a stable marriage (tracing its progress, if required); prints the stable marriage as a set of man/woman tuples. Please excuse my use of heteronormative terms. The problem is easier to state and understand when it uses two disjoint sets, men and women, whose members match only others outside their sets.
Suppose that N men and N women want to match in a heterosexual marriage. Each produces a list of his/her preferences, ranking all members of the opposite gender in highest to lowest order of acceptability as a partner. The Gale/Shapley algorithm (described in detail below) matches men and women in stable marriages. Marriages are stable when we cannot find a man and woman, who prefer each other to their match. This scenario can be used to find stable matches in other contexts. For example, this algorithm is used when medical school graduates match with hospitals for their residencies: the students and institutions rank each other and then the algorithm is run, processing these rankings. In this case, the residents propose (act as the men in the description above) and the hospitals accept/reject the proposals (act as the women).

The fundamental data structure used throughout this process (as both arguments to functions and the results returned by functions) is characterized by {str:[str,[str]]}, which describes a dictionary whose keys are associated with 2-lists. The dictionary keys are the names of men/women (str). Each man/woman is associated with a 2-list, whose first index is the current match of that person (str), and whose second index is a list ranking other possible matches (list of str), from highest to lowest preference.

For example, the following dictionary represents information about three men participating in marriages (m1, m2, m3):

  {'m1': [None, ['w3', 'w2', 'w1']],
   'm2': [None, ['w3', 'w1', 'w2']],
   'm3': [None, ['w2', 'w1', 'w3']]}
Here, m1 is currently matched with no one (None) and ranks the women, in order of preference, as follows w3 (hightes ranking) followed by w2 followed by w1 (lowest ranking). The other lines in this dictionary are interpreted similarly. In this example (and the ones below) I have printed each key/value pair (alphabetically by key) on its own line; of course, if we print a dictionary in Python, it can print its key/value pairs in any order.
The following dictionary represents information about three women participating in marriages (w1, w2, and w3):

  {'w1': [None, ['m1', 'm2', 'm3']],
   'w2': [None, ['m2', 'm1', 'm3']],
   'w3': [None, ['m3', 'm2', 'm1']]}
Here, w2 is currently matched with no one (None) and ranks the men, in order of preference, as follows m2 (highest ranking) followed by m1 followed by m3 (lowest ranking).
After running the Gale/Shapley algorithm (with men proposing to women, and women accepting or rejecting their proposals: more on these details later), these dictionaries are mutated to

  {'m1': ['w2', ['w3', 'w2', 'w1']],
   'm2': ['w3', ['w3', 'w1', 'w2']],
   'm3': ['w1', ['w2', 'w1', 'w3']]}

  {'w1': ['m3', ['m1', 'm2', 'm3']],
   'w2': ['m1', ['m2', 'm1', 'm3']],
   'w3': ['m2', ['m3', 'm2', 'm1']]}
Note the following invariant: if a man is matched to a woman in the man's dictionary, then that same woman must be matched to that man in the woman's dictionary. Verify that this is true above.
Are these marriages stable? First, let's look just at m1, who is matched to w2. By his preferences, he would rather marry w3, but she prefers m2 (her match) to m1. Now, let's look just at w1, who is matched to m3. By her preferences, she would rather marry m1, but he prefers w2 (his match) to w1; also w1 would prefer to marry m2, but he also prefers w3 (his match) to w1. If you check all the other men and women (do it) you will find that you can find no pair who would both rather marry each other, rather than their current matches, so these marriages are considered stable.

Input and Output:
Read files of men and women and their rankings of all members of the opposite gender (highest to lowest preference), separated by semicolons, building a dictionary like the ones above (where each match is initially the special value None). As described above, we annotate the structure of this dictionary as {str:[str,[str]]}.
In the file, the person's name appears first, followed by the names of all members of the opposite gender in highest to lowest preference, separated by one semicolon character. For example, the input file men0.txt contains the following lines: these line could appear in this order, or any other, but the each man's preferences must appear in decleasing order of preference.

  m1;w3;w2;w1
  m2;w3;w1;w2
  m3;w2;w1;w3
The first line means, m1 ranks the members of the opposite gender in the order of preference from w3, w2, and w1 in decreasing order of preference Each line is guaranteed to start with a unique name, which is guaranteed to be followed by all the names of all members of the opposite gender, each appearing once; and all names are separated by semicolons.
When you print such information, print each person on a separate line, followed by his/her match and preferences. For example, the file above would print as:

  m1 -> [None, ['w3', 'w2', 'w1']]
  m2 -> [None, ['w3', 'w1', 'w2']]
  m3 -> [None, ['w2', 'w1', 'w3']]
Note that the names on the lines must be sorted in alphabetical order; the list of preferences must appear in the same order they appeared in the file. There are multiple pairs of data files for this program, all named like men0.txt and women0.txt; Test/debug your program on the first file; when you are done, test it on the remaining files.

Here is a description of the Gale/Shapley Algorithm for computing a stable marriage. You must implement this algorithm, as it is described below. There might be other stable marriages, but this algorithm will always compute the same one. This algorithm is not symmetric: here men get to propose to women and women get to accept/reject men. If we ran the algorithm the other way (with women proposing to men, and men accepting or rejecting women, we would also get a stable marriage, but the matches might be different.

It is fairly straightforward to specify the Gale/Shapley algorithm, which is straightforward to implement in Python. But, first you must understand these English instructions, and only then can you carefully translate them into Python code. You should hand-simulate this algorithm using the data above, and verify that it produces the results that you expect, before coding the algorithm in Python.

Make a copy of only the men's data structure: create a new dictionary that copies all data, including copying the lists, from the original dictionary. We make a copy because the algorithm below mutates the men's data structure, but we don't want its matching argument to change. In the steps below, mutate the copy, not the parameter.
Make an unmatched set that contains the names of all unmatched men. Initially, all men are unmatched, so this set will contain all the men in the men's dictionary.
Repeat the following process until there are no more unmatched men.
Remove (see the pop operation on sets) any man from the set of unmatched men.
Determine the woman that is highest on his preference list and remove that woman from his preference list (see the pop operation on lists). This man will try to propose to that woman.
If that woman is unmatched: match this man and that woman.
If that woman is matched, but pefers this man to her current match: unmatch that woman and her current match and add the man that she previously matched (he is now unmatched) to the set of unmatched men. Then, match this man and that woman.
If that woman is matched, and pefers her current match to this man, just add this man (still unmatched) back to the set of unmatched men.
Read these instructions carefully, a few times. Do not attempt to write any Python code to solve this problem until you understand this algorithm and can apply it to the data specified below. Hand simulate these instructions to ensure that you understand the algorithm; use the data above, which is automatically traced in the example below. Eventually you will write your Python code to produce such a trace conditionally.
Here is a trace (see the 3rd parameter to the make_match function below) for the men and women data structures specified above.

  Women Preferences (unchanging)
    w1 -> [None, ['m1', 'm2', 'm3']]
    w2 -> [None, ['m2', 'm1', 'm3']]
    w3 -> [None, ['m3', 'm2', 'm1']]

  Men Preferences (current)
    m1 -> [None, ['w3', 'w2', 'w1']]
    m2 -> [None, ['w3', 'w1', 'w2']]
    m3 -> [None, ['w2', 'w1', 'w3']]
 
  unmatched men = {'m2', 'm3', 'm1'} 

  m2 proposes to w3, who is currently unmatched, accepting proposal

  Men Preferences (current)
    m1 -> [None, ['w3', 'w2', 'w1']]
    m2 -> ['w3', ['w1', 'w2']]
    m3 -> [None, ['w2', 'w1', 'w3']]
 
  unmatched men = {'m3', 'm1'} 

  m3 proposes to w2, who is currently unmatched, accepting proposal

  Men Preferences (current)
    m1 -> [None, ['w3', 'w2', 'w1']]
    m2 -> ['w3', ['w1', 'w2']]
    m3 -> ['w2', ['w1', 'w3']]

  unmatched men = {'m1'} 

  m1 proposes to w3, who is currently matched, rejecting the proposal (likes current match better)

  Men Preferences (current)
    m1 -> [None, ['w2', 'w1']]
    m2 -> ['w3', ['w1', 'w2']]
    m3 -> ['w2', ['w1', 'w3']]
 
  unmatched men = {'m1'} 

  m1 proposes to w2, who is currently matched, accepting the proposal (likes new match better)

  Men Preferences (current)
    m1 -> ['w2', ['w1']]
    m2 -> ['w3', ['w1', 'w2']]
    m3 -> [None, ['w1', 'w3']]
   
  unmatched men = {'m3'} 

  m3 proposes to w1, who is currently unmatched, accepting the proposal

  Tracing terminated, the final matches: {('m1', 'w2'), ('m3', 'w1'), ('m2', 'w3')}
The resulting matches form stable marriages (the ones discussed above, when we discussed the meaning of stability). When this algorithm stops, the local copy of the men's data structure has become
  m1 -> ['w2', ['w1']]
  m2 -> ['w3', ['w1', 'w2']]
  m3 -> ['w1', ['w3']]
Note that each man's preference list shows only the women he did not propose to. Finally, if we used the same algorithm but let the women propose to the men, who accept or reject the proposals, we would get the following matches.

Tracing terminated, the final matches: {('w2', 'm2'), ('w1', 'm1'), ('w3', 'm3')}
These matches are all different, but the marriages are all still stable. So, who proposes to whom can determine the results of the algorithm: we can run the program, swapping the men's/women's files, to see if it produces an alternative stable matching.

Functions and Script:
Write the following functions and script. I am providing line counts for these function bodies not as requirements, but to indicate the lengths of well-written Pythonic code.
read_match_preferences has an open (file) parameter; it returns the dictionary representing each man (or women, depending on which file is read) and his/her match (initially None) and preferences (body is 6 lines).
dict_as_str has a men or women dictionary, key function (default None) and bool (default False) as parameters; it returns a multi-line string (each line is ended by '\n'), which when printed shows the contents of the dictionary in the appropriate textual form. The key function determines the ordering and the bool determines whether to reverse it: like the key and reverse parameters used for sort/sorted in Python. This function is used to print both the men's/women's dictionaries, in the form dicussed above in the Input/Output section.
Important: The key function (and its use when iterating over the dictionary in dict_as_str) must assume that its argument is a key in the dictionary, not an item; otherwise the batch self-check test will fail even if your code works. (body is 4 lines; can you do it in 1?).

who_prefer has a list (of str) of preferences and two values (str) that are in the list; it returns the value with the higher preference: e.g., who_prefer(['w3','w1','w2'], 'w2', 'w3') returns w3 -the one present earlier in the list. Hint: I used this function in make_match defined below (body is 1 line).
extract_matches has a men dictionary as a parameter; it returns a set of 2-tuples: each has a match with the man in index 0 and the woman in index 1. Hint: I used this function in make_match defined below (body is 1 line).
make_match has a men and women dictionary as parameters, as well as a tracing parameter whose default value is False; it returns a set of 2-tuples: each has a match with the man in index 0 and the woman in index 1. This function uses the Gale/Shapley algorithm described above to find the match; if tracing is True it creates a trace in the form the example trace shown above (body is 25 lines, but only 18 lines without tracing code).
Write a script at the bottom of this module (in if __name__ == '__main__':) that prompts the user to enter the files storing the men and women preferences; reads these files and creates the required dictionaries; labels and prints both dictionaries (using dict_as_str); prompts the user about whether to trace the matching, then computes (using make_match) and prints the stable matches.
Sample Interaction:
The program, as specified, will have the following interaction: user-typed information appears in italics. Your output should match this one.
  Specify the file name representing the preferences for men: men0.txt
  Specify the file name representing the preferences for women: women0.txt

  Men Preferences
    m1 -> [None, ['w3', 'w2', 'w1']]
    m2 -> [None, ['w3', 'w1', 'w2']]
    m3 -> [None, ['w2', 'w1', 'w3']]

  Women Preferences
    w1 -> [None, ['m1', 'm2', 'm3']]
    w2 -> [None, ['m2', 'm1', 'm3']]
    w3 -> [None, ['m3', 'm2', 'm1']]

  Specify choice for tracing algorithm[True]: False

  The final matches: {('m1', 'w2'), ('m3', 'w1'), ('m2', 'w3')}
Note that if the user specified True for tracing the algorithm, the program would also print all the information shown above in the example of tracing the Gale/Shapley algorithm. Finally, you can also try processing the men1.txt/women1.txt and men2.txt/women2.txt pairs of files. You can print these data files and hand-simulate the Gale/Shapely algorithsm on them to compute their stable matches. You can also feed the women file in as the men file, and the men file in as the women file, to see the match that results from letting women propose and men accept or reject: it can produce different matching pairs, but the matching pairs it produces will be stable.

Problem #3: Finite Automata	
Problem Summary:
Write the required functions and script that prompts the user for the name of a file representing a finite automaton: indicating its states and input->state transitions; reads the information in the file (storing the finite automaton in a dictionary); prints the finite-automaton/dictionary in a special form; prompts the user for the name of a file storing the start-state and inputs to process (each line in the file contains this combination); repeatedly processes these lines, computing the results of the finite automaton on each input, and then prints the results. Note that a finite automaton is really a program; in this problem we are reading a program from a file and then executing it (running the finite automaton) on various inputs. So, we are really writing a compiler/interpreter for a small programming language.
A finite automaton (FA) is an machine that is sometimes called a Deterministic Finite Automaton (DFA; see the next problem for an NDFA: a non-deterministic finite automaton). An FA is described by its states and its transitions: each transition for a state specifies an input and what state in the FA that input leads to. We can illustrate an FA as a graph with state labels in circles and edge labels for transitions (see below).

Input and Output:
Read a file that describes a FA: each line contains a state and an arbitrary number of input->state transitions. Build a dictionary such that each key is a str state and whose associated value is another dictionary specifying all the transitions from that state: this second dictionary has keys that are str inputs and associated values are str states. The first token on each line is the str state and the remaining tokens (always coming in pairs) are str inputs and their resulting states. All tokens (which can comprise any number of characters) are separated by one semicolon character. We annotate this dictionary as {str:{str:str}}.
For example, the input file faparity.txt contains the following lines (which could appear in this order, or any other and still specify the same FA):

  even;0;even;1;odd
  odd;0;odd;1;even
Here is a picture of the parity FA. It graphically illustrates the two states (even and odd) and their transitions, using inputs (0 and 1) that always lead back to one of these two states.


Here, the state even (meaning it has seen an even number of 1 inputs so far) is a key in the main dictionary. Its value is a dictionary with two key/value pairs 0->even and 1->odd. It means that in the even state, if the input is a 0 the FA stays in the even state; if the input is a 1 the FA goes to the odd state. And similarly (the next line) means that for the odd state, if the input is a 0 the FA stays in the odd state; if the input is a 1 the FA goes back to the even state. So, seeing an input of 0 keeps the FA in the same state; seeing an input of 1 flips the FA into the other state.

Print the finite automaton, one state (and its transitions) per line; the states are printed alphabetically and the transition dictionary for each state is printed as a list of input/state items (tuples) such that these are printed alphabetically by the inputs.

For example, the file above would print as:

  Specified details of this Finite Automaton
    even transitions: [('0', 'even'), ('1', 'odd')]
    odd transitions: [('0', 'odd'), ('1', 'even')]
Note that there are multiple data files for this program: faparity.txt and fadivisibleby3.txt; test/debug your program on the first file; when you are done, test it on the last file. Draw the FA represented by each for to ensure that your code correctly prints and computes with it. Important: This task is not to write a Python code that simulates the Parity FA; it is to write code that simulates any FA, whose description it reads from a file.

Next, repeatedly read and process lines from a second input file, computing the results of the finite automaton running on the specified start-state with its inputs; then print out the results in a special form. Each line in the file contains a start-state followed by a sequence of inputs (all separated by semicolons). The start-state will be a state in the FA (it is a key in the outer dictionary) the inputs may specify legal or illegal transitions (may or may not be keys in some inner dictonary).

For example, the input file fainputparity.txt contains the following three lines:

  even;1;0;1;1;0;1
  even;1;0;1;1;0;x
  odd;1;0;1;1;0;1
The first line means, the start-state is even and the inputs are 1, 0, 1, 1, 0, and 1.
The result of processing each line is to print the start-state, and then each input and the new state it transitions to, and finally print the stop-state. For the parity FA and the first line in this file, it should print

Start state = even
  Input = 1; new state = odd
  Input = 0; new state = odd
  Input = 1; new state = even
  Input = 1; new state = odd
  Input = 0; new state = odd
  Input = 1; new state = even
Stop state = even
Note that the second line contains an input x which is not a legal input allowed in any state; any such input should stop the simulation for that line only, continuing to start a new simulation for all following lines (as illustrated in the Sample Interaction).

Functions and Script:
Write the following functions and script. I am providing line counts for these function bodies not as requirements, but to indicate the lengths of well-written Pythonic code.
read_fa has an open (file) parameter; it returns the dictionary representing the finite automaton; hint: I used splicing and the zip function to build the inner dictionaries. (body is 6 lines).
fa_as_str has a dictionary parameter (representing the FA); it returns a multi-line string (each line is ended by '\n'), which when printed shows the contents of the FA in the appropriate textual form: sorted alphabetically by state, with a state's transitions sorted by their input value (body is 4 lines; can you do it in 1?).
process has a dictionary parameter (representing the FA), a str parameter (representing the start-state), and a list parameter (representing a list of str inputs); it returns a list that contains the start-state followed by tuples that show the input and resulting state after each transition. For the example shown above, process returns the following list.
['even', ('1', 'odd'), ('0', 'odd'), ('1', 'even'), ('1', 'odd'), ('0', 'odd'), ('1', 'even')]
Finally, if an input is illegal (is not the key in some transition for the current state), say 'x', for the parity FA, then process should terminate with the last tuple in the list indicating a problem: ('x', None) (body is 9 lines).
interpret has a list parameter (the list result produced by process); it returns a multi-line string (each line is ended by '\n'), which when printed illustrates the results of processing an FA on an input in the appropriate textual form. See how it prints the example list argument shown above in the output further above. Also see the Sample Interaction below to see how it prints input errors: see the middle example (body is 9 lines).
Write a script at the bottom of this module (in if __name__ == '__main__':) that prompts the user to enter the file describing the FA, prints it, prompts the user to enter the file containing lines of start-states and input, simulates the FA on each line, printing the results in the appropriate textual form (body is 7 lines).
Sample Interaction:
The program, as specified, will have the following interaction: user-typed information appears in italics. Your output should match this one.
  Specify the file name representing the Finite Automaton: faparity.txt

  Specified details of this Finite Automaton
    even transitions: [('0', 'even'), ('1', 'odd')]
    odd transitions: [('0', 'odd'), ('1', 'even')]

  Specify the file name representing multiple start-states and their inputs: fainputparity.txt

  Computed FA trace from its start-state
  Start state = even
    Input = 1; new state = odd
    Input = 0; new state = odd
    Input = 1; new state = even
    Input = 1; new state = odd
    Input = 0; new state = odd
    Input = 1; new state = even
  Stop state = even
  
  Computed FA trace from its start-state
  Start state = even
    Input = 1; new state = odd
    Input = 0; new state = odd
    Input = 1; new state = even
    Input = 1; new state = odd
    Input = 0; new state = odd
    Input = x; illegal input: simulation terminated
  Stop state = None

  Computed FA trace from its start-state
  Start state = odd
    Input = 1; new state = even
    Input = 0; new state = even
    Input = 1; new state = odd
    Input = 1; new state = even
    Input = 0; new state = even
    Input = 1; new state = odd
  Stop state = odd
You can also try the fadivisibleby3.txt finite automaton file, which determines whether an integer (sequence of digits) is divisible by 3: it is divisible if the finite automaton stops in state rem0. It's input file fainputdivisibleby3.txt tries the number 12,435,711, which is divisible by 3 and number 823, which is not divisible by 3: dividing 823 by 3 leaves a remainder of 1.

Problem #4: Non-Deterministic FA	
Problem Summary:
Write the required functions and script that solve, for a Non-Deterministic Finite Automaton, the same problem that was solved for a Deterministic Finite Automaton in Problem #3 (above). Read about the differences between these two automata (below). Hint: Adapt your code for the FA problem to solve the more general NDFA problem.
A non-deterministic finite automaton (NDFA) is machine described by its states and its transitions: each transition for a state specifies an input and a set of states (more than one is allowed) that input can lead to: sets with more than one states is what makes it non-deterministic. We can illustrate a NDFA as a graph with state labels in circles and edge labels for transitions (see below). The critical difference between an FA and an NDFA is that an NDFA can have multiple edges with the same label going to different states (we'll see how to represent and simulate such transitions below).

Input and Output:
Read a file that describes a NDFA: each line contains a state and an arbitrary number of input->state transitions. Build a dictionary such that each key is a str state and whose associated value is another dictionary specifying all the transitions from that state: this second dictionary has keys that are str inputs and associated values that are sets of str states: all the states a particular input can lead to. The first token on each line is the str state and the remaining tokens (always coming in pairs) are str inputs and states. All tokens (which can comprise any number of characters) are separated by one semicolon character. We annotate this dictionary as {str:{str:{str}}}.
For example, the input file ndfaendin01.txt contains the following lines (which could appear in this order, or any other and still specify the same NDFA):

  start;0;start;1;start;0;near
  near;1;end
  end
Here is a picture of the endin01 NDFA. It graphically illustrates the three states (start, near, and end) and their transitions, using inputs (0 and 1).


Here, the state start is a key in the main dictionary. It's value is a dictionary with two key/value pairs: 0 mapping to the set containing start and near, and 1 mapping to the set containing just start. It means that in the start state, if the input is a 0 the NDFA can stay in the start state or it can go to the near state; if the input is a 1 the NDFA must stay in the start state. And similarly the next line means that in the near state, if the input is a 1 the NDFA must go into the end state. The last line means that the end state has no transitions out of it.

Print the NDFA, one state (and its transitions) per line; the states are printed alphabetically and the transition dictionary for each state is printed as a list of input/set of state items (2-tuples) such that these are printed alphabetically by the inputs, and the set of states for each input is printed as an alphabetically sorted list (e.g., near comes before start). Note that the state end is a key in the main dictionary, whose associated transitions are an empty dictionary.

For example, the file above would produce:

  Specified details of this Non-Deterministic Finite Automaton 
    end transitions: []
    near transitions: [('1', ['end'])]
    start transitions: [('0', ['near', 'start']), ('1', ['start'])]
Note that there are multiple data files for this program: ndfaendin01.txt and ndfatrain.txt and ndfare.txt;; test/debug your program on the first file; when you are done, test it on the last file. Draw the FA represented by each for to ensure that your code correctly prints and computes with it.

Next, repeatedly read and process lines from a second input file, computing the results of the non-determinisitc finite automaton on the specified start-state with its inputs ; then print out the results in a special form. Each line in the file contains a start-state followed by a sequence of inputs (all separated by semicolons). The start-state will be a state in the FA (it is a key in the outer dictionary) the inputs may specify legal or illegal transitions (may or may not be keys in some inner dictionary).

For example, the input file ndfainputendin01.txt contains the following two lines:

  start;1;0;1;1;0;1
  start;1;0;1;1;0;0
For example, the first line means, the start-state is start and the inputs 1, 0, 1, 1, 0, and 1.
The result of processing each line is to print the start-state, and then each input and the new states (plural) it could transition to (the could is what makes it non-deterministic), and finally print the stop-states. For the ndfaendin01 NDFA and the first line in this file, it should print

  Start state = start
    Input = 1; new possible states = ['start']
    Input = 0; new possible states = ['near', 'start']
    Input = 1; new possible states = ['end', 'start']
    Input = 1; new possible states = ['start']
    Input = 0; new possible states = ['near', 'start']
    Input = 1; new possible states = ['end', 'start']
  Stop state(s) = ['end', 'start']
Note that the set of states it might be in are printed as an alphabetized list. Also note especially that in the start state, if the input is a 0, then the NDFA can either remain in the start state or go into the near state. For this program, we keep track of all states that the NDFA can be in, using a set of new possible states. For the next input, 1, we can be either in the start state (from the start state; an input of 1 allows us to stay in the start state) or the end state (from the near state; an input of 1 allows us to transition to the end state). Thus, we keep track of the set of states the NDFA can be in, and the new set of states the NDFA can be in after processing the next input. In this example, because 'end' is included in the stop-states, this input does end in 01.

For any state that does not have a transition specifying the current input, ignore that input for that state. For example, if near is one of the possible states and 0 is the input, ignore the 0 for the near state.

Functions and Script:
Write the following functions and script. I am providing line counts for these function bodies not as requirements, but to indicate the lengths of well-written Pythonic code.
read_ndfa has an open (file) parameter; it returns the dictionary representing the non-deterministic finite automaton; hint: I used splicing and the zip function to build the inner dinctionaries, and I called the setdefault function for the inner dict: alternatively I could have built it as defaultdicts from the standard collections module (body is 9 lines).
ndfa_as_str has a dictionary parameter (representing the FA); it returns a multi-line string (each line is ended by '\n'), which when printed shows the contents of the NDFA in the appropriate textual form: sorted alphabetically by state, with a state's transitions sorted by their input values, and sorted by states if an input results in multiple states (body is 4 lines; can you do it in 1?).
process has a dictionary parameter (representing the NDFA), a str parameter (representing the start-state), and a list parameter (representing a list of str inputs); it returns a list that contains the start-state followed by tuples that show the input and resulting set of states after each transition. For the example shown above, process returns the following list.

  ['start', ('1', {'start'}), ('0', {'near', 'start'}), ('1', {'end', 'start'}), ('1', {'start'}),
    ('0', {'near', 'start'}), ('1', {'end', 'start'})]
Finally, remember that if an input is illegal for the current state (is not the key in some transition for the current state), just ignore it. But if the input leads to no possible states (the empty set of states) terminate processing there (body is 12 lines).
interpret has a list parameter (the list result produced by process); it returns a multi-line string (each line is ended by '\n'), which when printed illustrates the results of processing an NDFA on an input in the appropriate textual form. Note that in this output the sets computed in process appear as lists sorted alphabetically by state. See how it prints the example list argument shown above in the Sample Interaction below (body is 5 lines).
Write a script at the bottom of this module (in if __name__ == '__main__':) that prompts the user to enter the file describing the NDFA, prints it, prompts the user to enter the file containing lines of start-states and input, and simulates the NDFA on each line, printing the results in the appropriate textual form (body is 7 lines).
Sample Interaction:
The program, as specified, will have the following interaction: user-typed information appears in italics. Your output should "match" this one.
  Specify the file name representing the Non-Deterministic Finite Automaton: ndfaendin01.txt

  Specified details of this Non-Deterministic Finite Automaton 
    end transitions: []
    near transitions: [('1', ['end'])]
    start transitions: [('0', ['near', 'start']), ('1', ['start'])]

  Specify the file name representing multiple start-states and their inputs: ndfainputendin01.txt

  Computed NDFA trace from its start-state
  Start state = start
    Input = 1; new possible states = ['start']
    Input = 0; new possible states = ['near', 'start']
    Input = 1; new possible states = ['end', 'start']
    Input = 1; new possible states = ['start']
    Input = 0; new possible states = ['near', 'start']
    Input = 1; new possible states = ['end', 'start']
  Stop state(s) = ['end', 'start']
  
  Computed NDFA trace from its start-state
  Start state = start
    Input = 1; new possible states = ['start']
    Input = 0; new possible states = ['near', 'start']
    Input = 1; new possible states = ['end', 'start']
    Input = 1; new possible states = ['start']
    Input = 0; new possible states = ['near', 'start']
    Input = 0; new possible states = ['near', 'start']
  Stop state(s) = ['near', 'start']
In Week #2 of this course we will cover EBNF and regular expressions, which relate to the files below. You can run these files on your code to ensure they produce the correct results.

The ndfatrain.txt file is a non-deterministic finite automaton that determines whether or not a train (a sequence of characters representing different kinds of cars) is a legal train according to Chapter Exercise #7 in the ENBF lecture. Its input file is ndfainputtrain.txt, which starts with a legal train (one that ends with the state done as one possible state) followed by an illegal train (one that does not end with the state done as one possible state).

The ndfare.txt file is a non-deterministic finite automaton translation of the regular expression ((a*|b)cd)+. Its input file is ndfainputre.txt, which starts with a match (one that ends with the state last as one possible state) followed by a non-match (one that does not end with the state last as one possible state).

Problem #5: Word Generator	
Problem Summary:
Write the required functions and script that prompts the user to enter the order statistic (a positive number) and the name of a file of text; reads the file of text (storing it in a special corpus dictionary); prints the dictionary in a special form; prompts the user to enter the order statistic number of words, and the number of words to generate, then print a list of that many words randomly generated from the corpus. Your program will "learn" the word pattern of an author (based on some "order statistic" and reading a large sample of the author's writing) and then generate random text following the author's word patterns.
Input and Output:
After prompting for the order statistic, read a file of words, building a corpus dictionary storing data annotated as {(str):[str]}. Here the dictionary's keys are tuples of n words (where n is the order statistic) and each key's assocaited value is a list of all the words in the text that somewhere follow these words: e.g., if n were 2, the dictionary would contain a key for every pair of words appearing next to each other in the text, and each would have an associated value that is a list of all the words following these two (no matter where the pair occurs, with NO DUPLICATES allowed in the values list).
An easy way to read the words one at a time is to use the result returned by the helper function word_at_a_time (which I have supplied at the top of wordgenerator.py). When passed an open file to read from, this function returns an object on which we can (a) call next and/or (b) iterate over, using a for loop. For example, if a file named f.txt contained

  a b c
  d e
then executing the code
  i = word_at_a_time(open('f.txt'))
  print(next(i), next(i))  # print next (really first) two values in the file
  for c in i:              # iterate over all remaining values in the file
      print(c)             #   and print them
would print
  a b
  c
  d
  e
We will learn when we examine iterators in depth that the for loop implicitly calls next on the object (here i) that it is iterating over. For now, use this approach to read some number of words (based on the order statistic), followed by reading all the other words.

We can build the dictionary by "prereading" n words (by calling next explicitly) into a list (assume that this is always possible; how might it not be?); then repeatedly read the next word and put it in as a value associated with the list of pre-read words; then, drop the "oldest" word at the beginning of the list, and add this next word as the "youngest" at the end of the list (always keeping the list length at n); repeating this process until all the words have been read. Remember to convert this list of words to a tuple of words, before using it as a key in the dictionary.

For a simple example, the file wginput1.txt contains the following lines (it could have all this information on one line or more lines):

  a b c b a d c b a d
  c a a b a a d
Print all the associations in the corpus dictionary, one per line in standard lexical order; after printing all associations, print the length of the smallest and largest list that is a value in the dictionary. Each line contains an n word tuple, followed by the list of unique words (no duplicates) that follow them anywhere in the text. In standard lexical order, the keys appear in order relative to the first word in the tuple; for all first words that are the same, they appear in order relative to the second word in the tuple; for all first and second words that are the same, they appear in order relative to the thrid word in the tuple; etc. (see the example below).

For example, the file above would produce:

  Corpus
    ('a', 'a') can be followed by any of ['b', 'd']
    ('a', 'b') can be followed by any of ['c', 'a']
    ('a', 'd') can be followed by any of ['c']
    ('b', 'a') can be followed by any of ['d', 'a']
    ('b', 'c') can be followed by any of ['b']
    ('c', 'a') can be followed by any of ['a']
    ('c', 'b') can be followed by any of ['a']
    ('d', 'c') can be followed by any of ['b', 'a']
  min/max list lengths = 1/2
For example, ('a','d') appears three times in the text above, twice followed by 'c' and once followed by nothing (at the end of the file); ('a','b') appears twice in the file above, first followed by 'c' and second followed by 'a'.

Prompt the user for the words to start with (there are order statistic number of them) and the number of random words after that to generate. Produce such a list of words and print it.

A random 10 word list, after the words a and d might print as

    Random text = ['a', 'd', 'c', 'a', 'a', 'd', 'c', 'a', 'a', 'd', 'c', 'b']
In the result we start with a d (2 words specified by the user), we know only c can come next; then using d c we know that either b or a must come next; it randomly chooses a...
Functions and Script:
Write the following functions and script. I am providing line counts for these function bodies not as requirements, but to indicate the lengths of well-written Pythonic code.
read_corpus has an order statistic (int) parameter and and open (file) parameter; it returns the dictionary representing the corpus of words in a file (body is 8 lines).
corpus_as_str has a dictionary parameter (representing the corpus); it returns a multi-line string (each line is ended by '\n'), which when printed shows the contents of the corpus followed by the min/max list lengths in the appropriate textual form (body is 7 lines; can you do it in 4?).
produce_text has a dictionary parameter (representing the corpus), a list parameter (representing the starting words), and an int parameter (representing the number of additional words to generate); it returns a list that contains the the starting words followed by the generated words.
Hints: Let n be the order statistic of the dictionary. Construct two lists ([str]), each initially storing these same n starting words. The first will always contain only the most recent n words (to be coverted to a tuple and used as a key in the dictionary); the second will grow to contain all the generated words. Generate a random next word from the dictionary by using the choice function in the random module: e.g., choice(['a','b','c']) will return a random value in the list, either 'a', 'b', or 'c'); add it to both lists; then, drop the first word from the first list, so it remains a list of length n; repeat until you have generated the required number of words.

Warning: you might have to stop prematurely if you generate the last n words in the text, and if these words occur nowhere else. That is because in this case, there is no random word to generate following them; in this case append a None to the end of the list of words and immediately return that list.

A slightly more elegant solution in Python uses only one list, copying the last order statistic values of it into a tuple when needed for a key to the dictionary. Ensure that you do not mutate any of the parameters (body is 8 lines).

Write a script at the bottom of this module (in if __name__ == '__main__':) that prompts the user for (a) the order statistic (rejecting non-positive values), (b) the file storing the text, (c) order statistic words from the text, and (d) the number of random words to generate (reject any negative values); it calls these functions to solve the problem, and print the appropriate information (7 lines).
Sample Interaction:
The program, as specified, will have the following interaction: user-typed information appears in italics. Your output should match the form of this one (the actual random text my vary).
  Specify the order statistic: 2
  Specify the file name representing the text to process: wginput1.txt
  Corpus
    ('a', 'a') can be followed by any of ['b', 'd']
    ('a', 'b') can be followed by any of ['c', 'a']
    ('a', 'd') can be followed by any of ['c']
    ('b', 'a') can be followed by any of ['d', 'a']
    ('b', 'c') can be followed by any of ['b']
    ('c', 'a') can be followed by any of ['a']
    ('c', 'b') can be followed by any of ['a']
    ('d', 'c') can be followed by any of ['b', 'a']
  min/max list lengths = 1/2
  
  Specify 2 words starting the list
  Specify word 1: a
  Specify word 2: d
  Specify # of words to append at the end of the started list: 10
  Random text = ['a', 'd', 'c', 'a', 'a', 'd', 'c', 'a', 'a', 'd', 'c', 'b']
You can also try reading a much larger file included in this project folder war_and_peace.txt, Leo Tolstoy's, "War and Peace". I tried it with an order statistic of 3. The corpus has over 432,000 entries; the biggest key triple had an associated value with 120 unique words in it. It tooks a few second to produce the result. The key was ('one', 'of', 'the') and its associated value was the list

  ['best', 'genuine', 'next', 'fainting', 'buttons', 'footmen',
   'inner', 'tubs', 'doors', 'princesses', 'wines', 'ladies', 'doorways',
   'priests', 'columns', 'servants', 'associations', 'sweetest', 'largest',
   'great', 'infantry', 'most', 'battalion', 'officers', 'bolder', 'post',
   'ordinary', 'second', 'pleasantest', 'soft', 'lodges', 'warmest', 'longest',
   'hussars', 'apsheron', 'soldiers', 'lines', 'innumerable', 'drivers', 
   'hindmost', 'foremost', 'boulevards', 'principal', 'maids', 'happiest',
   'first', 'balls', 'players', 'brothers', 'brethren', 'eight', 'nursemaids',
   'hospital', 'frenchmen', 'masonic', 'committees', 'richest', 'greatest',
   'mahogany', 'front', 'merry', 'figures', 'mad', 'conditions', 'borzoi',
   'men', 'strange', 'rostovs', 'looking', 'stupidest', 'young', 'women',
   'veterans', 'bridges', 'swaying', 'aides', 'polish', 'chief', 'millions',
   'generals', 'rooms', 'senators', 'old', 'prince', 'coachmen', 'visitors',
   'educational', 'peasants', 'wealthiest', 'estates', 'carts', 'wounded',
   'head', 'doctors', 'orders', 'staff', 'least', 'tents', 'german', 'highest',
   'disinterested', 'shutters', 'passages', 'smiths', 'russians', 'gentlemen',
   'fancies', 'glasses', 'moscow', 'provincial', 'superior', 'few', 'combatants',
   'irregulars', 'french', 'big', 'marshals', 'three', 'plans', 'opinions']
With the appropriate modification, we can use this same program to read/generate music or DNA sequences or any other data made from an sequence of symbols.

