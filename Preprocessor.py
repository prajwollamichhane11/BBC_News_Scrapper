filename = 'News.csv'                         #Put your filename here
word_delete = ['<p class="story-body__introduction">','</p>','<p>','<strong>','</strong>']                           #Put what you want to delete here
with open(filename, 'r') as file_text:            #Open your file
    lines = file_text.readlines()                 #Read all the lines from your file, then put them in a list
    newlines = []                                 #Make a list to save edits in
    for line in lines:
        for i in range (len(word_delete)):
            newline = line.replace(word_delete[i], ' ')   #Replace the text in word_delete to an empty string (aka nothing)
            newlines.append(newline)                  #Add the edit to the list with edits
with open(filename, 'w') as file_text:            #Open the file, but in write mode
    file_text.writelines(newlines)                #Write the list with edits to the new file
