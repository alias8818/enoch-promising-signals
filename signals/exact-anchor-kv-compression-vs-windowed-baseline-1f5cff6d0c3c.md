# Exact-Anchor KV Compression vs Windowed Baseline

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-kv-compression-vs-windowed-baseline-1f5cff6d0c3c`
Run ID: `exact-anchor-kv-compression-vs-windowed-baseline-1f5cff6d0c3c-20260604T044944236412+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/d1eff6718125

## What looked useful

Exact anchors preserve the direction of old-anchor attention outputs, but reduced-cache softmax over-amplifies retained anchors; the tested policy loses MSE vs full attention to a same-slot window across anchor, mixed, random, and recent modes at budgets 256, 512, and 1024.

## Boundaries and scale limits

Synthetic K/V only; no trained language model, no real serving cache, no kernel latency, no natural long-context benchmark, and only simple block-mean compression.

## Claim scope

Bounded synthetic attention-cache policy test at seq_len 4096 comparing equal-slot sliding-window KV against exact old-anchor retention plus block-mean non-anchor compression.

## Why it stopped

Proxy early falsification: exact-anchor plus block-mean compression did not beat the same-slot window on full-attention output MSE in the larger synthetic tests, so this is not a full validation.

## Recommended next action

Stop this policy as a paper candidate; a bounded follow-up should test softmax denominator calibration or learned non-anchor summaries before any real-LM scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated Exact-Anchor KV Compression
- Success threshold: Calibrated exact-anchor must beat same-slot window on MSE in anchor and mixed modes at seq_len 4096 for at least two of three budgets, without more than 10 percent MSE regression in recent mode.
- Stop condition: Stop if calibration still loses MSE to window in anchor or mixed mode at budget 512, or if it requires full-cache oracle statistics unavailable to a compressed cache.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-kv-compression-vs-windowed-baseline-1f5cff6d0c3c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
