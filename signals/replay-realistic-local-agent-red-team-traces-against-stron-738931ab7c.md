# Replay Realistic Local-Agent Red-Team Traces Against Stronger Baselines

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `replay-realistic-local-agent-red-team-traces-against-stron-738931ab7c`
Run ID: `replay-realistic-local-agent-red-team-traces-against-stron-738931ab7c-20260531T220011564440+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Red-Team Ledger Replay for Local Agent Safety: enoch://control-plane/projects/red-team-ledger-replay-for-local-agent-safety-dec735b5b53d/runs/red-team-ledger-replay-for-local-agent-safety-dec735b5b53d-20260531T170500929985+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/6fcd819485b5

## What looked useful

The parent replay mechanism remains effective, but the incremental advantage disappears once a whole-trace trained baseline is included. Future tests must include stronger whole-trace controls and held-out attack families before claiming replay-specific value.

## Boundaries and scale limits

Generated trace families, scenario-defined labels, train/test variants drawn from the same scenario families, no live LLM agent or production trace capture.

## Claim scope

On a deterministic Tier 1 corpus of 800 held-out realistic local-agent red-team traces, append-only temporal replay did not improve detection over a trained whole-trace Naive Bayes baseline; both achieved 100% recall and 0% false-positive rate.

## Why it stopped

Controlled direct follow-up failed the stated incremental-value threshold: ledger replay recall minus best stronger-baseline recall was 0.000 with both at 100% recall and 0% FPR.

## Recommended next action

Run a bounded deepen test using independently authored or captured local-agent red-team traces split by attack family, requiring replay to beat trained whole-trace baselines at matched false-positive rates.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-Out Attack-Family Replay Against Whole-Trace Baselines
- Success threshold: Replay improves unsafe-trace recall by at least 10 absolute percentage points over the best trained whole-trace baseline at FPR <= 5% on held-out attack families.
- Stop condition: Stop if the best trained whole-trace baseline matches or exceeds replay recall at FPR <= 5%, or if replay exceeds 5% FPR after threshold tuning.

## Evidence references

- Artifact root: `<local-path>/projects/replay-realistic-local-agent-red-team-traces-against-stron-738931ab7c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
