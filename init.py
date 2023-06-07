import matplotlib.pyplot as plt
from collections import Counter

def get_input():


    algorithm = input("알고리즘 선택 (FIFO, LRU, LFU, MFU) : ")
    reference_string = list(input("참조열입력(EX. ABCDABACDC) : "))
    frame_size = int(input("프레임 사이즈 : "))

    return algorithm, reference_string, frame_size

def fifo(reference_string, frame_size):

    frame = []
    page_faults = 0
    page_hits = 0
    frame_status = []

    for page in reference_string:
        if len(frame) < frame_size:
            if page not in frame:
                frame.append(page)
                page_faults += 1
            else:
                page_hits += 1
        else:
            if page not in frame:
                frame.pop(0)
                frame.append(page)
                page_faults += 1
            else:
                page_hits += 1

        frame_status.append(list(frame))

    page_fault_rate = page_faults / len(reference_string)

    return {'page_faults': page_faults, 'page_hits': page_hits, 'page_fault_rate': page_fault_rate, 'frame_status': frame_status}

def lru(reference_string, frame_size):

    frame = []
    recent_use = {}
    page_faults = 0
    page_hits = 0
    frame_status = []

    for i, page in enumerate(reference_string):
        if page not in frame:
            if len(frame) < frame_size:
                frame.append(page)
            else:
                least_recently_used = min(recent_use, key=recent_use.get)
                frame.remove(least_recently_used)
                del recent_use[least_recently_used]

                frame.append(page)
            page_faults += 1
        else:
            page_hits += 1
        recent_use[page] = i

        frame_status.append(list(frame))

    page_fault_rate = page_faults / len(reference_string)

    return {'page_faults': page_faults, 'page_hits': page_hits, 'page_fault_rate': page_fault_rate, 'frame_status': frame_status}

def lfu(reference_string, frame_size):

    frame = []
    page_frequency = Counter()
    page_faults = 0
    page_hits = 0
    frame_status = []

    for page in reference_string:
        page_frequency[page] += 1
        if page not in frame:
            if len(frame) < frame_size:
                frame.append(page)
            else:
                least_frequently_used = min(frame, key=page_frequency.get)
                frame.remove(least_frequently_used)
                
                frame.append(page)
            page_faults += 1
        else:
            page_hits += 1

        frame_status.append(list(frame))

    page_fault_rate = page_faults / len(reference_string)

    return {'page_faults': page_faults, 'page_hits': page_hits, 'page_fault_rate': page_fault_rate, 'frame_status': frame_status}

def mfu(reference_string, frame_size):
    frame = []
    page_frequency = Counter()
    page_faults = 0
    page_hits = 0
    frame_status = []

    for page in reference_string:
        page_frequency[page] += 1
        if page not in frame:
            if len(frame) < frame_size:
                frame.append(page)
            else:
                most_frequently_used = max(frame, key=page_frequency.get)
                frame.remove(most_frequently_used)
                
                frame.append(page)
            page_faults += 1
        else:
            page_hits += 1

        frame_status.append(list(frame))

    page_fault_rate = page_faults / len(reference_string)

    return {'page_faults': page_faults, 'page_hits': page_hits, 'page_fault_rate': page_fault_rate, 'frame_status': frame_status}

def page_replacement(algorithm, reference_string, frame_size):

    if algorithm == 'FIFO':
        return fifo(reference_string, frame_size)
    elif algorithm == 'LRU':
        return lru(reference_string, frame_size)
    elif algorithm == 'LFU':
        return lfu(reference_string, frame_size)
    elif algorithm == 'MFU':
        return mfu(reference_string, frame_size)
    else:
        print("wrong input")
        return None


def analyze_result(result, reference_string):
    page_faults = result['page_faults']
    page_hits = result['page_hits']
    page_fault_rate = result['page_fault_rate']

    print("Page Faults: ", page_faults)
    print("Page Hits: ", page_hits)
    print("Page Fault Rate: ", page_fault_rate)

    frame_status = result['frame_status']

    print("Reference String: ", reference_string)

    for i, frames in enumerate(frame_status):
        print(reference_string[i].center(5), "|", " ".join(frames))


def output_result(result, reference_string):

    analyze_result(result, reference_string)
    draw_graph(result)


def draw_graph(result):

    page_faults = result['page_faults']
    page_hits = result['page_hits']
    
    labels = ['Page Faults', 'Page Hits']
    values = [page_faults, page_hits]

    plt.bar(labels, values)
    plt.title("Page Replacement Result")
    plt.show()


def main():
    algorithm, reference_string, frame_size = get_input()
    result = page_replacement(algorithm, reference_string, frame_size)
    if result is not None:
        output_result(result, reference_string)


if __name__ == "__main__":
    main()
