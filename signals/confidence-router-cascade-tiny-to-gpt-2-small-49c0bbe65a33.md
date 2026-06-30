# Confidence router cascade: tiny to GPT-2-small

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `confidence-router-cascade-tiny-to-gpt-2-small-49c0bbe65a33`
Run ID: `confidence-router-cascade-tiny-to-gpt-2-small-49c0bbe65a33-20260609T070601229536+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/0502ed0b661b

## What looked useful

The naive tiny-to-GPT-2 entropy router failed: tiny-GPT-2 entropy was effectively flat across examples (mean stdev 0.000137) and weakly anti-correlated with the tiny-vs-GPT-2 NLL gap (mean correlation -0.109). Quality-preserving operating points required 96.7% GPT-2 calls on average, eliminating meaningful cascade savings. A n-gram proxy control showed the sweep can detect a routing signal when entropy varies.

## Boundaries and scale limits

Small fixed corpus, short continuations, CPU inference, one tiny model, one expert model, and one confidence statistic. Does not evaluate learned routers, stronger small models, calibrated probabilities, latency under production serving, or broad benchmark corpora.

## Claim scope

Bounded direct inference probe of entropy-based routing from sshleifer/tiny-gpt2 to gpt2 on 104 short held-out text continuations, with always-tiny and always-GPT-2 baselines plus a mechanism-only n-gram control.

## Why it stopped

Proxy plus direct evidence completed, and the direct GPT-2-small probe showed the simple confidence statistic is not useful; this is an early falsification of the naive form, not a full validation or refutation of all cascade routers.

## Recommended next action

Stop this naive entropy-router line as an early bounded falsification; a worthwhile next test would replace the entropy-only rule with a learned/calibrated router and require <=50% GPT-2 calls while preserving at least 90% of the tiny-to-GPT-2 NLL improvement.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned confidence router for GPT-2 cascades
- Success threshold: At <=50% GPT-2 expert-call rate, preserve >=90% of the always-tiny to always-GPT-2 mean NLL improvement and show a positive calibrated relationship between router score and expert benefit.
- Stop condition: Stop if the learned router cannot beat the entropy threshold baseline by at least 20 percentage points of expert-call reduction at the same NLL gap, or if calibration remains non-monotonic on validation data.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-router-cascade-tiny-to-gpt-2-small-49c0bbe65a33`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
