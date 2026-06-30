# Token-Quality Allocation at Fixed Step Budget

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `token-quality-allocation-at-fixed-step-budget-3b99db719b40`
Run ID: `token-quality-allocation-at-fixed-step-budget-3b99db719b40-20260613T123033570425+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3c2469b6e979

## What looked useful

Fixed-step token-quality allocation is not a one-dimensional more-high-quality-is-always-better rule in this toy setting. Clean high-quality repetition can overfit when the high-quality pool is effectively small, while fresh noisy-but-related examples can provide useful diversity; low-to-high scheduling was best in the longer 1000-step, pool-256 condition.

## Boundaries and scale limits

Evidence is synthetic and small-model only: 2-layer 96-dim transformer, 64-token vocabulary, seq_len 48, 3 seeds per condition, and synthetic clean/noisy quality buckets. It does not validate natural-language corpora, tokenizer effects, dedup strategies, GPT-2-small-class or larger models, or production-scale pretraining.

## Claim scope

In a toy synthetic autoregressive language-modeling task with fixed optimizer steps, fixed model size, and high-quality data represented as a reusable clean pool, the best high/low token-quality allocation depended on both step budget and effective high-quality pool diversity: all-high won at 300 steps with pool size 256, low-to-high won at 1000 steps with pool size 256, and mostly-low won at 1000 steps with pool size 32.

## Why it stopped

No-paper closure: this run produced a reproducible toy useful signal, but the evidence is synthetic and not sufficient for a publication-grade claim about real language-model pretraining.

## Recommended next action

Run a bounded real-corpus GPT-2-small-class follow-up with explicit quality buckets, dedup controls, equal step/token budgets, and the same all-high/mostly-high/balanced/mostly-low/low-to-high/high-to-low schedule grid.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Corpus Fixed-Step Quality Allocation With Dedup Controls
- Success threshold: A mixed or low-to-high allocation beats all-high by at least 0.05 clean validation loss or 3% perplexity in the limited-diversity condition without losing more than 1% perplexity in the diverse high-quality condition, consistently in at least two of three seeds.
- Stop condition: Stop if all-high matches or beats every mixed schedule across both limited- and high-diversity real-corpus conditions, or if quality buckets cannot be constructed with auditable dedup controls.

## Evidence references

- Artifact root: `<local-path>/projects/token-quality-allocation-at-fixed-step-budget-3b99db719b40`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
