


def bestClosingTime(customers: str) -> int:
        counts = []
        y_count, n_count = 0, 0

        for customer in customers:
            counts.append([n_count])
            if customer == "N":
                n_count += 1
        counts.append([n_count])
        
        index = len(counts) - 1

        for customer in customers[::-1]:
            counts[index].append(y_count)
            if customer == "Y":
                y_count += 1
            index -= 1
        counts[index].append(y_count)

        min_loss = float("inf")
        min_index = -1
        
        for index, count in enumerate(counts):
            left_loss = count[0]
            right_loss = count[1]
            if left_loss + right_loss < min_loss:
                min_loss = left_loss + right_loss
                min_index = index
        
        return min_index


if __name__ == "__main__":
     print(bestClosingTime("YYNY"))