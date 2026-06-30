# INT4 Self-Draft Speculative Decoding on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int4-self-draft-speculative-decoding-on-gb10-28f407a5d101`
Run ID: `int4-self-draft-speculative-decoding-on-gb10-28f407a5d101-20260620T091933566432+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/198a2f451250

## What looked useful

The mechanism is real enough to reduce target forwards, but the simulated INT4 draft path and modest acceptance rate made speculative decoding 3.3x slower than baseline at draft window 4 and 4.1x slower at draft window 8 on GPT-2 small.

## Boundaries and scale limits

The run used GPT-2 small and tiny GPT-2 only, 16-token continuations, greedy decoding, no packed INT4 CUDA kernel, and no KV-cache-optimized speculative verification. It does not evaluate 7B+ models or production serving stacks.

## Claim scope

On GB10 with GPT-2-small-class greedy decoding, a naive PyTorch simulated-INT4 same-model draft preserved exact verifier outputs and reduced verifier forwards, but did not improve end-to-end throughput.

## Why it stopped

Proxy early falsification of the practical speedup claim for the naive simulated-INT4 implementation, not a full validation or global rejection of optimized INT4 self-draft speculative decoding.

## Recommended next action

Stop this run as a no-paper useful signal; only reopen as a bounded deepen test if a native packed INT4 draft kernel and KV-cache-aware verifier harness are available locally.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Native INT4 KV-Cache Self-Draft Decode on GB10
- Success threshold: At least 1.20x end-to-end tokens/s versus fp16 greedy baseline with exact output equivalence, mean acceptance rate above 0.50, and no memory pressure under GB10 no-swap posture.
- Stop condition: Stop as negative if native INT4 window-4 or window-8 remains below 1.0x baseline throughput or if acceptance stays below 0.40 across the prompt set.

## Evidence references

- Artifact root: `<local-path>/projects/int4-self-draft-speculative-decoding-on-gb10-28f407a5d101`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
