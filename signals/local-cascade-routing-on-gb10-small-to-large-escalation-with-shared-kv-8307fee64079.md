# Local cascade routing on GB10: small-to-large escalation with shared KV

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `local-cascade-routing-on-gb10-small-to-large-escalation-with-shared-kv-8307fee64079`
Run ID: `local-cascade-routing-on-gb10-small-to-large-escalation-with-shared-kv-8307fee64079-20260619T193647195462+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/970da9f66e8b

## What looked useful

Shared-KV-compatible escalation is mechanically viable and avoids naive small-then-full recomputation overhead; quality is the limiting factor because the 6-layer early route has only 14.06% argmax agreement with full GPT-2 and +6.10 mean NLL degradation when used broadly.

## Boundaries and scale limits

Single GPU, GPT-2 12-layer model, 64 validation samples, next-token evaluation only, no trained early-exit head, no batched production serving, no separate small/large model interface, no 7B+ validation.

## Claim scope

On a GB10 CUDA worker with GPT-2, a shared-backbone 6-layer early route can populate compatible KV state and escalated inference exactly matches full GPT-2 logits, but entropy-gated routing with an untrained early-exit head does not produce a strong speed/quality frontier on 64 WikiText-2 validation samples.

## Why it stopped

Closed as no-paper useful signal: direct local evidence supports exact shared-KV escalation but falsifies the untrained early-route quality needed for a practical cascade.

## Recommended next action

Run a bounded deepen experiment that trains or calibrates the early-exit head and requires a real speed/quality frontier before considering larger model scale.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train a calibrated GPT-2 early-exit head for shared-KV cascade routing
- Success threshold: Route >= 30% of tokens to the small path with mean NLL delta <= 0.25 nats, >= 95% full-model argmax agreement, and >= 1.2x mean latency speedup versus the manual full baseline.
- Stop condition: Stop if trained/calibrated routing cannot reach 20% small-route fraction while keeping mean NLL delta <= 0.5 nats and argmax agreement >= 90% on the held-out set.

## Evidence references

- Artifact root: `<local-path>/projects/local-cascade-routing-on-gb10-small-to-large-escalation-with-shared-kv-8307fee64079`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
