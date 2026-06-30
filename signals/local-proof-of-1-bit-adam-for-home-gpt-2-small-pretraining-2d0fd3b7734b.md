# Local proof of 1-bit Adam for home GPT-2-small pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `local-proof-of-1-bit-adam-for-home-gpt-2-small-pretraining-2d0fd3b7734b`
Run ID: `local-proof-of-1-bit-adam-for-home-gpt-2-small-pretraining-2d0fd3b7734b-20260530T063843470557+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/7f71c05face3

## What looked useful

Across three seeds, AdamW reached mean final validation loss 2.1581 while the 1-bit AdamW variant reached 2.4649, 14.2% worse. The 1-bit variant reduced optimizer-state memory by 37.5% but was 14.4% slower. A small LR sweep did not close the gap.

## Boundaries and scale limits

This was not GPT-2-small pretraining, not a full-token-budget run, and not the original distributed 1-bit Adam communication-saving setup. The model was a compact 4-layer GPT proxy, with 300 optimizer steps over three seeds plus a small learning-rate sweep.

## Claim scope

A naive local 1-bit-first-moment AdamW variant for compact GPT byte-level pretraining on TinyShakespeare saved optimizer-state memory but did not match AdamW convergence or throughput in bounded GB10 tests.

## Why it stopped

Early proxy falsification rather than full validation: the tested local 1-bit AdamW-style optimizer saved state memory but produced worse validation loss and lower throughput than AdamW on the controlled GPT pretraining proxy.

## Recommended next action

Stop this run as an early proxy falsification; only revisit if using a fused true bit-packed optimizer and a 50M-125M parameter direct GPT pretraining comparison.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/local-proof-of-1-bit-adam-for-home-gpt-2-small-pretraining-2d0fd3b7734b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
