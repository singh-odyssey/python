# remove given word from a list 

demo = ["hi","hola", "konichiwa", "Bounjour"]

def remove():
    if 'hi' in demo:
        print("before removing  ")
        print(demo)
        demo.remove('hi')
        print("Word removed successfully ")
        print(demo);
remove()