# Page Replacement Algorithms

This is a Python program that implements various page replacement algorithms including FIFO, LRU, LFU, and MFU.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/root39293/os-virtual-memory-page-replacement
   ```

2. Install the required dependencies:

    ```bash
    pip install matplotlib
    ```
3. Run the program:

    ```
    python init.py
    ```

## Available Algorithms

- FIFO: First-In-First-Out
- LRU: Least Recently Used
- LFU: Least Frequently Used
- MFU: Most Frequently Used

## Example

```less

알고리즘 선택 (FIFO, LRU, LFU, MFU) : FIFO
참조열 입력(EX. ABCDABACDC) : ABACCABDSAB
프레임 사이즈 : 3

Page Faults: 7
Page Hits: 4
Page Fault Rate: 0.6363636363636364

Reference String: ABACCABDSAB
    A   | A
    B   | A B
    A   | A B
    C   | A B C
    C   | A B C
    A   | A B C
    B   | A B C
    D   | B C D
    S   | C D S
    A   | D S A
    B   | S A B

```


