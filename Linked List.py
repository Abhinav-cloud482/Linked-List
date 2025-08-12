node2 = {"val": 2, "next": None}
node1 = {"val": 1, "next": node2}
head = node1  

new_head = {"val": 0, "next": head}
head = new_head

current = head
while True:
    if current is not None:
        print(current["val"], end=' ')
        current = current["next"]
    else:
        break

print()

new_tail = {"val": 3, "next": None}
current = head
while True:
    if current["next"] is None:
        current["next"] = new_tail
        break
    else:
        current = current["next"]

current = head
while True:
    if current is not None:
        print(current["val"], end=' ')
        current = current["next"]
    else:
        break
