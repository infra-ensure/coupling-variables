# CLAUDE.md

**Owner:** Max Nutz, BOKU University
**Language:** English

This repository holds the IAMC variable definitions for the Infra-Ensure
coupling in nomenclature format. It is consumed by `pypsa_validation_processing`
(`../pypsa_validation_processing`) via `definitions_path`.

## Background
- OQ-33 in `../pypsa_validation_processing/specs/open_questions.md`: the
  coupling variables are not in the common definitions of energy-scenarios-at-workflow.
  Until this repository is imported there, `pypsa_validation_processing` runs
  them with `definitions_path: false` (no unit conversion).
- Variable specs (source of descriptions and units):
  `../pypsa_validation_processing/specs/variables/`.
- Unit for prices: `EUR_2020/MWh` (OQ-34). Scope of the price variables: OQ-35.

## Conventions
- Variable names follow https://docs.ece.iiasa.ac.at/standards/variables.html.
- Every variable has `description` and `unit`; units must be parseable by `iam_units`.
- Reference the GitHub issue of `pypsa_validation_processing` in the description (`(#99)`).
- One file per variable family in `definitions/variable/` (e.g. `price.yaml`).
- Regions: only `Austria` so far (same as the common definitions, OQ-2).

## Checks
- `pixi run validate` and `pixi run test` must pass before every commit.

## Forbidden actions
- Do NOT invent variables, units or descriptions; ask the owner.
- Do NOT edit `../pypsa_validation_processing` from this repository.
