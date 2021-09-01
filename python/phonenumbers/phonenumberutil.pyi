from re import Pattern
from re import RegexFlag

from .phonemetadata import NumberFormat
from .phonemetadata import PhoneMetadata
from .phonemetadata import PhoneNumberDesc
from .phonenumber import PhoneNumber
from .util import UnicodeMixin

COUNTRY_CODE_TO_REGION_CODE: dict[int, tuple[str, ...]]
_REGEX_FLAGS: RegexFlag
_MIN_LENGTH_FOR_NSN: int
_MAX_LENGTH_FOR_NSN: int
_MAX_LENGTH_COUNTRY_CODE: int
_MAX_INPUT_STRING_LENGTH: int
UNKNOWN_REGION: str
_NANPA_COUNTRY_CODE: int
_COLOMBIA_MOBILE_TO_FIXED_LINE_PREFIX: str
_MOBILE_TOKEN_MAPPINGS: dict[int, str]
_GEO_MOBILE_COUNTRIES_WITHOUT_MOBILE_AREA_CODES: frozenset[int]
_GEO_MOBILE_COUNTRIES: frozenset[int]
_PLUS_SIGN: str
_STAR_SIGN: str
_RFC3966_EXTN_PREFIX: str
_RFC3966_PREFIX: str
_RFC3966_PHONE_CONTEXT: str
_RFC3966_ISDN_SUBADDRESS: str
_ASCII_DIGITS_MAP: dict[str, str]
_ALPHA_MAPPINGS: dict[str, str]
_ALPHA_PHONE_MAPPINGS: dict[str, str]
_DIALLABLE_CHAR_MAPPINGS: dict[str, str]
_ALL_PLUS_NUMBER_GROUPING_SYMBOLS: dict[str, str]
_SINGLE_INTERNATIONAL_PREFIX: Pattern[str]
_VALID_PUNCTUATION: str
_DIGITS: str
_VALID_ALPHA: str
_PLUS_CHARS: str
_PLUS_CHARS_PATTERN: Pattern[str]
_SEPARATOR_PATTERN: Pattern[str]
_CAPTURING_DIGIT_PATTERN: Pattern[str]
_VALID_START_CHAR: str
_VALID_START_CHAR_PATTERN: Pattern[str]
_SECOND_NUMBER_START: str
_SECOND_NUMBER_START_PATTERN: Pattern[str]
_UNWANTED_END_CHARS: str
_UNWANTED_END_CHAR_PATTERN: Pattern[str]
_VALID_ALPHA_PHONE_PATTERN: Pattern[str]
_VALID_PHONE_NUMBER: str
_DEFAULT_EXTN_PREFIX: str

def _extn_digits(max_length: int) -> str: ...
def _create_extn_pattern(for_parsing: bool) -> str: ...

_EXTN_PATTERNS_FOR_PARSING: str
_EXTN_PATTERNS_FOR_MATCHING: str
_EXTN_PATTERN: Pattern[str]
_VALID_PHONE_NUMBER_PATTERN: Pattern[str]
NON_DIGITS_PATTERN: Pattern[str]
_FIRST_GROUP_PATTERN: Pattern[str]
_NP_STRING: str
_FG_STRING: str
_CC_STRING: str
_FIRST_GROUP_ONLY_PREFIX_PATTERN: Pattern[str]

class PhoneNumberFormat:
    E164: int = ...
    INTERNATIONAL: int = ...
    NATIONAL: int = ...
    RFC3966: int = ...

class PhoneNumberType:
    FIXED_LINE: int = ...
    MOBILE: int = ...
    FIXED_LINE_OR_MOBILE: int = ...
    TOLL_FREE: int = ...
    PREMIUM_RATE: int = ...
    SHARED_COST: int = ...
    VOIP: int = ...
    PERSONAL_NUMBER: int = ...
    PAGER: int = ...
    UAN: int = ...
    VOICEMAIL: int = ...
    UNKNOWN: int = ...
    @classmethod
    def values(cls) -> tuple[int, ...]: ...

class MatchType:
    NOT_A_NUMBER: int = ...
    NO_MATCH: int = ...
    SHORT_NSN_MATCH: int = ...
    NSN_MATCH: int = ...
    EXACT_MATCH: int = ...

class ValidationResult:
    IS_POSSIBLE: int = ...
    IS_POSSIBLE_LOCAL_ONLY: int = ...
    INVALID_COUNTRY_CODE: int = ...
    TOO_SHORT: int = ...
    INVALID_LENGTH: int = ...
    TOO_LONG: int = ...

