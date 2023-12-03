class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = None

def build_trie(tokens):
    root = TrieNode()
    for token, value in tokens:
        node = root
        for char in token:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.value = value
    return root

def crunch(trie_root, input_str):
    nums = []
    index = 0

    while index < len(input_str):
        node = trie_root
        match_length = 0
        matched = False
        
        for char in input_str[index:]:
            if char in node.children:
                node = node.children[char]
                match_length += 1
                if node.value is not None:
                    nums.append(node.value)
                    matched = True
                    break
            else:
                break
        
        index += match_length if matched else 1
        
    if not nums:
        return 0

    return nums[0] * 10 + nums[-1]

def process_line(line, p1_trie, p2_trie):
    return crunch(p1_trie, line), crunch(p2_trie, line)

def main():
    try:
        p1_tokens = [("1", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5), ("6", 6), ("7", 7), ("8", 8), ("9", 9)]
        p2_tokens = p1_tokens + [("one", 1), ("two", 2), ("three", 3), ("four", 4), ("five", 5), ("six", 6), ("seven", 7), ("eight", 8), ("nine", 9)]

        p1_trie = build_trie(p1_tokens)
        p2_trie = build_trie(p2_tokens)

        p1_sum, p2_sum = 0, 0
        for line in sys.stdin:
            line = line.strip()
            p1_result, p2_result = process_line(line, p1_trie, p2_trie)
            p1_sum += p1_result
            p2_sum += p2_result

        print(p1_sum)
        print(p2_sum)

    except Exception as e:
        print(f"Error processing input: {e}")

if __name__ == "__main__":
    import sys
    main()
