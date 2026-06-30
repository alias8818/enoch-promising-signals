# Dedup-aware domain mixing tiny pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `dedup-aware-domain-mixing-tiny-pretraining-3a9b2de0c7e2`
Run ID: `dedup-aware-domain-mixing-tiny-pretraining-3a9b2de0c7e2-20260529T230701003748+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/4febaac72315

## What looked useful

Dedup-count mixing improved macro validation loss versus raw-count mixing in all 5 seeds, with mean paired delta -0.0501 loss and mean macro perplexity ratio 0.951. Raw-count sampling exposed the duplicate-heavy boilerplate domain about 78.6 examples per unique token versus about 1.4 for the diverse domains; dedup-count sampling equalized exposure near 6.2 examples per unique token.

## Boundaries and scale limits

Evidence is from a NumPy average-context causal LM, synthetic templated documents, exact duplicates, 5 seeds, and 900 training steps per condition on CPU. It is not evidence for large transformers, real web-scale corpora, near-duplicate detection, or downstream task gains.

## Claim scope

In a synthetic three-domain tiny causal-language-model probe where one domain has exact duplicate inflation, sampling domains by deduplicated token counts reduced unique held-out validation loss relative to raw-token-count sampling.

## Why it stopped

No-paper closure: this is useful synthetic mechanism evidence, not direct publication-grade validation on real corpora or transformer-scale pretraining.

## Recommended next action

Run a bounded real-text confirmation on small deduplicated domain shards with an identical tiny transformer or n-gram-controlled neural LM before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-text small-corpus confirmation of dedup-aware domain mixing
- Success threshold: Dedup-aware mixing improves macro held-out unique-document loss versus raw-count mixing in at least 3 of 3 seeds with mean loss reduction of at least 0.03 and no single domain regression above 0.05 loss.
- Stop condition: Stop as unsupported if the real-text setup shows mean macro loss delta above -0.01 or gains are explained only by one domain while another regresses by more than 0.05 loss.

## Evidence references

- Artifact root: `<local-path>/projects/dedup-aware-domain-mixing-tiny-pretraining-3a9b2de0c7e2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
