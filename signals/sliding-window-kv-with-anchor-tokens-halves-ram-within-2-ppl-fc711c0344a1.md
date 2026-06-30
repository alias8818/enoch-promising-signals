# Sliding-window KV with anchor tokens halves RAM within 2% ppl

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sliding-window-kv-with-anchor-tokens-halves-ram-within-2-ppl-fc711c0344a1`
Run ID: `sliding-window-kv-with-anchor-tokens-halves-ram-within-2-ppl-fc711c0344a1-20260629T122612514337+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/218ac87ce6e2

## What looked useful

Pure sliding-window KV degraded distilgpt2 aggregate PPL by +593.6%, while adding 8 prefix anchors restored aggregate PPL to -0.81% versus full KV at exactly 50% estimated KV-memory reduction. This supports the anchor mechanism but not the broad claim.

## Boundaries and scale limits

Not a paper-ready broad validation: one small GPT-2-class model, short contexts, embedded nonstandard corpus, no GPU serving telemetry, no long-context 1k-4k evaluation, and 1 of 2 sequences exceeded the +2% per-sequence PPL threshold.

## Claim scope

Bounded CPU direct-inference probe: distilgpt2 on 2 embedded public-domain text sequences of 128 targets each. Anchor-plus-sliding KV with 8 prefix anchors and a 56-token recent window exactly halved estimated KV bytes and achieved aggregate PPL within 2% of full KV.

## Why it stopped

No-paper useful signal: local direct evidence supports the mechanism on aggregate, but the run is too small and has a per-sequence threshold miss, so it is not a full validation.

## Recommended next action

Run a bounded deepen follow-up on GPT-2-small or larger over a standard held-out corpus with 1k-4k token contexts, requiring aggregate PPL within +2% and at least 95% of documents within +2% while retaining no more than 50% of KV tokens.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Standard-corpus GPT-2 validation of anchor-plus-sliding KV
- Success threshold: Anchor-plus-sliding retains no more than 50% of full KV tokens, aggregate PPL delta is <= +2%, and at least 95% of evaluated documents have per-document PPL delta <= +2%; pure sliding should be reported as the control regardless of outcome.
- Stop condition: Stop as negative if anchor-plus-sliding exceeds +2% aggregate PPL or more than 5% of documents exceed +2% at the 50% KV-token cap, or if the required context/model scale cannot run within the assigned bounded compute budget.

## Evidence references

- Artifact root: `<local-path>/projects/sliding-window-kv-with-anchor-tokens-halves-ram-within-2-ppl-fc711c0344a1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
