import json
import glob

def main():
    files = []
    #Iterating through logs and saving to files list
    for file in glob.glob('../logs - Krishna Test/logs/*.json'):
        with open(file, 'r') as f:
            for jsonObj in f:
                logDict = json.loads(jsonObj)
                files.append(logDict)

    #Temp container for each total tally object
    tally = {}
    #Final total tally container
    final_tally = {}
    idx = -1
    
    for log in files:
        idx += 1
        for item in log["logs"]:
            #Adding to current tally container total
            if item["email"] in tally.keys():
                tally[item["email"]] += 1
            else:
                tally[item["email"]] = 1
            #Adding to final_tally total
            if item["email"] in final_tally.keys():
                final_tally[item["email"]] += tally[item["email"]]
            else:
                final_tally[item["email"]] = tally[item["email"]]
        print('log_' + str(idx) + '\n ' + str(tally) + ' \n\n')
        #Saving to output files
        with open('../Output/' + str(idx) + '.json', 'w') as outfile:
            json.dump(tally, outfile)
        #Reset tally container
        tally = {}

    print('log_final \n ' + str(final_tally) + ' \n\n')
    #Saving to output file
    with open('../output.json', 'w') as outfile:
        json.dump(final_tally, outfile)

if __name__ == '__main__':
    main()