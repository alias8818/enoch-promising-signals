# Speculative decoding with a 2-bit + residual draft on a single gb10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-decoding-with-a-2-bit-residual-draft-on-a-single-gb10-2b91aa0dfd83`
Run ID: `speculative-decoding-with-a-2-bit-residual-draft-on-a-single-gb10-2b91aa0dfd83-20260621T084444116073+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/114ecde8251c

## What looked useful

2-bit alone is too lossy for a useful draft distribution on the tested traces, but preserving exact residuals for the high-probability token region changes acceptance from about 0.36-0.38 to about 0.85 at k=512. Residuals selected by largest quantization error do not help, so the residual mechanism must focus on likely tokens rather than reconstruction error.

## Boundaries and scale limits

This is a logit-trace proxy over 384 total target positions from distilgpt2 and gpt2. It does not implement an independent draft model, non-oracle residual selection, multi-token speculative decoding, or end-to-end throughput measurement.

## Claim scope

On GPT-2-class target-logit traces generated on a single GB10, raw 2-bit logit quantization gives low one-step speculative acceptance, while an oracle residual correcting the top target logits can recover high one-step acceptance at a residual budget of 256-512 logits.

## Why it stopped

Closed as a no-paper useful-signal result because the evidence is a bounded logit-proxy, not a full draft-model or serving-throughput validation.

## Recommended next action

Implement a non-oracle residual predictor or hot-token cache and measure multi-token speculative decoding tokens/second on GB10 against target-only decoding and a standard small draft baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end GB10 speculative decoding with a non-oracle 2-bit residual draft
- Success threshold: At least 1.2x end-to-end tokens/second over target-only decoding with exact output distribution verification and mean accepted draft length above 1.5 tokens.
- Stop condition: Stop if non-oracle residual selection cannot exceed 0.6 mean one-step acceptance or if end-to-end throughput is not faster than target-only decoding after a calibrated small run.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-with-a-2-bit-residual-draft-on-a-single-gb10-2b91aa0dfd83`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
