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
