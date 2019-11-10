def parent(test):
    print("This is from parent",test)
    def child1():
        test = ' modified from child'
        print("This is from child func:",test)
        def child2():
            print("This is from child 2",test)
        child2()
    child1()
    print("This is from parent again",test)
    


parent('testing')