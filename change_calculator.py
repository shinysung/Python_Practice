# To calculate how to give the change


def calculate_change(payment, cost):
    change = payment - cost

    fifty_cnt = change // 50000 # number of 50000 won
    ten_cnt = (change % 50000) // 10000 # number of 10000 won
    five_cnt = (change % 10000) // 5000 # number of 5000 won
    one_cnt = (change % 5000) // 1000 # number of 1000 won

    return "50000 won : {}\n10000 won : {}\n5000 won: {}\n1000 won : {}\n".format(fifty_cnt, ten_cnt, five_cnt, one_cnt)


payment = int(input("How much does the customer pay? "))
cost = int(input("How much does the item cost? "))
print(calculate_change(payment, cost))