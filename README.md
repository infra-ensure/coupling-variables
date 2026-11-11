# Infra-Ensure coupling variables

IAMC variable definitions for the Infra-Ensure model coupling, in the
[nomenclature](https://nomenclature-iamc.readthedocs.io/en/stable/) format.

The variables are evaluated from PyPSA-AT results by
`pypsa_validation_processing`. They are not part of the common definitions of
[energy-scenarios-at-workflow](https://github.com/iiasa/energy-scenarios-at-workflow),
so they live in this repository (OQ-33 in `pypsa_validation_processing/specs/open_questions.md`).

## Layout
| Path | Content |
|---|---|
| `definitions/variable/` | variable codelists (`*.yaml`) |
| `definitions/region/` | region codelists (`*.yaml`) |
| `tests/` | checks that the definitions load with `nomenclature.DataStructureDefinition` |

## Usage
```bash
pixi run validate   # nomenclature validate-project
pixi run test       # pytest
```

In `pypsa_validation_processing`, set `definitions_path` to this repository's
`definitions/` folder.

## Status
Draft. The price variables are taken from the reviewed specs in
`pypsa_validation_processing/specs/variables/Price__Final_Energy__Industry__*.md`;
the rest of the variables is specified in a definition session.
