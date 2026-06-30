# N-gram suffix speculative decoding on CPU Proxmox

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-suffix-speculative-decoding-on-cpu-proxmox-908194b64792`
Run ID: `n-gram-suffix-speculative-decoding-on-cpu-proxmox-908194b64792-20260620T053550728874+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ae97c47b70d8

## What looked useful

Best ideal target-call speedups were 3.30x on copy-rich streams, 5.90x on bursty reuse streams, and 7.16x on project-text proxy streams, while the low-overlap random control stayed at 1.00x with zero accepted draft tokens.

## Boundaries and scale limits

Synthetic and project-text proxy streams only; no live LLM verification, no end-to-end CPU serving latency, no tokenizer/model ablation, and cache index lifecycle was naive rather than production optimized.

## Claim scope

Offline CPU proxy shows n-gram/suffix speculative proposals reduce ideal target verification calls only on token streams with exact recurring continuations in prompt/current/prior-request cache.

## Why it stopped

Proxy evidence is useful but not paper-ready; it supports a narrow recurrence mechanism and falsifies a broad arbitrary-workload speedup claim.

## Recommended next action

Run a bounded deepen test with a small real CPU LLM decoder and real input-grounded/agentic traces, comparing greedy latency and accepted tokens against this suffix proposer.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live CPU LLM n-gram suffix speculative decoding on input-grounded traces
- Success threshold: At least 20% median end-to-end decode latency reduction on repetition-rich real traces with no quality divergence from greedy output, and no more than 5% regression on low-overlap controls.
- Stop condition: Stop if integrated suffix speculation yields less than 10% median latency reduction on repetition-rich traces or causes more than 5% low-overlap regression after cache/index overhead is included.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-speculative-decoding-on-cpu-proxmox-908194b64792`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
