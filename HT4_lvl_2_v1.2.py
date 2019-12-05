def hello():
    while True:
        Name = input("Enter your name: \n")
        if Name == '':
            break
        else:
            print("Hello! " + Name)

def hello_count():
    n = int(input('Count of ppl? \n'))
    for i in range(n):
        print(input('Enter your names: '))


hello()
hello_count()
