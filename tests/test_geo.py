from src import discover, util
from src.geo import (
    DEFAULT_SUFFIX_COUNTRY,
    DEQAR_COUNTRY_ISO,
    MULTI_SUFFIXES,
    merge_suffix_map,
)


def test_single_source_of_truth():
    # util/discover re-export the consolidated maps (no forked copies).
    assert util.MULTI_SUFFIXES is MULTI_SUFFIXES
    assert discover.DEQAR_COUNTRY_ISO is DEQAR_COUNTRY_ISO
    # Every multi-label default suffix is covered for registrable-base.
    for suffix in DEFAULT_SUFFIX_COUNTRY:
        if suffix.count(".") >= 1:
            assert suffix in MULTI_SUFFIXES, suffix
    assert DEQAR_COUNTRY_ISO["Germany"] == "DE"
    # WHED rotation countries all resolve (OSM/WHED adapters stamp iso2).
    assert DEQAR_COUNTRY_ISO["Senegal"] == "SN"
    assert DEQAR_COUNTRY_ISO["Vietnam"] == "VN"
    assert DEQAR_COUNTRY_ISO["Philippines"] == "PH"
    # Bare Faroe Islands ccTLD (wikidata P856 rows like flsk.fo).
    assert merge_suffix_map({})["fo"] == "FO"


def test_merge_suffix_map_override_wins():
    merged = merge_suffix_map({"edu.cn": "JP", "example": "FR"})
    assert merged["edu.cn"] == "JP"  # override wins over default CN
    assert merged["example"] == "FR"
    assert merged["edu"] == "US"  # default preserved
    assert merge_suffix_map({})["edu"] == "US"
    assert merge_suffix_map(None)["edu"] == "US"
