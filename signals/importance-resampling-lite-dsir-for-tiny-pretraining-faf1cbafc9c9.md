# Importance Resampling Lite (DSIR) for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `importance-resampling-lite-dsir-for-tiny-pretraining-faf1cbafc9c9`
Run ID: `importance-resampling-lite-dsir-for-tiny-pretraining-faf1cbafc9c9-20260613T123650646193+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3c2469b6e979

## What looked useful

Across 3 seeds with 15% target prevalence, DSIR-lite selected ~1.000 target fraction versus 0.166 uniform and improved target NLL by 0.556 with 42.8% lower perplexity; in a 5% target-prevalence probe it selected 0.985 target fraction versus 0.045 uniform and improved NLL by 2.812, nearly matching oracle target-only training.

## Boundaries and scale limits

Evidence is synthetic/proxy-only: no real web corpus, no tokenizer/dedup/leakage controls beyond generated templates, no GPT-2-small-class training, no long-run scaling, and no downstream transfer evaluation.

## Claim scope

In a self-contained synthetic mixed-domain tiny-pretraining benchmark, bigram DSIR-lite density-ratio selection from a small target seed enriched target-domain examples and improved target validation NLL versus uniform selection under identical tiny Transformer training budgets.

## Why it stopped

Closed as no-paper useful signal because the evidence supports the mechanism only in synthetic proxy corpora, not direct natural-corpus pretraining.

## Recommended next action

Run a bounded real-corpus confirmation using a held-out target domain and fixed token budget before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus DSIR-lite confirmation for tiny target-domain pretraining
- Success threshold: DSIR-lite reduces target validation NLL by at least 0.10 versus uniform selection across at least 3 seeds and does not trail an available target-only upper-control by more than 20% of the uniform-to-oracle gap.
- Stop condition: Stop if DSIR-lite does not beat uniform by at least 0.03 target validation NLL on a smoke real-corpus run or if leakage/domain-label diagnostics show the selection task is not valid.

## Evidence references

- Artifact root: `<local-path>/projects/importance-resampling-lite-dsir-for-tiny-pretraining-faf1cbafc9c9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
