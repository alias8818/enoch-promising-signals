# CPU MinHash Data Selection for Cheap Home Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-minhash-data-selection-for-cheap-home-pretraining-d4648e97f735`
Run ID: `cpu-minhash-data-selection-for-cheap-home-pretraining-d4648e97f735-20260521T232504431238+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/ba50c91d1226

## What looked useful

CPU MinHash-LSH is useful as a cheap near-duplicate suppression component, giving about 10x faster selection than exact dedup in this implementation and improving quality-only validation NLL by 0.092727, but standalone MinHash+quality selection remained 0.122966 NLL worse than random because it did not correct topic/coverage skew.

## Boundaries and scale limits

No real corpus, no neural LM, no tokenizer-level pretraining, no human quality labels, and no long/full-scale training. Results are bounded to 800-document smoke and three 2500-document synthetic medium seeds.

## Claim scope

Synthetic CPU-only proxy with imbalanced topic distribution, near-duplicate bursts, fixed document budget, and smoothed word-bigram validation on a balanced held-out target. MinHash-LSH + quality improves duplicate suppression, coverage, and validation NLL versus quality-only selection, but does not beat random selection on the balanced target.

## Why it stopped

Proxy/early falsification of standalone CPU MinHash data selection: it improved deduplication and quality-only selection but failed the stronger random baseline on balanced validation coverage and bigram NLL.

## Recommended next action

Stop this run as a no-paper useful signal; next bounded test should add explicit target coverage or topic-diversity quotas to MinHash selection and compare on a real small corpus with a small neural LM.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Coverage-Aware CPU MinHash Selection on a Real Small Corpus
- Success threshold: Coverage-aware MinHash must beat random and quality-only by at least 3% relative validation loss while keeping near-duplicate rate no worse than random and CPU selection time under 15 minutes for the chosen corpus.
- Stop condition: Stop if coverage-aware MinHash does not beat random on neural validation loss in two independent seeds or if CPU preprocessing exceeds the 15-minute local budget without checkpointable progress.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-minhash-data-selection-for-cheap-home-pretraining-d4648e97f735`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
