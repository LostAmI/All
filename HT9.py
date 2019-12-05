import json

d = {"Dima": 0, "Max": 0}
with open("data.json", "w") as file:
    json.dump(d, file)

with open("data.json", "w") as file:
    json.dump(d, file)


def Kont(score):
    with open("data.json", "r") as file:
        d1 = json.load(file)
    print(d1)
    name = input()
    if name in d1.keys():
        q1 = input("Collect or spend? ")
        if q1 == "Collect":
            d1[name] += 0.1 * score
        else:
            bonus = d1[name]
            d1[name] = (bonus - score) * (bonus - score > 0)
            print("Check")
            s = (score - bonus) * (score - bonus > 0)
    else:
        q2 = input("Want to Reg?")
        if q2 == "Yeap":
            d1[name] -= 0.1 * score
        return score
    with open("data.json", "w") as file:
        json.dump(d1, file)
    return s

print(Kont(200))