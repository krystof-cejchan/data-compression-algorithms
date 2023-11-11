class Nodes:
    def __init__(self, prob, symbol, left=None, right=None):
        self.prob = prob
        self.symbol = symbol
        self.left = left
        self.right = right
        self.code = ''


def CalculateProbability(d):
    the_symbols = dict()
    for item in d:
        if the_symbols.get(item) is None:
            the_symbols[item] = 1
        else:
            the_symbols[item] += 1
    return the_symbols


the_codes = dict()


def CalculateCodes(node, value=''):
    # a huffman code for current node
    newValue = value + str(node.code)

    if node.left:
        CalculateCodes(node.left, newValue)
    if node.right:
        CalculateCodes(node.right, newValue)

    if not node.left and not node.right:
        the_codes[node.symbol] = newValue

    return the_codes


def OutputEncoded(d, coding):
    encodingOutput = []
    for element in d:
        # print(coding[element], end = '')
        encodingOutput.append(coding[element])

    the_string = ''.join([str(item) for item in encodingOutput])
    return the_string


def TotalGain(d, coding):
    # total bit space to store the data before compression
    beforeCompression = len(d) * 8
    afterCompression = 0
    the_symbols = coding.keys()
    for symbol in the_symbols:
        the_count = d.count(symbol)
        # calculating how many bit is required for that symbol in total
        afterCompression += the_count * len(coding[symbol])
    print("Space usage before compression (in bits):", beforeCompression)
    print("Space usage after compression (in bits):", afterCompression)


def HuffmanEncoding(d):
    symbolWithProbs = CalculateProbability(d)
    the_symbols = symbolWithProbs.keys()
    the_probabilities = symbolWithProbs.values()
    print("symbols: ", the_symbols)
    print("probabilities: ", the_probabilities)

    the_nodes = []

    for symbol in the_symbols:
        the_nodes.append(Nodes(symbolWithProbs.get(symbol), symbol))

    while len(the_nodes) > 1:
        the_nodes = sorted(the_nodes, key=lambda x: x.prob)

        right = the_nodes[0]
        left = the_nodes[1]

        left.code = 0
        right.code = 1

        newNode = Nodes(left.prob + right.prob, left.symbol + right.symbol, left, right)

        the_nodes.remove(left)
        the_nodes.remove(right)
        the_nodes.append(newNode)

    huffmanEncoding = CalculateCodes(the_nodes[0])
    print("symbols with codes", huffmanEncoding)
    TotalGain(d, huffmanEncoding)
    encodedOutput = OutputEncoded(d, huffmanEncoding)
    return encodedOutput, the_nodes[0]


def HuffmanDecoding(encodedData, huffmanTree):
    treeHead = huffmanTree
    decodedOutput = []
    for x in encodedData:
        if x == '1':
            huffmanTree = huffmanTree.right
        elif x == '0':
            huffmanTree = huffmanTree.left
        try:
            if huffmanTree.left.symbol is None and huffmanTree.right.symbol is None:
                pass
        except AttributeError:
            decodedOutput.append(huffmanTree.symbol)
            huffmanTree = treeHead

    string = ''.join([str(item) for item in decodedOutput])
    return string


# the_data = "AAAAAAABBCCCCCCDDDEEEEEEEEE"
# print(the_data)
# encoding, the_tree = HuffmanEncoding(the_data)
# print("Encoded output", encoding)
# print("Decoded Output", HuffmanDecoding(encoding, the_tree))
