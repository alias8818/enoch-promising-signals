# Early-Exit Self-Draft Speculative Decoding

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `early-exit-self-draft-speculative-decoding-985f4c9bf404`
Run ID: `early-exit-self-draft-speculative-decoding-985f4c9bf404-20260607T011059509882+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ef1d873df424

## What looked useful

Untuned intermediate exits were too inaccurate or too expensive: best layer-count proxy was 0.800x at layer 3/12 block 1, and best warmed no-cache actual speedup was 0.818x. Deeper layer 9/12 improved accepted tokens per verifier pass to 1.519 at block 8 but predicted only 0.217x speedup.

## Boundaries and scale limits

No trained early-exit heads, no auxiliary losses, no KV-cache-optimized serving implementation, no sampling benchmark, no standard corpus evaluation, and no larger-than-GPT-2-small models were tested. Actual timing is a no-cache Python sanity check; the primary speed claim uses a simple layer-count proxy.

## Claim scope

Bounded GPT-2-small probe of zero-training early-exit self-drafting: applying GPT-2's final layer norm and tied LM head to intermediate hidden states at layers 3, 6, and 9 did not produce break-even exact speculative decoding on 10 fixed prompts and 240 emitted tokens per configuration.

## Why it stopped

Proxy/early falsification of the zero-training mechanism: no tested untuned early-exit configuration reached break-even by layer-count proxy or warmed no-cache timing, so this is not paper-positive and should not be scaled without adding trained exits.

## Recommended next action

Stop this run as an early negative/useful-signal result; if pursuing the idea, run a bounded trained early-exit-head follow-up on GPT-2-small with held-out prompts and the same exact-verification metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train GPT-2-small Early-Exit Heads for Exact Self-Draft Verification
- Success threshold: At least one layer/block configuration must achieve predicted layer-count speedup >= 1.15x and warmed actual no-cache speedup >= 1.05x while preserving exact full-model greedy outputs on held-out prompts.
- Stop condition: Stop if trained heads do not exceed 0.90 exact accepted draft fraction for layer 3 or 0.75 for layer 6 on a validation subset, or if final speculative speed remains below 1.0x.

## Evidence references

- Artifact root: `<local-path>/projects/early-exit-self-draft-speculative-decoding-985f4c9bf404`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
