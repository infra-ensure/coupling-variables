"""Check that the definitions folder is readable by nomenclature."""

from pathlib import Path

import nomenclature

DEFINITIONS = Path(__file__).resolve().parents[1] / "definitions"


def test_definitions_are_valid() -> None:
    dsd = nomenclature.DataStructureDefinition(DEFINITIONS)
    assert len(dsd.variable) > 0
    assert "Austria" in dsd.region


def test_every_variable_has_unit_and_description() -> None:
    dsd = nomenclature.DataStructureDefinition(DEFINITIONS)
    for name, code in dsd.variable.items():
        assert code.unit, f"{name} has no unit"
        assert code.description, f"{name} has no description"
