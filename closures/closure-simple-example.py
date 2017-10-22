def printMsg(msg):
#This is the main outer function that encloses printer function

    #this function is nested inside the printMsg function
    def printer():

        print(msg)
    #We return a function when printMsg function is called
    return printer
#here we call the function printMsg and store its output in another variable
another = printMsg("Hello")
another()

#we then call another and the output is
# Hello

#this is a simple example of closure that even when the execution
#of printMsg was finished, the message was still remembered and when we call
#another, the message Hello was displayed