SUPPORTED_REGIONS: set[str]
COUNTRY_CODES_FOR_NON_GEO_REGIONS: set[int]
_NANPA_REGIONS: set[str]

def _regenerate_derived_data() -> None: ...
def _copy_number_format(other: NumberFormat) -> NumberFormat: ...
def _extract_possible_number(number: str) -> str: ...
def _is_viable_phone_number(number: str) -> bool: ...
def _normalize(number: str) -> str: ...
def normalize_digits_only(number: str, keep_non_digits: bool = ...) -> str: ...
def normalize_diallable_chars_only(number: str) -> str: ...
def convert_alpha_characters_in_number(number: str) -> str: ...
def length_of_geographical_area_code(numobj: PhoneNumber) -> int: ...
def length_of_national_destination_code(numobj: PhoneNumber) -> int: ...
def country_mobile_token(country_code: int) -> str: ...
def _normalize_helper(number: str, replacements: dict[str, str], remove_non_matches: bool) -> str: ...
def supported_calling_codes() -> set[int]: ...
def _desc_has_possible_number_data(desc: PhoneNumberDesc | None) -> bool: ...
def _desc_has_data(desc: PhoneNumberDesc | None) -> bool: ...
def _supported_types_for_metadata(metadata: PhoneMetadata) -> set[int]: ...
def supported_types_for_region(region_code: str) -> set[int]: ...
def supported_types_for_non_geo_entity(country_code: int) -> set[int]: ...
def _formatting_rule_has_first_group_only(national_prefix_formatting_rule: str | None) -> bool: ...
def is_number_geographical(numobj: PhoneNumber) -> bool: ...
def is_number_type_geographical(num_type: int, country_code: int) -> bool: ...
def _is_valid_region_code(region_code: str | None) -> bool: ...
def _has_valid_country_calling_code(country_calling_code: int) -> bool: ...
def format_number(numobj: PhoneNumber, num_format: int) -> str: ...
def format_by_pattern(numobj: PhoneNumber, number_format: int, user_defined_formats: list[NumberFormat]) -> str: ...
def format_national_number_with_carrier_code(numobj: PhoneNumber, carrier_code: str) -> str: ...
def format_national_number_with_preferred_carrier_code(numobj: PhoneNumber, fallback_carrier_code: str) -> str: ...
def format_number_for_mobile_dialing(numobj: PhoneNumber, region_calling_from: str, with_formatting: bool) -> str: ...
def format_out_of_country_calling_number(numobj: PhoneNumber, region_calling_from: str) -> str: ...
def format_in_original_format(numobj: PhoneNumber, region_calling_from: str) -> str: ...
def _format_original_allow_mods(numobj: PhoneNumber, region_calling_from: str) -> str: ...
def _raw_input_contains_national_prefix(raw_input: str, national_prefix: str, region_code: str) -> bool: ...
def _has_formatting_pattern_for_number(numobj: PhoneNumber) -> bool: ...
def format_out_of_country_keeping_alpha_chars(numobj: PhoneNumber, region_calling_from: str) -> str: ...
def national_significant_number(numobj: PhoneNumber) -> str: ...
def _prefix_number_with_country_calling_code(country_code: int, num_format: int, formatted_number: str) -> str: ...
def _format_nsn(number: str, metadata: PhoneMetadata, num_format: int, carrier_code: str | None = ...) -> str: ...
def _choose_formatting_pattern_for_number(available_formats: list[NumberFormat], national_number: str) -> NumberFormat | None: ...
def _format_nsn_using_pattern(national_number: str, formatting_pattern: NumberFormat, number_format: int, carrier_code: str | None = ...) -> str: ...
def example_number(region_code: str) -> PhoneNumber | None: ...
def invalid_example_number(region_code: str) -> PhoneNumber | None: ...
def example_number_for_type(region_code: str | None, num_type: int) -> PhoneNumber | None: ...
def _example_number_anywhere_for_type(num_type: int) -> PhoneNumber | None: ...
def example_number_for_non_geo_entity(country_calling_code: int) -> PhoneNumber | None: ...
def _maybe_append_formatted_extension(numobj: PhoneNumber, metadata: PhoneMetadata, num_format: int, number: str) -> str: ...
def _number_desc_by_type(metadata: PhoneMetadata, num_type: int) -> PhoneNumberDesc | None: ...
def number_type(numobj: PhoneNumber) -> int: ...
def _number_type_helper(national_number: str, metadata: PhoneMetadata) -> int: ...
def _is_number_matching_desc(national_number: str, number_desc: PhoneNumberDesc | None) -> bool: ...
def is_valid_number(numobj: PhoneNumber) -> bool: ...
def is_valid_number_for_region(numobj: PhoneNumber, region_code: str) -> bool: ...
def region_code_for_number(numobj: PhoneNumber) -> str | None: ...
def region_code_for_country_code(country_code: int) -> str: ...
def _region_code_for_number_from_list(numobj: PhoneNumber, regions: tuple[str, ...]) -> str | None: ...
def region_codes_for_country_code(country_code: int) -> tuple[str, ...]: ...
def country_code_for_region(region_code: str) -> int: ...
def country_code_for_valid_region(region_code: str) -> int: ...
def ndd_prefix_for_region(region_code: str, strip_non_digits: bool) -> str | None: ...
def is_nanpa_country(region_code: str) -> bool: ...
def is_alpha_number(number: str) -> bool: ...
def is_possible_number(numobj: PhoneNumber) -> bool: ...
def is_possible_number_for_type(numobj: PhoneNumber, numtype: int) -> bool: ...
def _test_number_length(national_number: str, metadata: PhoneMetadata, numtype: int = ...) -> int: ...
def is_possible_number_with_reason(numobj: PhoneNumber) -> int: ...
def is_possible_number_for_type_with_reason(numobj: PhoneNumber, numtype: int) -> int: ...
def is_possible_number_string(number: str, region_dialing_from: str) -> bool: ...
def truncate_too_long_number(numobj: PhoneNumber) -> bool: ...
def _extract_country_code(number: str) -> tuple[int, str]: ...
def _maybe_extract_country_code(number: str, metadata: PhoneMetadata, keep_raw_input: bool, numobj: PhoneNumber) -> tuple[int, str]: ...
def _parse_prefix_as_idd(idd_pattern: Pattern[str], number: str) -> tuple[bool, str]: ...
def _maybe_strip_i18n_prefix_and_normalize(number: str, possible_idd_prefix: str) -> tuple[int, str]: ...
def _maybe_strip_national_prefix_carrier_code(number: str, metadata: PhoneMetadata) -> tuple[str, str, bool]: ...
def _maybe_strip_extension(number: str) -> tuple[str, str]: ...
def _check_region_for_parsing(number: str | None, default_region: str | None) -> bool: ...
def _set_italian_leading_zeros_for_phone_number(national_number: str, numobj: PhoneNumber) -> None: ...
def parse(number: str, region: str | None = ..., keep_raw_input: bool = ..., numobj: PhoneNumber | None = ..., _check_region: bool = ...) -> PhoneNumber: ...
def _build_national_number_for_parsing(number: str) -> str: ...
def _copy_core_fields_only(inobj: PhoneNumber) -> PhoneNumber: ...
def _is_number_match_OO(numobj1_in: PhoneNumber, numobj2_in: PhoneNumber) -> int: ...
def _is_national_number_suffix_of_other(numobj1: PhoneNumber, numobj2: PhoneNumber) -> bool: ...
def _is_number_match_SS(number1: str, number2: str) -> int: ...
def _is_number_match_OS(numobj1: PhoneNumber, number2: str) -> int: ...
def is_number_match(num1: PhoneNumber | str, num2: PhoneNumber | str) -> int: ...
def can_be_internationally_dialled(numobj: PhoneNumber) -> bool: ...
def is_mobile_number_portable_region(region_code: str) -> bool: ...

class NumberParseException(UnicodeMixin, Exception):
    INVALID_COUNTRY_CODE: int = ...
    NOT_A_NUMBER: int = ...
    TOO_SHORT_AFTER_IDD: int = ...
    TOO_SHORT_NSN: int = ...
    TOO_LONG: int = ...
    error_type: int = ...
    def __init__(self, error_type: int, msg: str) -> None: ...
    def __reduce__(self) -> tuple[type[NumberParseException], tuple[int, str]]: ...
    def __unicode__(self) -> str: ...

def _match_national_number(number: str, number_desc: PhoneNumberDesc | None, allow_prefix_match: bool) -> bool: ...
def _match(number: str, pattern: Pattern[str], allow_prefix_match: bool) -> bool: ...
