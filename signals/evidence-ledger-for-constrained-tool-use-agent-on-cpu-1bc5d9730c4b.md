# Evidence ledger for constrained tool-use agent on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-for-constrained-tool-use-agent-on-cpu-1bc5d9730c4b`
Run ID: `evidence-ledger-for-constrained-tool-use-agent-on-cpu-1bc5d9730c4b-20260607T202312191671+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/69fa459122a8

## What looked useful

The ledger reduced wrong-answer rate from 0.2174 to 0.0044 in low noise, 0.5523 to 0.0616 in mixed noise, and 0.9684 to 0.0550 under adversarial primary tools versus the first-answer baseline, while answer rates fell to 0.5186, 0.1283, and 0.1610 respectively.

## Boundaries and scale limits

Evidence is synthetic and structured; no real LLM planning, natural-language extraction, external APIs, human audit scoring, or calibrated-prior ablation was tested. Runs used five 5,000-episode seeds plus one 10,000-episode seed on a single CPU process.

## Claim scope

In a synthetic CPU-only structured lookup benchmark with noisy and adversarial constrained tools, a provenance-weighted evidence ledger reduced wrong answered claims and improved selective accuracy, but did not improve total accuracy because it abstained frequently.

## Why it stopped

No-paper useful signal: the result is a synthetic proxy showing a reliability-coverage tradeoff, not direct evidence that evidence ledgers improve real constrained tool-use agents.

## Recommended next action

Run a bounded real-tool or LLM-agent follow-up that compares ledger versus non-ledger agents on the same tasks with threshold sweeps and no oracle-calibrated reliability priors.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger threshold sweep on real constrained tool-use traces
- Success threshold: Ledger achieves at least a 50% relative reduction in wrong-answer rate versus the best non-ledger baseline while preserving at least 50% answer coverage on held-out real/tool-trace tasks.
- Stop condition: Stop if the ledger cannot maintain at least 50% answer coverage at any threshold that reduces wrong-answer rate by 50%, or if benefits disappear when oracle reliability priors are removed.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-constrained-tool-use-agent-on-cpu-1bc5d9730c4b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
