# Heuristic Quality Filter Ablation at 50M Tokens

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `heuristic-quality-filter-ablation-at-50m-tokens-efc1208dc00e`
Run ID: `heuristic-quality-filter-ablation-at-50m-tokens-efc1208dc00e-20260629T003718850141+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3f57fe012b74

## What looked useful

FineWeb was operationally unsuitable here due a Hugging Face 504. On OpenWebText, strict-filter smoke was slightly worse than raw. Two 1 MB medium runs at thresholds 2.82 and 2.84 showed small filtered-minus-raw mean validation-loss improvements of roughly 0.002 to 0.004 nats, with seed-level sign flips. The filter is not clearly harmful, but the effect is too small and unstable for a paper-ready claim.

## Boundaries and scale limits

This was not a 50M-token validation. It used 200 KB to 1 MB byte-token train pools, 50 KB to 150 KB validation pools, a tiny byte-level Transformer, and public OpenWebText streaming data. It did not use BPE tokens, GPT-2-small-class training, downstream tasks, or doc-matched random controls.

## Claim scope

On a bounded OpenWebText byte-level proxy, a transparent heuristic document-quality filter produced tiny mean validation-loss improvements at 1 MB train-pool scale, but the effect was not robust across seeds and cutoffs.

## Why it stopped

Proxy-scale evidence is mixed and too weak for publication or for claiming success at the title-level 50M-token scale.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded BPE-token follow-up with doc-matched random controls before considering any 50M-token ablation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: BPE-token doc-matched quality-filter ablation on OpenWebText
- Success threshold: Filtered condition beats both raw and doc-matched random control by at least 0.01 nats mean validation loss on high-score validation, with no worse than 0.005 nats degradation on raw validation, across at least 2 of 3 seeds.
- Stop condition: Stop as negative if the filtered condition fails to beat the doc-matched random control by 0.005 nats mean high-score validation loss or if seed-level signs remain mixed.

## Evidence references

- Artifact root: `<local-path>/projects/heuristic-quality-filter-ablation-at-50m-tokens-efc1208dc00e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
