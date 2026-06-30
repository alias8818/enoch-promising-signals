# Small neural LM confirmation of dedup-aware domain mixing under real-text duplicate pressure

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `small-neural-lm-confirmation-of-dedup-aware-domain-mixing-5bd83272fd`
Run ID: `small-neural-lm-confirmation-of-dedup-aware-domain-mixing-5bd83272fd-20260531T124615623345+0000`

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

- Parent run decision: Dedup-aware domain mixing tiny pretraining: enoch://control-plane/projects/dedup-aware-domain-mixing-tiny-pretraining-3a9b2de0c7e2/runs/dedup-aware-domain-mixing-tiny-pretraining-3a9b2de0c7e2-20260529T230701003748+0000
- Parent run decision: Real-text small-corpus confirmation of dedup-aware domain mixing: enoch://control-plane/projects/real-text-small-corpus-confirmation-of-dedup-aware-domain-a2807af629/runs/real-text-small-corpus-confirmation-of-dedup-aware-domain-a2807af629-20260530T033903467190+0000

## What looked useful

Dedup-aware domain mixing removed most of the duplicate-induced macro LM loss penalty: naive duplicate-exposed minus dedup-aware test macro NLL was +0.1696 with all three seeds positive, driven by a +0.5429 literature NLL recovery while sacrificing -0.2038 on the duplicated technical domain. The no-duplicate unique control was within +0.0035 macro NLL of dedup-aware, supporting duplicate-skew cancellation as the mechanism.

## Boundaries and scale limits

Small neural n-gram LM rather than Transformer/GPT architecture; two public text domains; injected chunk duplication rather than naturally mined web duplicates; 600 training steps per seed; no downstream task evaluation or web-scale pretraining.

## Claim scope

In a two-domain real-text experiment with an 8x duplicated technical domain, a small NumPy neural n-gram LM trained with dedup-aware balanced domain sampling achieved lower balanced held-out LM loss than a naive duplicate-exposed raw-corpus sampling baseline across three fixed seeds, while matching a no-duplicate unique-data control on macro loss.

## Why it stopped

Medium local evidence supports the mechanism but is not paper-positive because the LM architecture, domain count, duplicate source, and training scale are too small for a broad pretraining claim.

## Recommended next action

Run a bounded deepen follow-up with a parameter-matched small Transformer/BPE LM on at least four real domains with mined or injected duplicate clusters, preserving the same naive-vs-dedup-vs-no-duplicate controls and paired fixed seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small Transformer confirmation of dedup-aware domain mixing across multi-domain duplicate clusters
- Success threshold: Dedup-aware sampling improves test macro NLL versus naive duplicate-exposed sampling by at least 0.05 mean NLL across paired seeds, with the improvement positive on at least 4 of 5 seeds and no-duplicate control within 0.03 macro NLL of dedup-aware.
- Stop condition: Stop as unsupported if dedup-aware macro NLL improvement is below 0.02 mean or not directionally positive on a majority of paired seeds, or if improvements vanish when duplicate-domain identity is varied.

## Evidence references

- Artifact root: `<local-path>/projects/small-neural-lm-confirmation-of-dedup-aware-domain-mixing-5bd83272fd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
