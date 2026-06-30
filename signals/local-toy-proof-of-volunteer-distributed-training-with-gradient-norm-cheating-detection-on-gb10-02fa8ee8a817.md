# Local toy proof of volunteer distributed training with gradient-norm cheating detection on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `local-toy-proof-of-volunteer-distributed-training-with-gradient-norm-cheating-detection-on-gb10-02fa8ee8a817`
Run ID: `local-toy-proof-of-volunteer-distributed-training-with-gradient-norm-cheating-detection-on-gb10-02fa8ee8a817-20260610T093457777201+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/86984726c00f

## What looked useful

Across bounded sweeps, scaled and random-large cheating were detected at 100% and filtering recovered honest-control accuracy. Norm-matched anti-mean cheating was detected at 0%; with 25% cheaters and filtering enabled it reduced mean validation accuracy from 0.9456 to 0.7997.

## Boundaries and scale limits

No real volunteer network, no secure aggregation, no non-IID participant study, no asynchronous workers, and no large-model or multi-node training. Results support only a bounded mechanism and robustness warning.

## Claim scope

Local toy CUDA simulation with 16 synchronous volunteer workers training a tiny MLP on synthetic classification data. Robust median/MAD gradient-norm detection catches high-norm cheating but fails against norm-matched harmful gradients.

## Why it stopped

Proxy/local early falsification of gradient-norm-only cheating detection as a robust defense; not a full validation of volunteer distributed training.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should add direction/cosine or robust aggregation diagnostics and evaluate whether they catch norm-matched attacks without excessive false positives.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Toy robust aggregation diagnostics for norm-matched volunteer gradient cheating
- Success threshold: At 25% cheaters, recover final validation accuracy within 2 percentage points of the honest filtered baseline while rejecting at least 90% of norm-matched anti-mean or sign-flip harmful influence and keeping honest false positives under 5%.
- Stop condition: Stop as negative if direction-aware or robust aggregation variants either fail to improve the norm-matched anti-mean accuracy gap by at least half or exceed 10% honest false positives.

## Evidence references

- Artifact root: `<local-path>/projects/local-toy-proof-of-volunteer-distributed-training-with-gradient-norm-cheating-detection-on-gb10-`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
