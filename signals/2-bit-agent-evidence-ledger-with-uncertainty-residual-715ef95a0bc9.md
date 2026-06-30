# 2-bit agent evidence ledger with uncertainty residual

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-agent-evidence-ledger-with-uncertainty-residual-715ef95a0bc9`
Run ID: `2-bit-agent-evidence-ledger-with-uncertainty-residual-715ef95a0bc9-20260608T104914453009+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/f51065dc37c2

## What looked useful

The residual recovered quantization loss in all tested scenarios and replications, reducing Brier by about 0.119, log loss by about 0.335, ECE by about 0.077, and increasing accuracy by about 0.174 versus 2-bit-only. However, a simple signed-vote baseline often performed better and used fewer modeled bits than the float-residual ledger.

## Boundaries and scale limits

The test is synthetic and binary, uses generated LLR-like evidence rather than real agent traces, and the residual is float32, so it is not memory-matched against compact vote/count baselines.

## Claim scope

On synthetic binary claim streams with LLR-like noisy evidence, a 4-state evidence ledger plus a bounded float32 residual consistently improves accuracy and calibration versus the same 4-state ledger without the residual.

## Why it stopped

No-paper useful signal: this was a synthetic proxy showing residual benefit over a weak 2-bit comparator, but not a full validation and not storage-competitive as implemented.

## Recommended next action

Run a bounded memory-matched follow-up with a quantized 2-8 bit residual and a neutral-state 2-bit baseline against signed-vote/count baselines on synthetic and small real agent-trace data.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Memory-matched quantized residual evidence ledger
- Success threshold: At 8 or fewer total bits per claim, residual ledger should beat signed-vote/count baselines on Brier and ECE in at least 80% of synthetic scenarios and not lose more than 1 percentage point of accuracy on the real/semi-real trace benchmark.
- Stop condition: Stop if memory-matched residual variants fail to beat signed-vote/count baselines on Brier or ECE in a majority of synthetic scenarios.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-agent-evidence-ledger-with-uncertainty-residual-715ef95a0bc9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
