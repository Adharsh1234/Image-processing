def find_distacne(point1, point2):
    distacne = abs(point1-point2)
    return distacne


def knn():
    # regration problem=if yes or no question is asked then this problem has no answer
    weight_list = []
    nearest_height = []
    data = [
        [65.75, 112.99],
        [71.52, 136.49],
        [69.40, 153.03],
        [68.22, 142.34],
        [67.79, 144.30],
        [68.70, 123.30],
        [69.80, 141.49],
        [70.01, 136.46],
        [67.90, 112.37],
        [66.49, 127.45],
    ]
    user_input = float(input("Enter your weight: "))
    k = int(input("Enter the accuracy : "))
    for index, weight in enumerate(data):
        # print(index,weight[0])
        d = find_distacne(weight[0], user_input)
        # print(d)
        weight_list.append((d, index))
    # print(weight_list)
    sorted_weight_list = sorted(weight_list)
    # print(sorted_weight_list)
    for i in sorted_weight_list[:k]:
        # print(i[1])
        # print(data[i[1]][1])
        nearest_height.append(data[i[1]][1])
    result=sum(nearest_height)/len(nearest_height)
    print(result)

knn()
