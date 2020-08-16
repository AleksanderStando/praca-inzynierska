import csv

def save_transform(coeffs, filename):
    cA = coeffs[0]
    coeffs = coeffs[1:]
    with open(filename + ".csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['Approx coeff'] + cA)
        levels = len(coeffs)
        for i in range(levels):
            writer.writerow(['Detail coeff ' + str(levels-1-i)] + coeffs[i])
