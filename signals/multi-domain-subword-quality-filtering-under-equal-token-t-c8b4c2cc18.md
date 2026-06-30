# Multi-domain subword quality filtering under equal-token tiny-transformer pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `multi-domain-subword-quality-filtering-under-equal-token-t-c8b4c2cc18`
Run ID: `multi-domain-subword-quality-filtering-under-equal-token-t-c8b4c2cc18-20260531T105720915354+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real-corpus quality filtering for a tiny transformer under equal-token CPU pretraining: enoch://control-plane/projects/real-corpus-quality-filtering-for-a-tiny-transformer-under-e9df7dc4d2/runs/real-corpus-quality-filtering-for-a-tiny-transformer-under-e9df7dc4d2-20260530T050813691569+0000
- Parent run decision: Quality-filtered tiny pretraining on CPU: enoch://control-plane/projects/quality-filtered-tiny-pretraining-on-cpu-638ab37768c9/runs/quality-filtered-tiny-pretraining-on-cpu-638ab37768c9-20260530T010847274843+0000

## What looked useful

Across fixed seeds 11, 23, and 37, random baseline mean validation loss was 5.954954. Global quality_best filtering worsened loss to 19.543779, domain_balanced_quality_best worsened it to 10.518577, quality_worst worsened it to 7.371983, and score_shuffled_control matched baseline at 5.954471. The shuffled control indicates the effect is tied to score-based selection; the domain-balanced ablation indicates preserving coarse domain coverage does not rescue this naive subword-quality filter.

## Boundaries and scale limits

The corpus is local OS/Python docs/code plus deterministic synthetic fallback prose/web text; the model is much smaller than GPT-2-small and trained for short CPU-bounded runs. The result is a bounded Tier 2 falsification for this scoring/filtering rule, not a web-scale pretraining conclusion.

## Claim scope

On a local five-domain corpus with a 768-token BPE tokenizer and a 2-layer tiny causal Transformer trained for 180 optimizer steps under equal 48k-token budgets, naive subword-quality filtering by low BPE tokens-per-character does not improve mixed-domain validation loss over random sampling.

## Why it stopped

Tier 2 direct LM evidence with fixed seeds, a real random baseline, shuffled-score control, worst-score ablation, and domain-balanced quality ablation falsified the expected improvement for the tested filtering rule.

## Recommended next action

Stop this follow-up as a useful negative result; do not scale naive token-per-character subword-quality filtering without first replacing the selection rule with one that explicitly preserves diversity and demonstrates a local win over random sampling.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/multi-domain-subword-quality-filtering-under-equal-token-t-c8b4c2cc18`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
