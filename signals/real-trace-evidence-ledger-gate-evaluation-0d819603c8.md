# Real-trace evidence-ledger gate evaluation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-trace-evidence-ledger-gate-evaluation-0d819603c8`
Run ID: `real-trace-evidence-ledger-gate-evaluation-0d819603c8-20260619T095351534704+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Evidence-ledger gate for agent factual claims: enoch://control-plane/projects/evidence-ledger-gate-for-agent-factual-claims-1a3d0cc0af02/runs/evidence-ledger-gate-for-agent-factual-claims-1a3d0cc0af02-20260619T091656912995+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/32d194b9714d

## What looked useful

The real trace alone failed closure before artifacts existed, while the completed artifact set passed and controlled mutations for missing notes, invalid enum, missing mirror, mirror mismatch, and missing results were rejected.

## Boundaries and scale limits

Single real trace, artifact-level validation only, no corpus-level robustness, no adversarial log testing, and no semantic verification of scientific claims inside notes.

## Claim scope

On one real Codex worker trace from this Enoch project plus controlled artifact mutations, a small evidence-ledger gate enforced required Enoch closure artifacts and rejected missing or invalid closure states.

## Why it stopped

Tier 1 direct test produced mechanism support but not publication-grade or broad validation evidence.

## Recommended next action

Stop as no-paper useful signal; a next bounded deepen test should evaluate the same gate over at least 20 real worker traces with labeled closure states.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Corpus evaluation of real-trace evidence-ledger closure gates
- Success threshold: Zero false positives on invalid closure states and at least 95% recall on valid closure states across at least 20 real traces.
- Stop condition: Stop if any invalid closure mutation passes undetected or if valid closure recall falls below 95% after obvious parser/schema fixes.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-evidence-ledger-gate-evaluation-0d819603c8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
