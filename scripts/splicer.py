class Splicer:
    splitCharacters = []
    spliceForPeramiters = False
    
    def __init__(self, splitCharacters, spliceForPeramiters = False):
        self.splitCharacters = splitCharacters
        self.spliceForPeramiters = spliceForPeramiters

    def splice(self, segment):
        return self.spliceCharacter(segment, 0)
    
    def spliceCharacter(self, segment, characterIndex): # recursive method to extract segments of text based on splicers predefined split characters.
        output = []
        # if self.splitCharacters[characterIndex] == " ":
        #     divided = segment.strip()
        # else:
        divided = segment.split(self.splitCharacters[characterIndex])
        # print(divided)
        for i in divided:
            if (divided.index(i) % 2) == 0 and (characterIndex + 1) < len(self.splitCharacters):
                    segment = self.spliceCharacter(i, (characterIndex + 1))
                    # print(segment)
                    for part in segment:
                        # print("Part:", part, type(i))
                        output.append(part)
                    # print("I1:", i, type(i), segment)
            elif i != "":
                output.append(i)
                # print("I2:", i, type(i))

            # if i%2 == 0:
            #     if characterIndex < (len(self.splitCharacters) - 1):
            #         divided[i] = self.spliceCharacter(divided[i], (characterIndex + 1))
            #     # print(divided[i])
            #     if type(divided[i]) == "List":
            #         # print(type(divided[i]))
            #         for x in divided[i]:
            #             if x != "":
            #                 output.append(x)
            #     else:
            #         output.append(divided[0])
            # else:
            #     if type(divided[i]) == "List":
            #         # print(type(divided[i]))
            #         for x in divided[i]:
            #             if x != "":
            #                 output.append(x)
            #     else:
            #         output.append(divided[i])
        return output