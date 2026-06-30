# Tiny Quality Classifier Pre-filtering for Pretrain Mix

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-quality-classifier-pre-filtering-for-pretrain-mix-318e8c7a110b`
Run ID: `tiny-quality-classifier-pre-filtering-for-pretrain-mix-318e8c7a110b-20260619T201712030692+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/cf144e17405a

## What looked useful

Classifier-selected subsets improved clean validation loss versus random by 15.7% in smoke and 41.8% in medium, nearly matching oracle selection, but mixed-distribution validation loss degraded sharply because aggressive quality filtering removed noisy modes.

## Boundaries and scale limits

Synthetic corpus only; tiny hand-feature classifier; tiny character GRU; 45k and 180k character budgets; no real web data, GPT-2-small-class Transformer, long-token pretraining, or robustness sweep.

## Claim scope

In a synthetic document-mixture proxy, a tiny trained quality classifier can select a fixed pretraining subset that improves clean-target validation loss for a tiny character GRU LM versus random and unfiltered controls.

## Why it stopped

Closed as no-paper useful signal: local synthetic evidence supports the mechanism but is not direct/full validation and reveals a distribution-coverage tradeoff.

## Recommended next action

Run a bounded real-data follow-up using a small labeled/proxy-quality corpus and a GPT-2-small-class or parameter-matched Transformer, including mixture-retention ablations to measure the clean-loss gain versus mixed-loss regression.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-data bounded quality-filter pretraining with retention ablations
- Success threshold: At least 5% clean-validation loss improvement versus random at the same token budget while mixed-validation loss regresses by no more than 10% versus unfiltered or random.
- Stop condition: Stop if pure or retention-based quality filtering fails to beat random on clean validation, or if every clean-loss gain requires more than 10% mixed-validation degradation.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-quality-classifier-pre-filtering-for-pretrain-mix-318e8c7a110b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
