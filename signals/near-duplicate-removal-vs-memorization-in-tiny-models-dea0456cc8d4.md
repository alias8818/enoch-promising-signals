# Near-Duplicate Removal vs Memorization in Tiny Models

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `near-duplicate-removal-vs-memorization-in-tiny-models-dea0456cc8d4`
Run ID: `near-duplicate-removal-vs-memorization-in-tiny-models-dea0456cc8d4-20260525T062041828119+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4f52e446edcb

## What looked useful

Random-secret memorization metrics can overstate memorization: in the 64-canary run, near-duplicates lowered true-secret NLL by 0.7895 versus budget-matched dedup but trained-secret rank stayed near chance (+0.0020) and greedy exact recall did not change. In the 16-canary overfit stress test, near-duplicates improved trained-secret rank by 0.3097 and greedy exact recall by 0.4167 versus budget-matched dedup.

## Boundaries and scale limits

No real corpus, no tokenizer study, no Transformer or GPT-2-small-class baseline, no large-model/full-dedup pipeline; primary direct evidence is local synthetic data with 3-5 seeds and short training runs.

## Claim scope

Synthetic canary experiments in tiny character-level GRU language models: near-duplicate retention increased generic canary-likelihood in a 64-canary run and increased identity-specific exact recall only in a smaller overfit setting; budget-matched near-duplicate removal reduced exact recall in that smaller setting.

## Why it stopped

Closed as no-paper useful signal because evidence is synthetic/tiny and mixed: the mechanism appears in a small overfit setting but not as identity-specific recall in the broader 64-canary run.

## Recommended next action

Run a bounded Transformer follow-up with the same canary-cluster controls, natural-text filler, held-out paraphrase prompts, and identity-specific trained-secret ranking before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer canary-cluster deduplication test with identity-specific recall metrics
- Success threshold: Near-duplicate retention must improve trained-secret rank by at least 0.15 and greedy/sampled exact recall by at least 0.10 over budget-matched dedup in both prompt settings, without relying on random-secret rank saturation.
- Stop condition: Stop if trained-secret rank remains within 0.05 of budget-matched dedup across three seeds or if gains appear only on random-secret alternatives while identity-specific recall stays at chance.

## Evidence references

- Artifact root: `<local-path>/projects/near-duplicate-removal-vs-memorization-in-tiny-models-dea0456cc8d4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
