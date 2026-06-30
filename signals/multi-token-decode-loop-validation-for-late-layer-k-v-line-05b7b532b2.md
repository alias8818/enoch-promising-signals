# Multi-token decode-loop validation for late-layer K/V linear probe drafts

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `multi-token-decode-loop-validation-for-late-layer-k-v-line-05b7b532b2`
Run ID: `multi-token-decode-loop-validation-for-late-layer-k-v-line-05b7b532b2-20260527T014623165249+0000`

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

- Parent run decision: KV-Cache Linear Probe Drafting: enoch://control-plane/projects/kv-cache-linear-probe-drafting-c7dd87616b44/runs/kv-cache-linear-probe-drafting-c7dd87616b44-20260525T125641553934+0000
- Parent run decision: Direct speculative acceptance for K/V linear probe drafts: enoch://control-plane/projects/direct-speculative-acceptance-for-k-v-linear-probe-drafts-52f5064db3/runs/direct-speculative-acceptance-for-k-v-linear-probe-drafts-52f5064db3-20260526T191451277658+0000

## What looked useful

Trained K/V probes accepted 17-20 tokens per 120 generated tokens while random controls accepted zero, with exact greedy output preserved. Best trained condition was layer 10 draft length 4 with mean acceptance 0.0514, mean wall-clock ratio 0.3545 versus cached greedy, and mean estimated layer-cost speedup 0.6109, below the 1.0 break-even threshold.

## Boundaries and scale limits

Completed fixed-seed runs used 80 train texts, 50 eval texts, 10 generation prompts, 12 generated tokens per prompt, one training epoch, GPT-2 small only, and a random untrained control. Larger planned runs with shuffled-label controls were SIGTERM-terminated before completion.

## Claim scope

On GPT-2 small with Wikitext-2 slices, late-layer K/V linear multi-horizon probes trained on blocks 10 and 11 produce non-random verified accepted draft tokens in an exact greedy speculative decode loop, but do not approach cached greedy throughput or layer-cost break-even.

## Why it stopped

Direct fixed-seed decode-loop validation found a real trained-probe mechanism over random control, but acceptance and speed were far below the threshold needed for practical multi-token speculative decoding.

## Recommended next action

Stop this follow-up as no-paper useful signal; the bounded next test is confidence-gated K/V drafting to see whether abstention can raise accepted-run efficiency enough to approach break-even.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Confidence-gated late-layer K/V probe drafting
- Success threshold: On at least two fixed seeds, gated K/V drafting must preserve exact greedy output, improve accepted tokens per verifier call by at least 2x over ungated probes, and raise estimated layer-cost speedup above 0.8; paper-positive requires exceeding 1.0 and beating cached greedy wall-clock throughput.
- Stop condition: Stop if confidence gating cannot improve estimated layer-cost speedup by at least 20% over ungated probes or if cached greedy wall-clock ratio remains below 0.5 across fixed seeds.

## Evidence references

- Artifact root: `<local-path>/projects/multi-token-decode-loop-validation-for-late-layer-k-v-line-05b7b532b2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
