# Quality-Curriculum Data Selection for Tiny GPT-2 Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quality-curriculum-data-selection-for-tiny-gpt-2-pretraining-976b764d606c`
Run ID: `quality-curriculum-data-selection-for-tiny-gpt-2-pretraining-976b764d606c-20260611T031731873764+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bc2847f32b96

## What looked useful

Quality filtering gave a consistent proxy benefit: mean clean test loss 3.2168 versus 3.2619 for random, a -0.0451 nats delta with 5/5 paired wins. Oracle clean-only training reached 3.0733, showing selector headroom. Curriculum ordering alone was weak: high-to-low and low-to-high both had about -0.0085 nats delta versus random.

## Boundaries and scale limits

This was not GPT-2 or Tiny GPT-2 training. It used synthetic clean/noisy documents, character-level modeling, and a small NumPy neural LM on CPU. It does not validate transformer dynamics, tokenizer effects, real web data quality, downstream transfer, or larger-scale pretraining.

## Claim scope

In a five-seed NumPy autoregressive language-model proxy on a controlled clean/noisy corpus, top-half quality filtering improved clean held-out test loss versus random training, while high-to-low curriculum ordering over the full corpus was not distinguishable from anti-curriculum ordering.

## Why it stopped

Proxy evidence supports quality filtering but not curriculum-ordering as a distinct mechanism; this is an early bounded proxy result rather than full Tiny GPT-2 validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should train an actual Tiny GPT-2-class transformer with a real tokenizer on a real mixed-quality corpus and compare random, quality filtering, and curriculum ordering under equal token/FLOP budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny GPT-2 Real-Corpus Quality Filtering vs Curriculum Ordering
- Success threshold: Quality filtering improves held-out loss versus random by at least 0.03 nats or 1 percent perplexity on at least 3 seeds, and curriculum ordering exceeds anti-curriculum by at least 0.02 nats if making an ordering-specific claim.
- Stop condition: Stop if filtering fails to beat random on a majority of seeds, or if curriculum and anti-curriculum remain tied within 0.01 nats after the planned equal-budget runs.

## Evidence references

- Artifact root: `<local-path>/projects/quality-curriculum-data-selection-for-tiny-gpt-2-pretraining-976b764d606c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
