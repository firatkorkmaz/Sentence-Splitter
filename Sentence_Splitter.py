# Sentence Splitter by Limited Number of Words/Letters of Lines #

def sentence_splitter():
    # Enter Words Separated with Space
    # Example: "the quick brown fox jumps over the lazy dog"
    inputString = input("\nEnter Words Separated with Space: ")
    wordData = inputString.split(' ')

    # Select Limit Mode
    while True:
        inputMode = input("\nSelect Limit Mode:\nWord Limit  : 1\nLetter Limit: 2\nEnter 1 or 2: ")
        if not inputMode.isdigit() or int(inputMode) != 1 and int(inputMode) != 2:
            print("Please Enter 1 or 2!")
        else:
            modeData = int(inputMode)
            break


    # Start Processing According to the Limit Mode
    if modeData == 1:        # Splitting the String by Lines with Word Count Limit
        while True:
            limitData = input("\nWord Number per Line: ")
            if not limitData.isdigit():
                print("Please Enter A Number!")
            else:
                words = int(limitData)      # Integer Type Word Count is Assigned
                break

        line = []                           # Lines Limited by Word Count
        ln = ""                             # Temporary Line

        for i in range(0, len(wordData)):   # For Each Word:
            if words == 0:                  # If the Word Count is Zero
                break                       # Stop the Process

            elif i == 0:
                ln = wordData[i]            # There will Be No Space Before the 1st Word

            else:
                if len(ln.split(' ')) + 1 <= words:    # if length(Added Words) + 1 New Word <= Word Count
                    ln += " " + wordData[i]

                else:
                    line.append(ln)          # Append the Temp Line to the Line List
                    ln = wordData[i]         # start the Next Line with the Current Word

                if i == len(wordData) - 1:   # If This is the Last Word, Loop must End with Appending It
                    line.append(ln)

        # Testing
        print()
        for x in line:
            print(x)


    elif modeData == 2:      # Splitting the String by Lines with Letter Count Limit
        while True:
            limitData = input("\nLetter Number per Line: ")
            if not limitData.isdigit():
                print("Please Enter A Number!")
            else:
                letters = int(limitData)    # Integer Type Letter Count is Assigned
                break

        line = []                           # Lines Limited by Letter Count
        ln = ""                             # Temporary Line

        for i in range(0, len(wordData)):   # For Each Word
            if len(wordData[i]) > letters:  # If A Word is Longer than the Letter Limit
                if ln != "":                # If the 1st Word Exceeds the Limit, do Not Add "" to the Lines
                    line.append(ln)         # Add the Word from the Previous Iteration and Stop the Process
                break                   # This could Be "continue" If It is Required to Print the Remaining

            else:
                if i == 0:
                    ln = wordData[i]        # There will Be No Space Before the 1st Word

                else:
                    if len(ln) + 1 + len(wordData[i]) <= letters:  # if length(ln + " " + wordData[i]) <= Letter Count
                        ln += " " + wordData[i]

                    else:
                        line.append(ln)     # Append the Current Temporary Line to the Line List
                        ln = wordData[i]    # Start the Next Line with the Current Word: wordData[i]

                    if i == len(wordData) - 1:  # If This is the Last Word, Loop must End with Appending It
                        line.append(ln)

        #Testing
        print()
        for x in line:
            print(x)
            

sentence_splitter()