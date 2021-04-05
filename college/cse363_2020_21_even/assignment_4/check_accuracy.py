import json
# from matplotlib import pyplot as plt

with open("labeled_data_dict.json") as f:
    labeled_data = json.load(f)
    f.close()

with open("saved_result_dict.json") as f:
    result_dict = json.load(f)
    f.close()

correct = 0
total = 0

plot_y = []

for file_name in list(result_dict.keys()):
    if result_dict[file_name] == labeled_data[file_name]:
        correct += 1
    total += 1

    plot_y.append(correct / total)

print("Accuracy %:", 100 * correct / total)

# plt.plot([(i + 1) for i in range(len(plot_y))], plot_y)
# plt.show()
