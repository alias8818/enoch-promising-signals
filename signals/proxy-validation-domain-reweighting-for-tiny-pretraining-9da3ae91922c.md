# Proxy-validation domain reweighting for tiny pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `proxy-validation-domain-reweighting-for-tiny-pretraining-9da3ae91922c`
Run ID: `proxy-validation-domain-reweighting-for-tiny-pretraining-9da3ae91922c-20260527T174820970334+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/1399af805d1d

## What looked useful

Across 120 seeds, matched proxy validation improved target NLL by +0.0234 at proxy_n=500 and +0.0255 at proxy_n=2000 with 120/120 positive trials, while noisy proxy_n=500 hurt target NLL by -0.00994 on average.

## Boundaries and scale limits

Closed-form bigram model over synthetic Markov domains only; no neural transformer training, no real corpus domains, no downstream evaluations, and no datacenter-scale validation.

## Claim scope

In a synthetic bigram tiny-pretraining proxy, target-like proxy validation can select domain weights that reduce held-out target NLL versus uniform mixing; deliberately mismatched proxy validation can harm performance.

## Why it stopped

No-paper closure because the evidence is a synthetic/proxy mechanism test rather than direct tiny neural pretraining validation.

## Recommended next action

Run a bounded direct tiny-transformer follow-up on real or semi-real text domains with repeated seeds, proxy-size ablations, and a proxy-mismatch control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny-transformer proxy-validation domain reweighting on real text domains
- Success threshold: Proxy-selected weights improve mean held-out target NLL versus uniform by at least 1% relative with no worse than one failed seed in three or more seeds, and the mismatched-proxy control does not show the same improvement.
- Stop condition: Stop if matched proxy selection fails to beat uniform in at least two of three seeds or if gains disappear after controlling for total target-like validation leakage.

## Evidence references

- Artifact root: `<local-path>/projects/proxy-validation-domain-reweighting-for-tiny-pretraining-9da3ae91922c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
