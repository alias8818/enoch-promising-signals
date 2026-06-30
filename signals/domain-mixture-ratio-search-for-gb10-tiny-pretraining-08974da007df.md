# Domain Mixture Ratio Search for GB10 Tiny Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `domain-mixture-ratio-search-for-gb10-tiny-pretraining-08974da007df`
Run ID: `domain-mixture-ratio-search-for-gb10-tiny-pretraining-08974da007df-20260611T173619671261+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/33572c430bc7

## What looked useful

The target mixture beat uniform by 0.0156 absolute target-weighted loss, a 0.98% relative reduction, but only on 2 of 3 seeds. The no-wiki control was much worse at 2.9234 mean loss versus 1.5885 for uniform, showing the harness can detect harmful domain omission.

## Boundaries and scale limits

Synthetic token generators only; 8 hand-written candidate mixtures; 3 seeds; 160 optimizer steps per candidate/seed; no real corpora, no downstream evaluation, no learned optimizer/search algorithm, and no full-scale or overnight pretraining validation.

## Claim scope

Synthetic tiny causal-Transformer pretraining over four generated domains showed that candidate domain mixture ratios affect held-out target-mixture loss under a fixed 15.7M-token search budget; the target-matching mixture was best on average, while omitting a target domain was clearly harmful.

## Why it stopped

Synthetic bounded evidence is useful for mechanism and harness validation, but the best-vs-uniform effect is small, not seed-unanimous, and not direct real-pretraining evidence.

## Recommended next action

Stop this run as a no-paper useful signal; next run should repeat the same fixed-budget mixture search on small real corpora with uniform, target, selected-ratio, and omitted-domain controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small real-corpus domain-mixture confirmation for GB10 tiny pretraining
- Success threshold: Selected or target-informed mixture improves target-weighted held-out loss by at least 2% relative versus uniform and wins on at least 4 of 5 seeds without worsening any target domain by more than 5% relative.
- Stop condition: Stop as negative if no candidate beats uniform by at least 1% relative mean loss, if the apparent winner fails to beat uniform on a majority of seeds, or if gains come only from synthetic/proxy metrics without real-corpus validation.

## Evidence references

- Artifact root: `<local-path>/projects/domain-mixture-ratio-search-for-gb10-tiny-pretraining-08974da007df`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
