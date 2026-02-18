

def generate_report(counts: dict[str, dict], total: int):
    for dimension, values in counts.items():
        print(f"{dimension}:")
        sorted_items = sorted(values.items(), key=lambda x: x[1], reverse=True)
        for value, count in sorted_items:
            percentage = (count / total) * 100
            print(f"{value} {percentage:.2f}%")
        print()