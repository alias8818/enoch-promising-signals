# Residual-Corrected 2-Bit Speculative Draft Model

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-corrected-2-bit-speculative-draft-model-47cfbdc0bb4f`
Run ID: `residual-corrected-2-bit-speculative-draft-model-47cfbdc0bb4f-20260604T102015335951+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/8f397d98905f

## What looked useful

Sparse residuals were stable but small (+0.23 to +0.76 simulated acceptance percentage points over q2-only). Rank-24 low-rank residual improved simulated acceptance from 0.7125 to 0.7452 at about 3.0 bits/logit, but rank-8 low-rank was worse than q2-only and rank-24 reduced p05 overlap acceptance, indicating residual-tail instability.

## Boundaries and scale limits

No trained transformer draft model, no real text corpus, no end-to-end multi-token speculative serving benchmark, and no measurement of 2-bit kernel unpacking or target-model verification throughput.

## Claim scope

Synthetic transition-distribution proxy for speculative decoding acceptance: 2-bit per-context logit quantization with compact residual correction can improve mean target/draft distribution overlap, but the benefit depends strongly on residual form and budget.

## Why it stopped

No-paper closure: this was a bounded synthetic mechanism proxy with mixed evidence, not full validation of a trained residual-corrected 2-bit speculative draft model.

## Recommended next action

Run a bounded real-LM follow-up: train or adapt a tiny/GPT-2-small-class draft, compare q2-only, sparse residual, and low-rank residual under matched storage and compute budgets, and measure accepted tokens/block plus tokens/sec against a fixed target.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Matched-Budget Real-LM Validation of Residual-Corrected 2-Bit Drafts
- Success threshold: At matched storage/compute, a residual variant improves accepted tokens/block by at least 5% and end-to-end tokens/sec by at least 3% over q2-only while p05 context acceptance is no worse than q2-only by more than 1 percentage point.
- Stop condition: Stop if residual variants fail to improve accepted tokens/block by 2% over q2-only, reduce p05 acceptance by more than 3 percentage points, or lose end-to-end tokens/sec after overhead accounting.

## Evidence references

- Artifact root: `<local-path>/projects/residual-corrected-2-bit-speculative-draft-model-47cfbdc0bb4f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
