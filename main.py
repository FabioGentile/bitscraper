import logging
import bitscraper as bs
import os
import json

# region logger
logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s %(name)-12s %(levelname)-8s %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)
# endregion

CATEGORY = "MOT"
SUBCATEGORY = "Euro-obbligazioni"


def test_bitscraper():
    p = bs.BITScraper()
    cat = p.avail_categories
    scat = p.avail_subcategories
    return cat, scat


def test_bitlisting(category, subcategory):
    listing = bs.BITListing(category=category, subcategory=subcategory)
    p = listing.details

    dest_file = os.path.join(".", "tests", f"./tests/BIT_{category}_{subcategory}.json")

    with open(dest_file, "w") as fp:
        json.dump(obj=p, fp=fp, sort_keys=False, indent=4)


def main():
    # cat, scat = test_bitscraper()
    # for i, c in enumerate(cat):
    #     for sc in scat[i]:
    #         print(c, sc)
    #         test_bitlisting(c, sc)

    test_bitlisting(category=CATEGORY, subcategory=SUBCATEGORY)


if __name__ == "__main__":
    main()
