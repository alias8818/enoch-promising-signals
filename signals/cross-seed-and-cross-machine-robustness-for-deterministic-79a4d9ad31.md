# Cross-seed and cross-machine robustness for deterministic CPU puzzle oracle

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cross-seed-and-cross-machine-robustness-for-deterministic-79a4d9ad31`
Run ID: `cross-seed-and-cross-machine-robustness-for-deterministic-79a4d9ad31-20260611T073330110610+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Deterministic CPU Puzzle Suite as Volunteer Training Oracle: enoch://control-plane/projects/deterministic-cpu-puzzle-suite-as-volunteer-training-oracle-4def09468712/runs/deterministic-cpu-puzzle-suite-as-volunteer-training-oracle-4def09468712-20260611T070129385804+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e509d1003508

## What looked useful

Canonical ordering plus deterministic integer generation removed Python hash-seed and multiprocessing nondeterminism, while a fragile set-iteration control varied across all 16 hash seeds. Arithmetic width remained a real portability risk: u32, u48, and u64/unbounded produced different batch digests.

## Boundaries and scale limits

Single host only; cross-machine behavior was proxied with environment/process variation and integer-width profiles, not measured on distinct hardware, OS, libc, or Python builds.

## Claim scope

On one CPU host, a BLAKE2b/integer grid-puzzle oracle was invariant across 256 puzzle seeds, 16 Python hash seeds, and serial/1/2/4-process layouts within each arithmetic profile; it was not invariant across underspecified u32/u48/u64 accumulator profiles.

## Why it stopped

Controlled Tier 1 run produced a mixed useful signal, but the cross-machine claim remains unproven and partially falsified by integer-width profile divergence.

## Recommended next action

Run a bounded two-host validation after fixing the oracle spec to mandate canonical u64 or unbounded arithmetic and byte serialization; stop paper consideration until cross-host digests match exactly.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Two-host fixed-arithmetic validation for deterministic CPU puzzle oracle
- Success threshold: For the fixed arithmetic contract, all stable-oracle batch digests must match exactly across hosts, 16 or more Python hash seeds, and serial/parallel layouts, while the fragile control must show at least two distinct digests.
- Stop condition: Stop as negative for cross-machine robustness if any stable-oracle digest differs after platform metadata and dependency versions are recorded.

## Evidence references

- Artifact root: `<local-path>/projects/cross-seed-and-cross-machine-robustness-for-deterministic-79a4d9ad31`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
