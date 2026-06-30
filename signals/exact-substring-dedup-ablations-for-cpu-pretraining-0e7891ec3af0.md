# Exact Substring Dedup Ablations for CPU Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-substring-dedup-ablations-for-cpu-pretraining-0e7891ec3af0`
Run ID: `exact-substring-dedup-ablations-for-cpu-pretraining-0e7891ec3af0-20260528T205941194047+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9412444b7082

## What looked useful

Raw training had the best unique-heldout loss in both conditions (6.6870 full-corpus bits/token; 6.1978 fixed-budget). Dedup raised duplicate-span uncertainty, e.g. doc_dedup canary 8.5202 vs raw 6.1112 full-corpus and exact_span8 boilerplate 8.5244 vs raw 0.8823, but exact_span8 worsened unique loss to 7.0737 and aggressive_span4 collapsed unique loss to 9.4719.

## Boundaries and scale limits

Five seeds on synthetic corpora up to 184860 raw training tokens and a fixed 20000-token-budget condition; no neural LM, no real web corpus, no downstream tasks, no production dedup implementation.

## Claim scope

Controlled synthetic CPU proxy with a word-trigram language model: exact document/window dedup reduces confidence on repeated boilerplate/canary spans, but does not improve unique-heldout cross-entropy versus raw training; very short exact-window dedup is harmful.

## Why it stopped

Proxy evidence is mixed/negative for validation-quality gains and clearly negative for aggressive exact-window dedup; it is not a full validation of neural CPU pretraining.

## Recommended next action

Stop this run as no-paper proxy evidence; the concrete next test is a bounded small neural LM on a real duplicate-contaminated corpus with matched token budgets and exposure metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small Neural LM Exact-Substring Dedup on Real Duplicate-Contaminated Text
- Success threshold: Moderate dedup reduces exposure by at least 2x while clean heldout loss is no worse than 1 percent above raw across at least three seeds.
- Stop condition: Stop if all dedup thresholds worsen clean heldout loss by more than 1 percent or fail to reduce duplicate-span exposure by at least 2x.

## Evidence references

- Artifact root: `<local-path>/projects/exact-substring-dedup-ablations-for-cpu-pretraining-0e7891ec3af0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
