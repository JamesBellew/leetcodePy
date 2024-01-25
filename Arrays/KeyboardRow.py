class Solution(object):
    def findWords(self, words):
        rows = ["qwertyuiop","asdfghjkl","zxcvbnm"]
        output =[]

        for i in words:
            print(i)
            for l in rows:
                if i[0].lower() in l:
                    print(i, 'in this row:',l)
                    count =0
                    for w in range(len(i)):
                        
                        if i[w].lower() in l.lower():
                            count+=1
                            print("good")
                        else:
                            print('no good')


                        print(count, " <-- count")
                        print(len(i), "length of word")
                        if count == len(i):
                            output.append(i)
        return output



                    




            # for j in range(len(i)):
            #     # we need to finf which row it belongs to
            #     print(i[j])
# Testing the function
solution = Solution()
result = solution.findWords(["Hello","Alaska","Dad","Peace"])
print(result)