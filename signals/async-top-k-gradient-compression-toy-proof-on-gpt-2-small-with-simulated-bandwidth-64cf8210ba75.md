# Async Top-K Gradient Compression Toy Proof on GPT-2-Small with Simulated Bandwidth

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `async-top-k-gradient-compression-toy-proof-on-gpt-2-small-with-simulated-bandwidth-64cf8210ba75`
Run ID: `async-top-k-gradient-compression-toy-proof-on-gpt-2-small-with-simulated-bandwidth-64cf8210ba75-20260620T090252934016+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/09b091fae8ea

## What looked useful

0.1% top-k reduced payload about 250x and could be hidden at 1000 Mbps under measured 59.19 ms compute, but captured only 27.9% mean gradient energy with relative update error near 1.0; 1.0% top-k captured 69.0% energy with about 25x payload reduction but still high update error. One-step stale gradient cosine was -0.0021 on synthetic batches.

## Boundaries and scale limits

Single GB10 host, one process, synthetic token batches, analytic bandwidth simulation, no real network stack, no real text corpus, no multi-worker optimizer dynamics, and only 8 GPT-2-small-shaped steps.

## Claim scope

A local GPT-2-small-shaped synthetic mechanism probe shows that 0.1% to 1.0% top-k gradient payloads can greatly reduce simulated low-bandwidth communication cost versus dense fp16 gradient exchange, but it does not validate distributed convergence.

## Why it stopped

No-paper closure: this synthetic/simulated proxy produced a useful mixed signal but does not provide direct convergence evidence for asynchronous top-k distributed training.

## Recommended next action

Run a bounded two-rank GPT-2-small text-corpus experiment comparing dense synchronous, top-k synchronous, and top-k asynchronous updates for matched token and wall-clock budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Two-rank GPT-2-small async top-k convergence check on real text
- Success threshold: Top-k async reaches validation loss within 5% of dense synchronous at the same token budget and improves bandwidth-limited wall-clock throughput by at least 2x at 100 Mbps without unbounded residual growth.
- Stop condition: Stop early if top-k async validation loss diverges by more than 10% from dense synchronous for two consecutive checkpoints, or if residual norm exceeds 3x current gradient norm after warmup.

## Evidence references

- Artifact root: `<local-path>/projects/async-top-k-gradient-compression-toy-proof-on-gpt-2-small-with-simulated-bandwidth-64cf8210ba75`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
