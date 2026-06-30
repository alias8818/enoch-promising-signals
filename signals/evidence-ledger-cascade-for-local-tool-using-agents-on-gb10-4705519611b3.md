# Evidence-ledger cascade for local tool-using agents on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-cascade-for-local-tool-using-agents-on-gb10-4705519611b3`
Run ID: `evidence-ledger-cascade-for-local-tool-using-agents-on-gb10-4705519611b3-20260609T235911668733+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/de3914d62c41

## What looked useful

Evidence ledgers are useful versus no ledger, but hard cascade filtering appears to over-prune weak-but-informative evidence. A flat weighted ledger was consistently stronger in paired bootstrap comparisons.

## Boundaries and scale limits

Synthetic traces only; no real LLM transcript extraction, no live tool latency, no model-specific prompt adherence, and no GB10 GPU/model-serving workload. Main run covered 160,000 claim decisions across four noise regimes.

## Claim scope

On a deterministic synthetic benchmark of local tool-use evidence traces, a hard cascade evidence ledger improves accuracy over trusting the newest observation but underperforms a simpler flat weighted evidence ledger across four tested noise regimes.

## Why it stopped

Proxy synthetic evidence does not support the cascade mechanism over the relevant flat-ledger baseline, so this is an early bounded negative rather than a full real-agent validation.

## Recommended next action

Stop this run as a no-paper useful signal; if continuing, run a bounded real-transcript follow-up comparing hard cascade filtering against a soft reliability-calibrated ledger.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-transcript soft ledger versus hard cascade for local tool agents
- Success threshold: Soft reliability-calibrated ledger improves task accuracy or unsupported-claim rate over flat weighted ledger by at least 3 percentage points with a paired 95% confidence interval excluding zero, while hard cascade does not regress accuracy by more than 1 point.
- Stop condition: Stop if hard cascade and soft ledger both fail to beat the flat weighted baseline on real transcripts, or if evidence extraction quality is too poor to score provenance reliably.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-cascade-for-local-tool-using-agents-on-gb10-4705519611b3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
