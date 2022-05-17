#!/usr/bin/env python

"""This script counts the numbers of passive suffixes attached to verbs in
     Maori.The verbs going through internal change are not accounted for via
     this script."""

import argparse
import re
import csv

import pynini

from pynini.lib import pynutil
from pynini.lib import rewrite
# from collections import Counter


# The alphabet: https://teara.govt.nz/en/interactive/41063/the-maori-alphabet
# "ng" and "wh" are diagraphs, but we treat them as separete characters."
sigma_star = (
    pynini.union(
        "a",
        "e",
        "i",
        "o",
        "u",
        "h",
        "k",
        "m",
        "n",
        "g"
        "p",
        "r",
        "t",
        "w",
        "ā",
        "ē",
        "ī",
        "ō",
        "ū"
    ).closure().optimize()
)

# Rules for each of the 13 passive suffixes
tia_rule = pynini.concat(sigma_star, pynutil.insert("tia"))
a_rule = pynini.concat(sigma_star, pynutil.insert("a"))
hia_rule = pynini.concat(sigma_star, pynutil.insert("hia"))
ia_rule = pynini.concat(sigma_star, pynutil.insert("ia"))
ina_rule = pynini.concat(sigma_star, pynutil.insert("ina"))
kia_rule = pynini.concat(sigma_star, pynutil.insert("kia"))
mia_rule = pynini.concat(sigma_star, pynutil.insert("mia"))
na_rule = pynini.concat(sigma_star, pynutil.insert("na"))
nga_rule = pynini.concat(sigma_star, pynutil.insert("nga"))
ngia_rule = pynini.concat(sigma_star, pynutil.insert("ngia"))
ria_rule = pynini.concat(sigma_star, pynutil.insert("ria"))
kina_rule = pynini.concat(sigma_star, pynutil.insert("kina"))
tanga_rule = pynini.concat(sigma_star, pynutil.insert("tanga"))

# "tia" rule
assert rewrite.matches("hohou", "hohoutia", tia_rule)
assert not rewrite.matches("arahi", "arahina", tia_rule)
# "a" rule
assert rewrite.matches("ehu", "ehua", a_rule)
assert not rewrite.matches("ato", "atohia", a_rule)
# "hia" rule
assert rewrite.matches("ara", "arahia", hia_rule)
assert not rewrite.matches("arahi", "arahina", hia_rule)
# "ia" rule
assert rewrite.matches("hiko", "hikoia", ia_rule)
assert not rewrite.matches("hirihiri", "hirihiria", ia_rule)
# "ina" rule
assert rewrite.matches("kata", "kataina", ina_rule)
assert not rewrite.matches("kari", "karia", ina_rule)
# "kia" rule
assert rewrite.matches("momoto", "momotokia", kia_rule)
assert not rewrite.matches("momotu", "momotuhia", kia_rule)
# "mia" rule
assert rewrite.matches("nanao", "nanaomia", mia_rule)
assert not rewrite.matches("nati", "natia", mia_rule)
# "na" rule
assert rewrite.matches("ruaki", "ruakina", na_rule)
assert not rewrite.matches("runa", "runaa", na_rule)

# "nga" rule
assert rewrite.matches("kai", "kainga", nga_rule)
# raises an error:
assert not rewrite.matches("kanga", "kangaa", nga_rule)

# "ngia" rule
assert rewrite.matches("waikeri", "waikeringia", ngia_rule)
assert not rewrite.matches("hongi", "hongia", ngia_rule)
# "ria" rule
assert rewrite.matches("takapau", "takapauria", ria_rule)
assert not rewrite.matches("tari", "taria", ria_rule)
# "kina" rule
assert rewrite.matches("hopu", "hopukina", kina_rule)
assert not rewrite.matches("rumaki", "rumakina", kina_rule)

# "tanga" rule
# Raises a Composition Failure error
assert rewrite.matches("hūpana", "hūpanatanga", tanga_rule)
assert not rewrite.matches("ihiihi", "ihiihia", tanga_rule)

# Pairing suffixes with their corresponding rules to loop over.
rule_dict = {
    "tia": tia_rule,
    "a": a_rule,
    "hia": hia_rule,
    "ia": ia_rule,
    "ina": ina_rule,
    "kia": kia_rule,
    "mia": mia_rule,
    "na": na_rule,
    "nga": nga_rule,
    "ngia": ngia_rule,
    "ria": ria_rule,
    "kina": kina_rule,
    "tanga": tanga_rule
}

# I am not sure if using collections.Counter as you initially suggested is
# a better idea than the dictionary below, but I couldn't really figure out how
# to use it.

# suffix_dict = {}

suffix_dict = {
    "tia": 0,
    "a": 0,
    "hia": 0,
    "ia": 0,
    "ina": 0,
    "kia": 0,
    "mia": 0,
    "na": 0,
    "nga": 0,
    "ngia": 0,
    "ria": 0,
    "kina": 0,
    "tanga": 0
}


def main(args: argparse.Namespace) -> None:
    with open(args.input, "r") as source:
        # Do I need to remove the delimiter here since I am using
        # "lemma, passive"?
        # What does the delimiter do there?
        tsv_reader = csv.reader(source, delimiter="\t")

        for lemma, passive in source:
            if rewrite.matches(lemma, passive, tia_rule):
                suffix_dict["tia"] += 1
            if rewrite.matches(lemma, passive, a_rule):
                suffix_dict["a"] += 1
            if rewrite.matches(lemma, passive, hia_rule):
                suffix_dict["hia"] += 1
            if rewrite.matches(lemma, passive, ia_rule):
                suffix_dict["ia"] += 1
            if rewrite.matches(lemma, passive, ina_rule):
                suffix_dict["ina"] += 1
            if rewrite.matches(lemma, passive, kia_rule):
                suffix_dict["kia"] += 1
            if rewrite.matches(lemma, passive, mia_rule):
                suffix_dict["mia"] += 1
            if rewrite.matches(lemma, passive, na_rule):
                suffix_dict["na"] += 1
            if rewrite.matches(lemma, passive, nga_rule):
                suffix_dict["nga"] += 1
            if rewrite.matches(lemma, passive, ngia_rule):
                suffix_dict["ngia"] += 1
            if rewrite.matches(lemma, passive, ria_rule):
                suffix_dict["ria"] += 1
            if rewrite.matches(lemma, passive, kina_rule):
                suffix_dict["kina"] += 1
            if rewrite.matches(lemma, passive, tanga_rule):
                suffix_dict["tanga"] += 1
# Should I have it output the counts on the terminal?
          suffix_dict


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="input Maori TSV file")

# Do I need an output argument?

    # parser.add_argument(
    #     "--output", required=True, help="output Maori file as lemmas"
    # )
    main(parser.parse_args())
