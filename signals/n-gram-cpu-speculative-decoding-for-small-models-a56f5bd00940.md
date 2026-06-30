# N-Gram CPU Speculative Decoding for Small Models

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-cpu-speculative-decoding-for-small-models-a56f5bd00940`
Run ID: `n-gram-cpu-speculative-decoding-for-small-models-a56f5bd00940-20260527T205101056909+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c397c3a251f1

## What looked useful

DistilGPT-2 exact-checked run: 384 generated tokens, 50.3% target-call reduction, 1.29x actual wall-clock speedup. GPT-2 small exact-checked run: 384 generated tokens, 14.1% target-call reduction but 0.87x actual wall-clock speed due to drafting overhead. Tiny smoke: overhead dominates. Pythia probe exposed cache-correctness gap.

## Boundaries and scale limits

Only 2-8 windows per model, 32-384 generated tokens per valid run, one natural-text corpus, Python suffix search, CPU-only PyTorch, greedy decoding only. Pythia-70M compatibility failed exact matching and is excluded from performance claims.

## Claim scope

On local Tiny Shakespeare windows, a CPU n-gram suffix drafter with exact greedy verification produced a real wall-clock speedup for DistilGPT-2 and target-call savings without wall-clock speedup for GPT-2 small; claims are limited to the checked GPT-2-family CPU implementation in this project.

## Why it stopped

Moderate bounded evidence shows a real small-model speedup only for DistilGPT-2 and mixed results elsewhere; the implementation is not broad or robust enough for paper-positive closure.

## Recommended next action

Stop this run as no-paper useful signal; next bounded action is to implement a model-family-correct optimized suffix index and rerun exact checked serving wall-clock on GPT-2, DistilGPT-2, and Pythia across at least two corpora.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Optimized exact n-gram CPU speculation across small LM families
- Success threshold: Exact greedy equivalence on every checked window and geometric-mean actual wall-clock speedup above 1.10x over cached greedy baselines across at least two validated model/corpus pairs.
- Stop condition: Stop as negative if exact greedy equivalence fails for any target model after cache repair, or if optimized suffix lookup still leaves geometric-mean wall speedup at or below 1.00x on validated runs.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-cpu-speculative-decoding-for-small-models-a56f5bd00940`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
