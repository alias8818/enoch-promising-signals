# Rolling Suffix Buffer Token Recycling for Speculative Draft

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `rolling-suffix-buffer-token-recycling-for-speculative-draft-b3cb91c0184f`
Run ID: `rolling-suffix-buffer-token-recycling-for-speculative-draft-b3cb91c0184f-20260603T235501080961+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/9b0f2019f36a

## What looked useful

Rejected suffix tokens often recur somewhere later in the gpt2/distilgpt2 run, but rarely at the exact immediate positions needed for speculative acceptance. Corrected one-shot recycling cut draft tokens per output token from 1.6758 to 1.3242, but recycled-token acceptance was only 3.71% and target calls per output token rose from 0.2793 to 0.3770.

## Boundaries and scale limits

Small causal LMs, 16 hand-written prompts, 1024 emitted tokens per medium run, greedy decoding only, simple algorithmic proposal-source harness, no production KV-cache, batching, serving latency, sampling, or 7B+ validation.

## Claim scope

On small greedy speculative-decoding probes with distilgpt2/tiny and gpt2/distilgpt2, unguarded rolling suffix-buffer recycling reduces draft-model token generation but yields very low recycled-token acceptance and worsens target-call efficiency for the plausible small draft/target pair.

## Why it stopped

Proxy/direct small-model evidence is a useful early falsification of the unguarded recycling hypothesis, not a full validation of all gated or production-scale variants.

## Recommended next action

Stop the unguarded FIFO suffix-buffer variant; only revisit with a bounded context-aware gating experiment that must preserve target-call efficiency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Context-aware gate for recycled speculative suffix tokens
- Success threshold: At least 10% draft-token reduction with recycled-token acceptance >=25% and target calls per output token no more than 5% above baseline on the gpt2/distilgpt2 probe.
- Stop condition: Stop if recycled-token acceptance remains below 10% or target calls per output token exceed baseline by more than 10% after implementing the gate.

## Evidence references

- Artifact root: `<local-path>/projects/rolling-suffix-buffer-token-recycling-for-speculative-draft-b3cb91c0184f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
