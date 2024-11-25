import argparse

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--filename", "-f", required=True)
    parser.add_argument("--medals", action="store_true", required=False)
    parser.add_argument("--total", action="store_true", required=False)
    parser.add_argument("--overall", action="store_true", required=False)
    parser.add_argument("--country", required=False, nargs='*')
    parser.add_argument("--noc", required=False)
    parser.add_argument("--year", required=False)
    parser.add_argument("--sport", required=False)
    parser.add_argument("--output", "-o", required=False)
    args = parser.parse_args()
    if args.medals:
        task1(args.output, args.filename, args.country, args.year, args.noc)
    elif args.total:
        task2(args.year, args.filename)


def task1(output, filename, country, year, noc):
    gold = 0
    silver = 0
    bronze = 0
    total = 0
    list_medals = ["Gold", "Silver", "Bronze"]
    counter = 0
    output_file = None
    idx = 0
    print(gold, silver, bronze)
    if output is not None:
        output_file = open(output, "wt")
    with open(filename, "r") as file:
        for line in file:
            data = line.strip().split("\t")
            if (data[6] == country or data[7] == noc) and data[9] == year and data[14] in list_medals:
                medalist = [data[1], data[12], data[14]]
                counter += 1
                total += 1
                if data[14] == list_medals[0]:
                    gold += 1
                if data[14] == list_medals[1]:
                    silver += 1
                if data[14] == list_medals[2]:
                    bronze += 1
                if counter <= 10:
                    first_medalist = ", ".join(medalist)
                    print(f"{first_medalist}")
        print(gold, silver, bronze)
    if output_file is not None:
        idx += 1
        output_file.write(str(idx) + ",".join(data) + "\n")
    if output_file is not None:
        output_file.close()

#  python3 main.py --medals --filename "Olympic Athletes - athlete_events.tsv" --noc CHN --year 1992 --sport Basketball


def task2(year, filename):
    all_medals = {}
    list_medals = ["Gold", "Silver", "Bronze"]
    with open(filename, "r") as file:
        for line in file:
            data = line.strip().split("\t")
            if data[9] == year and data[14] in list_medals:
                if data[6] in all_medals:
                    country_medals = all_medals[data[6]]
                    if data[14] == "Gold":
                        country_medals[0] += 1
                    elif data[14] == "Silver":
                        country_medals[1] += 1
                    elif data[14] == "Bronze":
                        country_medals[2] += 1
                else:
                    all_medals[data[6]] = [0, 0, 0]
                    country_medals = all_medals[data[6]]
                    if data[14] == "Gold":
                        country_medals[0] = 1
                    elif data[14] == "Silver":
                        country_medals[1] = 1
                    elif data[14] == "Bronze":
                        country_medals[2] = 1
    for key in all_medals:
        count = all_medals[key]
        print(f"{key}: {count[0]} - {count[1]} - {count[2]}")

# python3 main.py --total --filename "Olympic Athletes - athlete_events.tsv" --year 1992

if __name__ == '__main__':
    main()

# python3 main.py --medals --filename "Olympic Athletes - athlete_events.tsv" --noc CHN --year 1992 --sport Basketball
# python3 main.py --total --filename "Olympic Athletes - athlete_events.tsv" --year 1992

