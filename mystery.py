# Name: Your Name Goes Here
# SI 206
# HW6 - Regular Expressions

import re
import os

def read_file(filename):
    """ Return a list of the lines in the file with the passed filename """
    
    # Open the file and get the file object
    source_dir = os.path.dirname(__file__) #<-- directory name
    full_path = os.path.join(source_dir, filename)
    infile = open(full_path,'r')
    
    # Read the lines from the file object into a list
    lines = infile.readlines()
    
    # Close the file object
    infile.close()
    
    # return the list of lines
    return lines

            
def find_dates(filename):
    """ Return a list of valid dates from the text file. 
    
        filename -- the name of the file to read from
        return -- the list of valid dates found in the file
    """
    matches = []
    reg = re.compile(r"((?:[0-9]{2}|[0-9]{1})([\/\.\-])(?:[0-9]{2}|[0-9]{1})\2(?:[0-9]{4}|[0-9]{2}))")
    for line in open(filename, 'r'):
        match_tuples = reg.findall(line)
        if match_tuples:
            line_matches, _ = zip(*match_tuples)
            matches.extend(line_matches)
    return matches


def find_emails(filename):
    """ Return a list of valid emails in the text file with the given filename """
    matches = []
    reg = re.compile(r"[\w\.]+@[\w\.]+")
    for line in open(filename, 'r'):
        line_matches = reg.findall(line)
        matches.extend(line_matches)
    return matches


def find_phoneNumbers(filename):
    """ Return a list of valid phone numbers in the text file with the given filename """
    """
    xxx/xxx-xxxx (eg, 206/782-8410)
    xxx.xxx.xxxx (eg, 206.782.8410)
    xxx xxx xxxx (eg, 206 782 8410)
    (xxx) xxx-xxxx (eg, (206) 782-8410)
    xxx-xxx-xxxx (eg, 206-782-8410 )
    xxxxxxxxxx (eg, 2067828410)
    """
    matches = []
    reg1 = re.compile(r"(\d{3}([\-\.\s]?)\d{3}\2?\d{4})")
    reg2 = re.compile(r"\d{3}\/\d{3}\-\d{4}")
    reg3 = re.compile(r"\(\d{3}\)\s\d{3}\-\d{4}")
    for line in open(filename, 'r'):
        # reg1
        match_tuples = reg1.findall(line)
        if match_tuples:
            line_matches, _ = zip(*match_tuples)
            matches.extend(line_matches)
        #reg2
        line_matches = reg2.findall(line)
        matches.extend(line_matches)
        #reg3
        line_matches = reg3.findall(line)
        matches.extend(line_matches)
    return matches


## Extra credit
def count_word(filename, word):
    """ Return the number of times a given word or its plural (add s) appears in the file 
    
        fileName -- the name of the file to read from
        word -- the word to look for
        return -- a count of the number of times the word or its plural appears in the file 
    """
    pass
        

## Do not modify the code below
## This function is for grading and debugging purposes
## statistics function reports your score based on the number of matches you got correct. 
def statistics(list1, list2):
    #print("Function output: ",list1)
    #print("Actual output: ", list2)
    matches = set(list2).intersection(set(list1)) 
    score = (len(matches)/len(list2))*20
    if len(matches)==len(list2):
        # no mismatches
        print("You found all the matches! Woohooo! Your score is: ", int(score))
    else:
        print("Looks like you missed some matches. Your score is:", int(score))
        print("You missed:", list(set(list2) - matches))

if __name__ == "__main__":
    filename = "The_Adventures_of_Sherlock_Holmes.txt"
    
    #Report the accuracy of find_dates function
    print("Testing find_dates function")
    statistics(find_dates(filename), [
        '11/29/02',
        '9/14/2020',
        '12-1-98',
        '12/09/19',
        '10-9-1890',
        '8.13.18',
        '11/31/16',
        '10-12-2021',
        '12.7.2018',
        '3.4.1991',
        '3/2/10',
        '5-16-1919',
        '2.4.91'])

    print("--------------------------------------------")
    #Report the accuracy of find_emails function
    print("Testing find_emails function")
    statistics(find_emails(filename), [
        'source@collab.sakaiproject.org',
        'm05ECIaH010327@nakamura.uits.iupui.edu',
        'louis@media.berkeley.edu',
        'rjlowe@iupui.edu',
        'cwen@iupui.edu',
        'gsilver@umich.edu',
        'apache@localhost','antranig@caret.cam.ac.uk',
        'gopal.ramasammycook@gmail.com'
    ])

    print("--------------------------------------------")
    # Report the accuracy of find_phoneNumbers function
    print("Testing find_phoneNumbers function")
    statistics(find_phoneNumbers(filename), [
        '674-763-9655',
        '694/876-8944',
        '767.764.7643',
        '385-765-9867',
        '3348769876',
        '(879) 765-3457',
        '765/987-8765',
        '9864636672',
        '780 764 3456',
        '780 345 6703',
        '675.673.6876',
        '670-465-3426',
        '780/654-5783',
        '567-796-8943',
        '(670) 765-5632',
        '456-565-5430',
        '764/433-5675',
        '543.545.4533',
        '309-321-4345'
    ])
    
    count = count_word(filename,"lip")
    if count == 10:
        print("You earned 3 extra points for finding the correct number")
    else:
        print("Count word for shoud return 10 and it returned: " + str(count))
    
    





