from typing import Optional

from .phonemetadata import PhoneNumberDesc
from .phonenumber import PhoneNumber

SUPPORTED_SHORT_REGIONS: list[str]

class ShortNumberCost:
    TOLL_FREE: int = ...
    STANDARD_RATE: int = ...
    PREMIUM_RATE: int = ...
    UNKNOWN_COST: int = ...

def _region_dialing_from_matches_number(numobj: PhoneNumber, region_dialing_from: str) -> bool: ...
def is_possible_short_number_for_region(short_numobj: PhoneNumber, region_dialing_from: str) -> bool: ...
def is_possible_short_number(numobj: PhoneNumber) -> bool: ...
def is_valid_short_number_for_region(short_numobj: PhoneNumber, region_dialing_from: str) -> bool: ...
def is_valid_short_number(numobj: PhoneNumber) -> bool: ...
def expected_cost_for_region(short_numobj: PhoneNumber, region_dialing_from: str) -> int: ...
def expected_cost(numobj: PhoneNumber) -> int: ...
def _region_code_for_short_number_from_region_list(numobj: PhoneNumber, region_codes: tuple[str, ...]) -> Optional[str]: ...
def _example_short_number(region_code: str) -> str: ...
def _example_short_number_for_cost(region_code: str, cost: int) -> str: ...
def connects_to_emergency_number(number: str, region_code: str) -> bool: ...
def is_emergency_number(number: str, region_code: str) -> bool: ...
def _matches_emergency_number_helper(number: str, region_code: str, allow_prefix_match: bool) -> bool: ...
def is_carrier_specific(numobj: PhoneNumber) -> bool: ...
def is_carrier_specific_for_region(numobj: PhoneNumber, region_dialing_from: str) -> bool: ...
def is_sms_service_for_region(numobj: PhoneNumber, region_dialing_from: str) -> bool: ...
def _matches_possible_number_and_national_number(number: str, number_desc: Optional[PhoneNumberDesc]) -> bool: ...
