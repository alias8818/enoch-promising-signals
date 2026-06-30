# Gradient-Similarity Domain Mixing for Tiny Models

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gradient-similarity-domain-mixing-for-tiny-models-fe9a3340eae5`
Run ID: `gradient-similarity-domain-mixing-for-tiny-models-fe9a3340eae5-20260525T001009422342+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/a7fbc702656d

## What looked useful

Source-only gradient-similarity mixing reduced target cross entropy by 14.50% versus uniform and recovered most of the oracle-no-conflict gain, with final average sampling weights aligned=0.940, noisy=0.022, conflict=0.038.

## Boundaries and scale limits

Synthetic data only; tiny GRU only; 5 seeds; 250 training steps; conflict domain is intentionally constructed; no real corpus, tiny transformer, GPT-2-class baseline, or long pretraining run was tested.

## Claim scope

In a controlled synthetic tiny-GRU next-token benchmark with aligned, noisy, and conflicting source domains, target-probe gradient cosine sampling consistently down-weighted harmful domains and improved target validation loss versus uniform domain mixing across 5 seeds.

## Why it stopped

No-paper closure: the current result is a synthetic mechanism probe that supports a useful signal but does not provide direct publication-grade evidence for real domain mixing.

## Recommended next action

Run a bounded deepen follow-up on tokenized real or semi-real text domains using a parameter-matched tiny transformer and the same fixed target-probe gradient policy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-text tiny-transformer gradient-similarity domain mixing
- Success threshold: Gradient-similarity mixing must beat uniform target validation loss in at least 4 of 5 seeds, improve mean target loss by at least 3%, and assign lower average weight to empirically harmful domains than to aligned domains.
- Stop condition: Stop if gradient-similarity fails to beat uniform in 3 or more seeds, if gains vanish under the simpler adaptive baseline, or if cosine traces do not distinguish harmful from aligned domains.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-similarity-domain-mixing-for-tiny-models-fe9a3340eae5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
