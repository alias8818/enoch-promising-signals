# Real-text tiny-transformer gradient-similarity domain mixing

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-text-tiny-transformer-gradient-similarity-domain-mixi-8fe71b55c6`
Run ID: `real-text-tiny-transformer-gradient-similarity-domain-mixi-8fe71b55c6-20260525T003342480760+0000`

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

- Parent run decision: Gradient-Similarity Domain Mixing for Tiny Models: enoch://control-plane/projects/gradient-similarity-domain-mixing-for-tiny-models-fe9a3340eae5/runs/gradient-similarity-domain-mixing-for-tiny-models-fe9a3340eae5-20260525T001009422342+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/a7fbc702656d

## What looked useful

Gradient-similarity mixing produced small target NLL gains in two of three longer direct runs but a large third-seed regression made mean target NLL worse than uniform. Raw instantaneous gradient cosine appears too unstable for the stated domain-mixing claim without smoothing or constraints.

## Boundaries and scale limits

Small character-level model, one target domain, four total domains, three seeds, short 1500-step horizon; no GPT-2-scale tokenizer/model, broad corpus, or long-run robustness.

## Claim scope

Real-text 20 Newsgroups character-level tiny Transformer LM with target domain sci.space and three auxiliary domains; matched uniform versus raw gradient-cosine auxiliary weighting over three seeds.

## Why it stopped

Controlled small direct real-text test failed the success threshold: at 1500 steps gradient-similarity improved seeds 1 and 2 by 1.10% and 1.29% target NLL but regressed seed 3 by 4.84%, making mean target NLL worse than uniform.

## Recommended next action

Stop this raw-gradient-similarity variant as no-paper evidence; run one bounded deepen test of stabilized gradient-similarity weights before considering any larger scale validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Stabilized gradient-similarity domain mixing on real text
- Success threshold: Mean target validation NLL at least 1% lower than uniform over 5 seeds, at least 4 of 5 paired wins, and no seed worse than uniform by more than 1%.
- Stop condition: Stop if stabilized weighting fails the mean 1% target-NLL improvement threshold or still shows a single-seed regression larger than 1%.

## Evidence references

- Artifact root: `<local-path>/projects/real-text-tiny-transformer-gradient-similarity-domain-mixi-8fe71b55c6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
