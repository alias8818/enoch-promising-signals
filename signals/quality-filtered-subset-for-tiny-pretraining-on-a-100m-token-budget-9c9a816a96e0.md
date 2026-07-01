# Quality-filtered subset for tiny pretraining on a 100M sequence-item budget

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quality-filtered-subset-for-tiny-pretraining-on-a-100m-token-budget-9c9a816a96e0`
Run ID: `quality-filtered-subset-for-tiny-pretraining-on-a-100m-token-budget-9c9a816a96e0-20260610T235656384513+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/603d8d89d296

## What looked useful

The cheap lexical filter removed obvious noise but assigned high scores to word-shuffled text, causing the selected subset to slightly underperform random by +0.012357 byte NLL (+0.56%). Oracle-clean beat random by -0.057306 byte NLL, showing that true quality selection can help in the same setup.

## Boundaries and scale limits

Tiny GRU byte LM, 120k-byte subset budget, 3 seeds, synthetic corruptions, and WikiText-2 validation only; not a 100M-token, web-scale, tokenizer-scale, or production-quality-filter validation.

## Claim scope

Bounded proxy on WikiText-2-derived synthetic quality mixtures: a shallow lexical quality filter did not improve tiny byte-level LM held-out clean byte NLL versus random selection at equal byte budget, while an oracle-clean selector did improve it.

## Why it stopped

Proxy early falsification of the shallow lexical quality-filter hypothesis, not a full 100M-token validation.

## Recommended next action

Stop this run as a no-paper useful signal; next run should test a coherence-aware or reference-LM quality score against this lexical filter and random under the same equal-budget protocol.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Coherence-aware quality filtering for tiny equal-budget pretraining
- Success threshold: Coherence-aware filtering must beat random and the lexical filter by at least 1% mean held-out clean byte NLL across 3 seeds, with no seed worse than random.
- Stop condition: Stop if the coherence-aware filter fails to beat random by at least 1% mean held-out clean byte NLL on the synthetic mixture, or if it still admits substantial word-shuffled content.

## Evidence references

- Artifact root: `<local-path>/projects/quality-filtered-subset-for-tiny-pretraining-on-a-100m-token-budget-9c9a816a96e0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
