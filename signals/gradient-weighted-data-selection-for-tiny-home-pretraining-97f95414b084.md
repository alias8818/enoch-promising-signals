# Gradient-weighted data selection for tiny home pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-weighted-data-selection-for-tiny-home-pretraining-97f95414b084`
Run ID: `gradient-weighted-data-selection-for-tiny-home-pretraining-97f95414b084-20260527T222143760014+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/0baf61e57fbd

## What looked useful

Gradient-target cosine selection reliably shifted sampling toward the aligned source and away from random/anti sources, beating uniform on all seeds; the cheaper loss-weighted selector concentrated more strongly on the aligned source and beat gradient weighting on all seeds.

## Boundaries and scale limits

Synthetic Markov data, small GRU, 320 update steps per method, 4 seeds, same-process generated validation data; no real text corpus, tokenizer, transformer, GPT-2-small-class baseline, downstream task, or long-run pretraining evidence.

## Claim scope

On a synthetic five-source Markov next-token tiny-pretraining proxy with a small GRU and 4 seeds, gradient-weighted source sampling improves target validation loss over uniform sampling by 0.165 mean cross-entropy but does not beat a simple loss-weighted selector.

## Why it stopped

Proxy evidence is mixed: gradient weighting is viable versus uniform but consistently loses to a simple baseline, so this is not a full validation or paper-positive result.

## Recommended next action

Stop this run as a no-paper useful signal; next run should test gradient alignment versus tuned loss weighting on a real tiny text pretraining setup before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real tiny-transformer comparison of gradient-aligned and loss-weighted source selection
- Success threshold: Gradient-aligned selection must reduce final target-domain validation loss by at least 0.05 cross-entropy versus the best tuned non-gradient baseline on at least 3 seeds, without using more total train/probe tokens.
- Stop condition: Stop if gradient-aligned selection fails to beat tuned loss weighting on at least 2 of 3 seeds or if source-allocation diagnostics show it is only replicating the same aligned-source concentration as loss weighting.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-weighted-data-selection-for-tiny-home-pretraining-97f95414b084`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
