
import matplotlib.pyplot as plt
from collections import Counter

def getInput():
    referenceString = list(input("참조열 입력(EX. ABADCBBDACADDABC) : "))
    maxFrameSize = input("1부터 X까지의 프레임 사이즈 : ")

    return referenceString, maxFrameSize


def fifo(referenceString, frameSize):
    frame = []
    pageFaults = 0
    pageHits = 0

    for page in referenceString:
        if page not in frame:
            if len(frame) < frameSize:
                frame.append(page)
            else:
                frame.pop(0)
                frame.append(page)
            pageFaults += 1
        else:
            pageHits += 1

    pageFaultRate = pageFaults / len(referenceString)

    return pageFaultRate, pageHits, pageFaults




def lru(referenceString, frameSize):
    frame = []
    recentUse = {}
    pageFaults = 0
    pageHits = 0

    for i, page in enumerate(referenceString):
        if page not in frame:
            if len(frame) < frameSize:
                frame.append(page)
            else:
                leastRecentlyUsed = min(recentUse, key=recentUse.get)
                frame.remove(leastRecentlyUsed)
                del recentUse[leastRecentlyUsed]
                frame.append(page)
            pageFaults += 1
        else:
            pageHits += 1

        recentUse[page] = i

    pageFaultRate = pageFaults / len(referenceString)

    return pageFaultRate, pageHits, pageFaults


def lfu(referenceString, frameSize):
    frame = []
    pageFrequency = Counter()
    pageFaults = 0
    pageHits = 0

    for page in referenceString:
        pageFrequency[page] += 1
        if page not in frame:
            if len(frame) < frameSize:
                frame.append(page)
            else:
                leastFrequentlyUsed = min(frame, key=pageFrequency.get)
                frame.remove(leastFrequentlyUsed)

                frame.append(page)
            pageFaults += 1
        else:
            pageHits += 1

    pageFaultRate = pageFaults / len(referenceString)

    return pageFaultRate, pageHits, pageFaults



def mfu(referenceString, frameSize):
    frame = []
    pageFrequency = Counter()
    pageFaults = 0
    pageHits = 0

    for page in referenceString:
        pageFrequency[page] += 1
        if page not in frame:
            if len(frame) < frameSize:
                frame.append(page)
            else:
                mostFrequentlyUsed = max(frame, key=pageFrequency.get)
                frame.remove(mostFrequentlyUsed)

                frame.append(page)
            pageFaults += 1
        else:
            pageHits += 1

    pageFaultRate = pageFaults / len(referenceString)

    return pageFaultRate, pageHits, pageFaults



def pageReplacement(algorithm, referenceString, frameSize):
    if algorithm == 'FIFO':
        return fifo(referenceString, frameSize)
    elif algorithm == 'LRU':
        return lru(referenceString, frameSize)
    elif algorithm == 'LFU':
        return lfu(referenceString, frameSize)
    elif algorithm == 'MFU':
        return mfu(referenceString, frameSize)
    else:
        print("잘못된 입력입니다.")
        return None




def main():
    referenceString, maxFrameSize = getInput()

    algorithms = ['FIFO', 'LRU', 'LFU', 'MFU']
    frameSizes = list(range(1, int(maxFrameSize) + 1))
    results = {}

    for algorithm in algorithms:
        pageFaultRates = []
        pageHitsList = []
        pageFaultsList = []

        for frameSize in frameSizes:
            pageFaultRate, pageHits, pageFaults = pageReplacement(algorithm, referenceString, frameSize)

            if pageFaultRate is not None:
                pageFaultRates.append(pageFaultRate)
                pageHitsList.append(pageHits)
                pageFaultsList.append(pageFaults)

        results[algorithm] = {'pageFaultRates': pageFaultRates, 'pageHits': pageHitsList, 'pageFaults': pageFaultsList}

    for algorithm in algorithms:
        print(f"Algorithm: {algorithm}")
        print()

        for i, frameSize in enumerate(frameSizes):
            print(f"Frame Size: {frameSize}")
            print(f"Page Fault Rate: {results[algorithm]['pageFaultRates'][i]}")
            print(f"Page Hits: {results[algorithm]['pageHits'][i]}")
            print(f"Page Faults: {results[algorithm]['pageFaults'][i]}")
            print(" = = = = = = = = = =")

    for algorithm in algorithms:
        plt.plot(frameSizes, results[algorithm]['pageFaultRates'], label=algorithm)

    plt.title('Page Fault Rates by Frame Size')
    plt.xlabel('Frame Size')
    plt.ylabel('Page Fault Rate')
    plt.legend()
    plt.xticks(range(1, max(frameSizes) + 1))
    plt.yticks([i/10 for i in range(11)])  
    plt.ylim([0, 1.1]) 
    plt.savefig('page_fault_rates.png')
    plt.show()

    plt.clf() 

    for algorithm in algorithms:
        plt.plot(frameSizes, results[algorithm]['pageHits'], label=algorithm)

    plt.title('Page Hits by Frame Size')
    plt.xlabel('Frame Size')
    plt.ylabel('Page Hits')
    plt.legend()
    plt.xticks(range(1, max(frameSizes) + 1))
    plt.savefig('page_hits.png')


    plt.clf() 

    for algorithm in algorithms:
        plt.plot(frameSizes, results[algorithm]['pageFaults'], label=algorithm)

    plt.title('Page Faults by Frame Size')
    plt.xlabel('Frame Size')
    plt.ylabel('Page Faults')
    plt.legend()
    plt.xticks(range(1, max(frameSizes) + 1))
    plt.savefig('page_faults.png')


if __name__ == "__main__":
    main()
