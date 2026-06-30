# N-Gram Draft Speculative Decoding for CPU Greedy Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-draft-speculative-decoding-for-cpu-greedy-inference-28869c612f81`
Run ID: `n-gram-draft-speculative-decoding-for-cpu-greedy-inference-28869c612f81-20260529T131610946805+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/6788e13f97b2

## What looked useful

Best trace rows produced 15.991x target-call reduction on repeated paragraphs and 10.601x on structured records, with dense-proxy estimated speedups of 3.974x and 2.635x respectively. Random ASCII showed no useful benefit, and prompt-like text required shorter drafts for only a 1.413x proxy speedup.

## Boundaries and scale limits

No real transformer model, KV-cache implementation, BPE tokenization, production inference runtime, or full wall-clock CPU serving benchmark was run. Evidence is limited to byte-token traces and a NumPy dense-operation proxy under one short CPU-worker run.

## Claim scope

Trace-level exact replay and dense CPU proxy indicate n-gram drafting can accelerate greedy decoding only for repetitive or template-like output streams with high suffix-copy acceptance.

## Why it stopped

Proxy-only evidence supports a workload-sensitive mechanism but does not validate production CPU greedy inference speedups.

## Recommended next action

Stop this run as no-paper useful signal; the concrete next test is a bounded direct implementation in a small CPU transformer runtime comparing exact greedy baseline against n-gram drafted verification on identical generated outputs.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU Transformer N-Gram Draft Verification Benchmark
- Success threshold: At least 1.2x median wall-clock speedup on repetitive/template prompts with exact output equality and no more than 5% slowdown on low-repetition controls.
- Stop condition: Stop if exact output equality fails, if verifier integration cannot batch draft-token positions, or if median speedup remains below 1.1x on the favorable prompt class.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-draft-speculative-decoding-for-cpu-greedy-inference-28869c612f81`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
