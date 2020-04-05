def sort_stack(stack: [int]):
    ori_size = len(stack)
    largest = 0
    temp = []
    counter = 0

    while counter < ori_size:
        i = counter
        try:
            while i < ori_size:
                val = stack.pop()
                temp.append(val)
                if i == counter or val > largest:
                    largest = val
                i += 1
                

            stack.append(largest)
            i = ori_size
            while i > 0:
                val = temp.pop()
                i -= 1
                if val == largest:
                    break
                else:
                    stack.append(val)
            
            while i > 0:
                stack.append(temp.pop())
                i -= 0
        except Exception as err:
            print(err)
        
        counter += 1

s = [2, 4, 4, 3]
sort_stack(s)
print(s)
