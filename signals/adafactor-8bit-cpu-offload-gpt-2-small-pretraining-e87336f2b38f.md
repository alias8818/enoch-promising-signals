# AdaFactor-8bit-CPU-Offload GPT-2-Small Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adafactor-8bit-cpu-offload-gpt-2-small-pretraining-e87336f2b38f`
Run ID: `adafactor-8bit-cpu-offload-gpt-2-small-pretraining-e87336f2b38f-20260525T140751452441+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/7cb06f40219f

## What looked useful

The memory mechanism works at GPT-2-small parameter scale, but the prototype pays a material throughput penalty and does not establish pretraining-quality viability.

## Boundaries and scale limits

Synthetic random-token benchmark only; 20 optimizer steps; batch size 1; no real corpus, validation perplexity, long-horizon stability, checkpoint restart, distributed training, or learning-rate tuning.

## Claim scope

On a GB10 host, a prototype CPU-resident 8-bit factored AdaFactor optimizer is runnable for GPT-2-small-class synthetic next-token updates and reduces serialized optimizer-state storage by about 1540x versus PyTorch AdamW in a 20-step, 1024-token-context benchmark, while reaching about 47.7% of AdamW throughput.

## Why it stopped

Proxy-only systems feasibility result: optimizer state and throughput were directly tested, but real pretraining convergence was not.

## Recommended next action

Stop this run as no-paper useful-signal evidence; the next bounded test should train GPT-2-small on a real text corpus for a fixed small token budget and compare validation perplexity, throughput, memory, and checkpoint restart behavior against AdamW.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus GPT-2-small CPU8 AdaFactor convergence probe
- Success threshold: CPU8 factored AdaFactor reaches validation loss or perplexity within 5% of AdamW at the same token budget while retaining at least 100x lower optimizer-state storage and no restart failure.
- Stop condition: Stop if CPU8 factored AdaFactor diverges, is more than 10% worse in validation perplexity after the agreed token budget, or its throughput falls below 25% of AdamW without a compensating memory-constrained use case.

## Evidence references

- Artifact root: `<local-path>/projects/adafactor-8bit-cpu-offload-gpt-2-small-pretraining-e87336f2b38f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
