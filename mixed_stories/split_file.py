with open ("mix_story","r") as f,\
    open("story_a.txt","a") as f1,\
    open("story_b.txt", "a") as f2:

    for index,line in enumerate(f):
        if index % 2 == 0:
            f1.write(line)

        else:
            f2.write(line)
