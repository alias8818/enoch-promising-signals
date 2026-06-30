# Real-corpus GPT-2-small Adafactor vs AdamW memory-throughput-loss comparison

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-corpus-gpt-2-small-adafactor-vs-adamw-memory-throughp-5b51e7288c`
Run ID: `real-corpus-gpt-2-small-adafactor-vs-adamw-memory-throughp-5b51e7288c-20260610T234641866278+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Adafactor vs AdamW matched-token on GPT-2-small, memory delta: enoch://control-plane/projects/adafactor-vs-adamw-matched-token-on-gpt-2-small-memory-delta-0009a8c399f0/runs/adafactor-vs-adamw-matched-token-on-gpt-2-small-memory-delta-0009a8c399f0-20260610T131611980135+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/021ea2559543

## What looked useful

Adafactor delivered the expected large optimizer-memory reduction for real-corpus GPT-2-small CUDA updates without a short-run throughput or loss penalty in this controlled setting.

## Boundaries and scale limits

Short run only: one corpus, one GPT-2-small checkpoint, one learning rate, one batch/sequence setting, fp32, three seeds, and no validation perplexity or long-horizon convergence measurement. This does not establish publication-grade optimizer superiority or full-scale training behavior.

## Claim scope

In a Tier 1 direct CUDA test, GPT-2-small fine-tuning on WikiText-2 raw text for 3 seeds x 40 measured steps showed Adafactor using 42.0% less CUDA peak allocated memory and 35.3% less reserved memory than AdamW, with similar/slightly higher throughput and lower short-horizon training loss under the tested fp32 batch-size-2 sequence-length-256 setting.

## Why it stopped

Tier 1 direct evidence produced a useful mechanism signal, but the run is too short and narrow for paper-positive claims.

## Recommended next action

Run a bounded deepen follow-up with matched-token GPT-2-small training for thousands of steps, validation perplexity checkpoints, and batch/sequence scaling to test whether the memory saving yields practically larger feasible training configurations.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Longer matched-token GPT-2-small Adafactor vs AdamW validation-perplexity and batch-scaling test
- Success threshold: Adafactor must reduce CUDA peak allocated memory by at least 25%, enable at least one larger feasible batch/sequence configuration, and finish within 2% validation perplexity of AdamW at the same token budget without more than 10% throughput regression.
- Stop condition: Stop if Adafactor loses the memory advantage below 15%, is more than 10% slower at matched settings, or validation perplexity is more than 5% worse than AdamW after the planned matched-token budget.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-gpt-2-small-adafactor-vs-adamw-memory-throughp-5b51e7288c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
