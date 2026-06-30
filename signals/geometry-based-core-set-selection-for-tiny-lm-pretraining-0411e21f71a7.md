# Geometry-based core-set selection for tiny LM pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `geometry-based-core-set-selection-for-tiny-lm-pretraining-0411e21f71a7`
Run ID: `geometry-based-core-set-selection-for-tiny-lm-pretraining-0411e21f71a7-20260520T162452444679+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/d77c9dd075a0

## What looked useful

Plain geometry selection achieved mean held-out loss 3.9255 versus random 3.9300 and quality-only 3.9465 in a 6-replicate persistence check. The average paired delta versus random was -0.00455 loss with 6/6 wins, while quality-filtered geometry was unstable at 3/6 wins.

## Boundaries and scale limits

Synthetic corpus only; TF-IDF geometry only; tiny transformer only; 250-step early pretraining only; no real web corpus, neural embedding selector, downstream task evaluation, or long-horizon convergence evidence.

## Claim scope

On a generated five-domain corpus, fixed-budget k-center selection over TF-IDF document geometry improved held-out next-token loss for a tiny causal transformer versus balanced random sampling in 6 of 6 paired seeds.

## Why it stopped

No-paper closure: the evidence is a useful synthetic direct-training signal, but it is not a full validation of geometry-based core-set selection for real tiny-LM pretraining.

## Recommended next action

Run a bounded real-corpus deepen test on WikiText or OpenWebText shards with the same paired-seed fixed-budget protocol and require geometry to beat random by at least 0.01 held-out loss or win at least 8 of 10 seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus paired-seed test of geometry core-set selection for tiny LM pretraining
- Success threshold: Geometry beats random by at least 0.01 held-out loss on average or wins at least 8 of 10 paired seeds without hurting any major validation slice by more than 0.02 loss.
- Stop condition: Stop if geometry fails to beat random in at least 6 of the first 10 paired seeds or if the average loss delta is within +/-0.003 after 10 seeds.

## Evidence references

- Artifact root: `<local-path>/projects/geometry-based-core-set-selection-for-tiny-lm-pretraining-0411e21f71a7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
