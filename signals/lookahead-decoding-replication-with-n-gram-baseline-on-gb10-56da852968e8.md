# Lookahead Decoding Replication With N-Gram Baseline on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `lookahead-decoding-replication-with-n-gram-baseline-on-gb10-56da852968e8`
Run ID: `lookahead-decoding-replication-with-n-gram-baseline-on-gb10-56da852968e8-20260629T153637582357+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f114b7da08bd

## What looked useful

Exact n-gram speculation was workload-sensitive: slower than cached greedy on mixed/default prompts (0.95x, 8.5% draft acceptance) but faster on repetitive structured prompts (1.12x, 21.2% draft acceptance). Upstream LADE could not run on the current Transformers 4.57 API, ran only after pinning Transformers 4.36 and forcing eager attention, compressed decoding steps, but was slower wall-clock than matched eager greedy.

## Boundaries and scale limits

Not a full ICML-scale replication: one small LLaMA-family model, short prompt sets, no MT-bench/HumanEval/XSum/CNN-DM suite, no 7B+ model, no FlashAttention LADE path, and no multi-GPU strong scaling.

## Claim scope

TinyLlama-1.1B-class local GB10 inference using exact greedy decoding, exact n-gram prompt/history speculative verification, and the upstream LookaheadDecoding LADE monkeypatch under a pinned Transformers 4.36 eager-attention compatibility path.

## Why it stopped

Local evidence did not reproduce a wall-clock Lookahead Decoding speedup on GB10; positive n-gram results were limited to repetitive prompts and are insufficient for a paper claim.

## Recommended next action

Stop this run as no-paper useful signal; a bounded follow-up should port or configure LADE for modern SDPA/FlashAttention-compatible inference and retest against the n-gram baseline on larger prompt suites.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Modern Attention LADE Port Versus Exact N-Gram Baseline
- Success threshold: LADE reaches at least 1.2x wall-clock tokens/s over cached greedy and beats exact n-gram speculation on at least two of three prompt suites while preserving deterministic greedy outputs.
- Stop condition: Stop if LADE still requires eager attention or remains below 1.0x cached greedy throughput after one modern-attention compatibility attempt and one parameter sweep.

## Evidence references

- Artifact root: `<local-path>/projects/lookahead-decoding-replication-with-n-gram-baseline-on-gb10-56da852968e8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
