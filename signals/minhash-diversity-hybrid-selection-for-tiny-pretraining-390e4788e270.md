# MinHash-diversity hybrid selection for tiny pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `minhash-diversity-hybrid-selection-for-tiny-pretraining-390e4788e270`
Run ID: `minhash-diversity-hybrid-selection-for-tiny-pretraining-390e4788e270-20260604T170322129591+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/b57543c984e7

## What looked useful

Explicit diversity helped more than quality-only or MinHash+quality selection, but the tested hybrid weighting reduced unique template-family coverage and consistently underperformed diversity-only. Hybrid mean validation loss was 3.9934 vs 3.8277 for topic_diversity and 3.9346 for random.

## Boundaries and scale limits

Three synthetic corpus seeds, 192 selected documents per method per seed, a 250,088-parameter Transformer, and short CUDA training runs; not validated on real web text, exact token budgets, downstream tasks, GPT-2-small-class models, or long pretraining.

## Claim scope

On a controlled synthetic tiny-pretraining benchmark with topic skew, quality variation, and MinHash-detectable near duplicates, the implemented greedy hybrid selector improved over quality-only and MinHash+quality controls but did not outperform random selection or a simpler topic-diversity selector.

## Why it stopped

Proxy controlled evidence rejects paper-readiness for the tested hybrid: it never beat diversity-only or random across three seeds, so this is an early bounded falsification rather than a full validation.

## Recommended next action

Run a token-matched deepen test on a small real corpus comparing diversity-only against a tuned MinHash-quality-diversity weight sweep before considering any larger pretraining validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Token-matched real-corpus diversity versus tuned MinHash hybrid selection
- Success threshold: A tuned hybrid must beat diversity-only and random by at least 0.03 validation-loss points on mean paired loss across three seeds while keeping duplicate-cluster repeats no worse than diversity-only.
- Stop condition: Stop if no hybrid setting beats diversity-only on at least two of three seeds or if improvements disappear after exact token matching.

## Evidence references

- Artifact root: `<local-path>/projects/minhash-diversity-hybrid-selection-for-tiny-pretraining-390e4788e270`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
