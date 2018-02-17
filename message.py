import re
def spamDetection(messages, spamSignals):
    fail = "failed :"
    ans = ["Passed","Passed","Passed","Passed"]
    user = {}
    message ={}
    count = 0
    fault = 0
    spam = ""
    dim = len(messages)
    i = 0
    while i < len(messages):
        if (len(messages[i][0].split(" ")) < 5):
            count += 1
        if (messages[i][0] not in message.keys()):
            message[messages[i][0]] = 1
        else:
            message[messages[i][0]] += 1
        if (messages[i][1] not in user.keys()):
            user[messages[i][1]] = []
            user[messages[i][1]].append(messages[i][0])
        else:
            user[messages[i][1]].append(messages[i][0])
        j = 0
        while j < len(spamSignals):
            print( re.split('! | ,| " " | @ | # | $ | % | * | &',messages[i][0].lower()))
            if (spamSignals[j] in re.split('! | " " | @ | # | $ | % | * | &',messages[i][0].lower())):
                print( messages[i][0].split(" "),spamSignals[j])
                fault += 1
                if  spamSignals[j] not in spam.split(" "):
                    spam = spam + " " +spamSignals[j]
                j = len(spamSignals)
            j += 1
        i += 1
        
    if (count/dim) * 100 > 90:
        ans[0] = fail + str(count) +"/" + str(dim)
    failed = fail
    flag = False
    for k,v in message.items(): 
        if (v/dim) * 100 > 50:
            flag = True
            failed += str(k)
    if(flag):
        ans[2] = failed
    print(fault)       
    if(fault/dim) * 100 > 50:
        ans[3] = fail + fault
        
        
    return ans


messages = [["Sale today!", "2837273"],
            ["Unique offer!", "3873827"],
            ["Only today and hey hey hey", "2837273"],
            ["Sale today!", "2837273"],
            ["Unique offer!", "3873827"]]

spamSignals = ["sale", "discount", "offer"]
print(spamDetection(messages, spamSignals))
            