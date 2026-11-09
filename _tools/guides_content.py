"""All guides, in the order they appear on /guides/. Each guide's text is in _tools/guides/."""
from guides import (
    used_car_checks,
    write_offs,
    clocking,
    tax_and_mot,
    clean_air,
    service_history,
    mot_history,
)

GUIDES = [
    used_car_checks.GUIDE,
    write_offs.GUIDE,
    clocking.GUIDE,
    tax_and_mot.GUIDE,
    mot_history.GUIDE,
    clean_air.GUIDE,
    service_history.GUIDE,
]
