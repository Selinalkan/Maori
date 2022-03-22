#!/usr/bin/env python

"""This script splits the column containing the lemma and suffixes of passive Maori verbs extracted from Biggs, Ryan and Te Aka into two tab separated columns the first of which lists the lemmas and the second of which list the corresponding suffix for each lemma."""

import argparse
import re
import csv


def main(args: argparse.Namespace) -> None:
    # this is line 10 lems_and_sufs = []
    # he wants me to open and read
    with open(args.input, "r") as source, open(args.output, "w") as sink:
        tsv_reader = csv.reader(source, delimiter="\t")
        tsv_writer = csv.writer(sink, delimiter="\t")
        for row in tsv_reader:
            matchObj = re.match(r"(\w+)(\-)(\w+)", row[1])
            if matchObj:
                row = [
                    matchObj.group(1),
                    matchObj.group(1) + matchObj.group(3),
                ]
                # write an assertion here
                assert ("aru", "arumia")
                assert not ("aru", "aru-mia")
            else:
                row = [matchObj.group(1), matchObj.group(1)]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="input Maori file")
    parser.add_argument(
        "--output", required=True, help="output Maori file as lemmas"
    )
    main(parser.parse_args())
